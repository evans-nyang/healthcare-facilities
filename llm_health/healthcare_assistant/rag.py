from openai import OpenAI
import os
import json
from time import time
from dotenv import load_dotenv

import ingest

# Load environment variables from the .env file
load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]
)


index = ingest.load_data()


def search(query):
    boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results


prompt_template = """
You're a course healthcare information assistant. Answer the QUESTION based on the CONTEXT from the healthcare database. 
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: {context}
""".strip()


entry_template = """
name: {name}
keph_level: {keph_level}
facility_type: {facility_type}
owner: {owner}
regulatory_body: {regulatory_body}
beds: {beds}
cots: {cots}
county: {county}
constituency: {constituency}
sub_county: {sub_county}
ward: {ward} 
operation_status: {operation_status}
open_whole_day: {open_whole_day}
open_public_holidays: {open_public_holidays}
open_weekends: {open_weekends}
open_late_night: {open_late_night}
approved: {approved}
public_visible: {public_visible}
closed: {closed}
"""


def build_prompt(query, search_results):

    context_str = ""

    for doc in search_results:
        context_str = context_str + entry_template.format(**doc) + "\n\n"

    prompt = prompt_template.format(question=query, context=context_str).strip()
    return prompt 


def llm(prompt, model='gpt-4o'):
    response = client.chat.completions.create(
        model = model,
        messages = [{"role": "user", "content": prompt}]
    )

    answer = response.choices[0].message.content
    token_stats = {
        "prompt_tokens": response.usage.prompt_tokens,
        "completion_tokens": response.usage.completion_tokens,
        "total_tokens": response.usage.total_tokens,
    }

    return answer, token_stats


evaluation_prompt_template = """
You are an expert evaluator for a Retrieval-Augmented Generation (RAG) system.
Your task is to analyze the relevance of the generated answer to the given question.
Based on the relevance of the generated answer, you will classify it
as "NON_RELEVANT", "PARTLY_RELEVANT", or "RELEVANT".

Here is the data for evaluation:

Question: {question}
Generated Answer: {answer}

Please analyze the content and context of the generated answer in relation to the question
and provide your evaluation in parsable JSON without using code blocks:

{{
  "Relevance": "NON_RELEVANT" | "PARTLY_RELEVANT" | "RELEVANT",
  "Explanation": "[Provide a brief explanation for your evaluation]"
}}
""".strip()

def evaluate_relevance(question, answer):
    prompt = evaluation_prompt_template.format(question=question, answer=answer)
    evaluation, tokens = llm(prompt, model='gpt-4o')

    try:
        eval_data = json.loads(evaluation)
        return eval_data, tokens
    except json.JSONDecodeError:
        result = {
            "Relevance": "UNKNOWN",
            "Explanation": "Failed to parse evaluation"
        }
        return result, tokens
    

def calculate_cost(model, tokens):
    openai_cost = 0

    if model == "gpt-4o":
        openai_cost = (tokens["total_tokens"] * 0.00250 + tokens["completion_tokens"] * 0.01) / 1000
    else:
        print("Invalid model specified. No cost calculated.")

    return openai_cost


def rag(query, model='gpt-4o'):
    t0 = time()
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer, token_stats = llm(prompt, model=model)

    relevance, relevance_token_stats = evaluate_relevance(query, answer)

    t1 = time()
    took = t1 - t0

    openai_cost_rag = calculate_cost(model, token_stats)
    openai_cost_eval = calculate_cost(model, relevance_token_stats)

    openai_cost = openai_cost_rag + openai_cost_eval

    return {
        "answer": answer,
        "model_used": model,
        "response_time": took,
        "relevance": relevance.get("Relevance", "UNKNOWN"),
        "relevance_explanation": relevance.get("Explanation", "Failed to parse evaluation"),
        "prompt_tokens": token_stats["prompt_tokens"],
        "completion_tokens": token_stats["completion_tokens"],
        "total_tokens": token_stats["total_tokens"],
        "eval_prompt_tokens": relevance_token_stats["prompt_tokens"],
        "eval_completion_tokens": relevance_token_stats["completion_tokens"],
        "eval_total_tokens": relevance_token_stats["total_tokens"],
        "openai_cost": openai_cost
    }
