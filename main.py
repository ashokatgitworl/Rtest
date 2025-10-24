from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from service import get_ai_response
import uvicorn
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Chatbot API",
    description="A simple AI chatbot powered by Groq and LangChain",
    version="1.0.0"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest) -> ChatResponse:
    """
    Chat with the AI assistant
    
    Args:
        request: ChatRequest object containing the user message
    Returns:
        ChatResponse object containing the AI response
    Raises:
        HTTPException: If there's an error processing the request
    """
    try:
        logger.info(f"Processing chat request: {request.message[:50]}...")
        ai_response = get_ai_response(request.message)
        return ChatResponse(response=ai_response)
    except Exception as e:
        logger.error(f"Error in chat endpoint: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/", response_model=Dict[str, str])
async def root() -> Dict[str, str]:
    """Root endpoint returning API status"""
    return {"message": "AI Chatbot API is running! Visit /docs for API documentation"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)