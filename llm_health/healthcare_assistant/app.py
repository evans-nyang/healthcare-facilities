from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

from rag import rag

app = FastAPI()

# Define Pydantic models for request and response payloads
class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    conversation_id: str
    question: str
    result: str
    
class FeedbackRequest(BaseModel):
    conversation_id: str
    feedback: int


# POST endpoint to ask a question
@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    question = request.question

    if not question:
        raise HTTPException(status_code=400, detail="No question provided")

    # Call the RAG function to generate the answer
    result = rag(question)
    answer = result["answer"]

    # Generate a unique conversation ID (UUID)
    conversation_id = str(uuid.uuid4())

    # Return the result, conversation ID, and question
    return AnswerResponse(
        conversation_id=conversation_id,
        question=question,
        result=answer
    )


# POST endpoint to handle user feedback
@app.post("/feedback")
async def feedback(request: FeedbackRequest):
    conversation_id = request.conversation_id
    feedback = request.feedback  # +1 for positive, -1 for negative

    if not conversation_id or feedback not in [-1, 1]:
        raise HTTPException(status_code=400, detail="Invalid input")

    print(f"Feedback received: Conversation ID = {conversation_id}, Feedback = {feedback}")

    return {"message": "Feedback received"}
