# streamlit_app.py
import streamlit as st
import requests

# Define the base URL for your FastAPI app
BASE_URL = "http://localhost:8000"  # Update if running FastAPI elsewhere

st.title("Healthcare Assistant")

# Section to ask a question
st.header("Ask a Question")
question = st.text_input("Enter your question:")

if st.button("Submit Question"):
    if question:
        # Send a POST request to the /ask endpoint
        response = requests.post(f"{BASE_URL}/ask", json={"question": question})
        
        if response.status_code == 200:
            data = response.json()
            st.write(data["result"])
            # st.write("**Answer:**", data["result"])
            # st.write("**Conversation ID:**", data["conversation_id"])
            st.session_state["conversation_id"] = data["conversation_id"]
        else:
            st.error("Error: Unable to retrieve answer. Please try again.")
    else:
        st.warning("Please enter a question.")

# Section to provide feedback
st.header("Provide Feedback")
if "conversation_id" in st.session_state:
    feedback = st.radio("Was the answer helpful?", ("👍 Yes", "👎 No"))
    if st.button("Submit Feedback"):
        feedback_value = 1 if feedback == "👍 Yes" else -1
        feedback_response = requests.post(
            f"{BASE_URL}/feedback",
            json={"conversation_id": st.session_state["conversation_id"], "feedback": feedback_value},
        )
        
        if feedback_response.status_code == 200:
            st.success("Feedback submitted successfully!")
        else:
            st.error("Error: Unable to submit feedback.")
else:
    st.info("Ask a question first to provide feedback.")
