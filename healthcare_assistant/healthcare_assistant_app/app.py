from fastapi import FastAPI, HTTPException
import uuid

from rag import rag
import db
from models import QuestionRequest, FeedbackRequest


app = FastAPI()


# POST endpoint to ask a question
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    question = request.question

    if not question:
        raise HTTPException(status_code=400, detail="No question provided")

    # Call the RAG function to generate the answer
    answer_data = rag(question)

    # Generate a unique conversation ID (UUID)
    conversation_id = str(uuid.uuid4())

    # Save the conversation to the database
    db.save_conversation(
        conversation_id=conversation_id,
        question=question,
        answer_data=answer_data
    )

    return {
        "conversation_id": conversation_id,
        "question": question,
        "result": answer_data["answer"]
    }


# POST endpoint to handle user feedback
@app.post("/feedback")
async def feedback(request: FeedbackRequest):
    conversation_id = request.conversation_id
    feedback = request.feedback  # +1 for positive, -1 for negative

    if not conversation_id or feedback not in [-1, 1]:
        raise HTTPException(status_code=400, detail="Invalid input")
    
    # Save the feedback in the database
    db.save_feedback(
        conversation_id=conversation_id,
        feedback=feedback,
    )

    return {
        "message": "Feedback received",
        "conversation_id": conversation_id,
        "feedback": feedback
    }

# Run the FastAPI app with Uvicorn server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
