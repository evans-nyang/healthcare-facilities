from openai import OpenAI
import os
from dotenv import load_dotenv
import ingest

# Load environment variables from the .env file
load_dotenv()
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

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

    return response.choices[0].message.content


def rag(query):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    response = llm(prompt)
    return {"answer": response}
