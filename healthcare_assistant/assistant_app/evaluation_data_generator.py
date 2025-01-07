import json
import os
from time import sleep

import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from tqdm.auto import tqdm

load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"]
)

df = pd.read_csv('../data/kenya_health_facilities_clean.csv')
documents = df.to_dict(orient='records')

prompt_template = """
You emulate a user of our healthcare facility assistant application.
Formulate 5 diverse questions this user might ask based on the provided healthcare facility. The record
should contain the answer to the questions, and the questions should be complete and not too short. 
Ensure the questions are diverse and not similar to each other. Use as fewer words as possible from the record. 

The record:

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

Provide the output in parsable JSON without using code blocks:

["question1", "question2", ..., "question5"]
""".strip()

def generate_questions(doc):
    prompt = prompt_template.format(**doc)
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)

def main():
    results = {}

    # Load existing results from CSV file
    existing_results = pd.read_csv('../data/ground_truth_retrieval.csv')
    existing_doc_ids = set(existing_results['id'])

    for i, doc in enumerate(tqdm(documents)):
        doc_id = doc['id']
        if doc_id in existing_doc_ids:
            continue

        questions = generate_questions(doc)
        results[doc_id] = questions

        if (i + 1) % 10 == 0:
            sleep(60)

    final_results = [(doc_id, q) for doc_id, questions in results.items() for q in questions]

    df_results = pd.DataFrame(final_results, columns=['id', 'question'])
    existing_results = pd.concat([existing_results, df_results], ignore_index=True)
    existing_results.to_csv('./ground_truth_data.csv', index=False)

if __name__ == "__main__":
    main()
