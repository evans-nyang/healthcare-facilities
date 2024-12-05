import logging
import os
import uuid
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from rag import rag
from db import init_db, save_conversation, save_feedback
from models import QuestionRequest, FeedbackRequest


# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define an async context manager for lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Initializing database...")
        init_db()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {str(e)}")
        raise HTTPException(status_code=500, detail="Database initialization failed")
    
    yield
    

app = FastAPI(lifespan=lifespan)

# Get origins from environment variables
ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000"
).split(",")

# Add CORS middleware to allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    save_conversation(
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
    save_feedback(
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
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=port,
        reload=False  # Set to False in production
    )
