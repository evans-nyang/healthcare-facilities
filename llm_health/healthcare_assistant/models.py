from pydantic import BaseModel


# Define Pydantic models for request and response payloads
class QuestionRequest(BaseModel):
    question: str
    
class FeedbackRequest(BaseModel):
    conversation_id: str
    feedback: int
