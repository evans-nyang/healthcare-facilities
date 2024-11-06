import streamlit as st
import requests
from PIL import Image


# Define the base URL for your FastAPI app
BASE_URL = "http://localhost:8000" 


# Add a logo image 
logo = Image.open("../images/logo.png")
st.image(logo, width=100)

# App title and description
st.title("Healthcare Facility Assistant")
st.write("Welcome to the Healthcare Facility Assistant! Ask questions and provide feedback to improve our service.")

# Question Input Section
st.subheader("Ask a Question")
question = st.text_input("What would you like to know?")

if st.button("Submit Question", key="question_button"):
    if question:
        # Send a POST request to the /ask endpoint
        response = requests.post(f"{BASE_URL}/ask", json={"question": question})
        
        if response.status_code == 200:
            data = response.json()
            st.write(data["result"])
            st.session_state["conversation_id"] = data["conversation_id"]
        else:
            st.error("Error: Unable to retrieve answer. Please try again.")
    else:
        st.warning("Please enter a question before submitting.")

# Feedback Section
st.subheader("Provide Feedback")
if "conversation_id" in st.session_state:
    st.write("Help us improve by letting us know if the answer was helpful!")
    feedback = st.radio("Was the answer helpful?", ("👍 Yes", "👎 No"))
    if st.button("Submit Feedback", key="feedback_button"):
        feedback_value = 1 if feedback == "👍 Yes" else -1
        feedback_response = requests.post(
            f"{BASE_URL}/feedback",
            json={"conversation_id": st.session_state["conversation_id"], "feedback": feedback_value},
        )
        
        if feedback_response.status_code == 200:
            st.success("Thank you! Feedback submitted successfully.")
        else:
            st.error("Error: Unable to submit feedback.")
else:
    st.info("Please ask a question first to provide feedback.")
