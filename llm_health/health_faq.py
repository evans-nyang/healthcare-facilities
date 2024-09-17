import streamlit as st
from openai import OpenAI
from elasticsearch import Elasticsearch
import requests

# Elasticsearch client setup
es_client = Elasticsearch('http://localhost:9200')

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama'
)

def elastic_search(query, index_name='medical_facilities'):
    search_query = {
        "size": 5,
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["Name^3", "County", "Constituency", "Sub_county", "Ward"]
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    result_docs = []

    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])

    return result_docs

def build_prompt(query, search_results):
    prompt_template = """
        You're a healthcare facility data AI assistant. Answer the QUESTION based on the CONTEXT from the healthcare facilities database.
        Use only the facts from the CONTEXT when answering the QUESTION.

        QUESTION: {question}

        CONTEXT: {context}
    """.strip()

    context_str = ""

    for doc in search_results:
        context_str += (
            f"Name: {doc['Name']}\n"
            f"Code: {doc['Code']}\n"
            f"Keph Level: {doc['Keph_level']}\n"
            f"Facility Type: {doc['Facility_type']}\n"
            f"Owner: {doc['Owner']}\n"
            f"County: {doc['County']}\n"
            f"Constituency: {doc['Constituency']}\n"
            f"Sub County: {doc['Sub_county']}\n"
            f"Ward: {doc['Ward']}\n"
            f"Operational Status: {doc['Operation_status']}\n"
            f"Beds: {doc['Beds']}\n"
            f"Cots: {doc['Cots']}\n\n"
        )

    prompt = prompt_template.format(question=query, context=context_str).strip()
    return prompt

# def llm(prompt):
#     payload = {
#         "prompt": prompt
#     }
#     headers = {
#         'Content-Type': 'application/json'
#     }
#     response = requests.post(OLLAMA_API_URL, headers=headers, json=payload)
#     response_data = response.json()
#     return response_data['response']
def llm(prompt):
    response = client.chat.completions.create(
        model = 'phi3',
        messages = [{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

def rag(query):
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer

# Streamlit app
def main():
    st.title("Healthcare Facility Data Assistant")

    # Input box
    user_input = st.text_input("Enter your question about healthcare facilities: ")

    # Button to invoke the RAG function
    if st.button("Ask"):
        with st.spinner('Processing your input...'):
            # Call the RAG function
            output = rag(user_input)
            st.success('Completed!')
            st.write(output)

if __name__ == "__main__":
    main()
