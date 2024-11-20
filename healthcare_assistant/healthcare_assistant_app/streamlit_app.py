import streamlit as st
import requests
from PIL import Image

# Define the base URL for your FastAPI app
BASE_URL = "http://127.0.0.1:8000"  # Update if running FastAPI elsewhere

# Initialize session state to maintain conversation history
if "history" not in st.session_state:
    st.session_state.history = []  # To store chat history
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = None  # To store the conversation ID


# Function to handle sending questions
def send_question():
    user_input = st.session_state.user_question
    if not user_input.strip():
        st.warning("Please enter a valid question.")
        return

    # Send question to backend
    response = requests.post(f"{BASE_URL}/ask", json={"question": user_input})
    if response.status_code == 200:
        data = response.json()
        bot_response = data["result"]
        st.session_state.conversation_id = data["conversation_id"]
        st.session_state.history.append(("You", user_input))
        st.session_state.history.append(("Assistant", bot_response))
    else:
        st.error("Error: Unable to retrieve answer. Please try again.")
    
    # Clear the input field after processing
    st.session_state.user_question = ""

# Function to submit feedback
def submit_feedback(feedback):
    if not st.session_state.conversation_id:
        st.error("No conversation to provide feedback for.")
        return

    feedback_value = 1 if feedback == "Yes 👍" else -1
    feedback_response = requests.post(
        f"{BASE_URL}/feedback",
        json={"conversation_id": st.session_state.conversation_id, "feedback": feedback_value},
    )
    if feedback_response.status_code == 200:
        st.success("Feedback submitted successfully!")
    else:
        st.error("Error: Unable to submit feedback.")

# Add a logo image 
# logo = Image.open("../../media/logo.png")
# st.image(logo, width=100)

# Streamlit UI
st.title("💬 Chat with the Healthcare Assistant")
st.markdown("Ask your healthcare-related questions below and receive assistance instantly.")

# Display chat history
st.subheader("Chat History")
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f"**You**: {message}")
    else:
        st.markdown(f"**Assistant**: {message}")

# Input field and send button
st.text_input(
    "Type your question:",
    placeholder="Ask your question here...",
    key="user_question",
    on_change=send_question,
)

# Feedback section
if st.session_state.conversation_id:
    st.subheader("Was this response helpful?")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Yes 👍", on_click=submit_feedback, args=("Yes 👍",))
    with col2:
        st.button("No 👎", on_click=submit_feedback, args=("No 👎",))

# Run the Streamlit app as `streamlit run app.py`
