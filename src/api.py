import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException

load_dotenv()
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

from agents.chat_manager import ChatManager

# Initialize the FastAPI app and ChatManager
app = FastAPI()
allowed_origins = os.getenv("CORS_ALLOW_ORIGINS", "*")
origins = [o.strip() for o in allowed_origins.split(",") if o.strip()]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins if origins else ["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)
chat_manager = ChatManager()

# --- Health ---
@app.get("/health")
def health():
  return {"status": "ok"}

# --- Pydantic Models ---
class ChatMessage(BaseModel):
    message: str

class NewChatRequest(BaseModel):
    name: str | None = None

# --- API Endpoints ---

@app.get("/contexts")
def list_contexts(current_context_id: int | None = None):
    """List all available chat contexts."""
    return chat_manager.list_contexts(current_context_id)

@app.post("/contexts")
def create_new_context(request: NewChatRequest):
    """Create a new chat context and return its details."""
    new_context = chat_manager.create_new_context(name=request.name)
    context_id = chat_manager.save_context(new_context)
    # It's good practice to return the full created object, including its new ID
    created_context = chat_manager.load_context(context_id)
    return created_context

@app.get("/contexts/{context_id}")
def get_context(context_id: int):
    """Get the details of a specific chat context."""
    ctx = chat_manager.load_context(context_id)
    if ctx is None:
        raise HTTPException(status_code=404, detail="Context not found")
    return ctx

@app.post("/contexts/{context_id}/chat")
async def chat(context_id: int, message: ChatMessage):
    """
    Send a message to a chat context and get a streaming response of the conversation.
    """
    async def stream_generator():
        for conversation_history in chat_manager.chat(context_id, message.message):
            yield f"data: {json.dumps(conversation_history)}\n\n"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")

@app.get("/contexts/{context_id}/draft")
async def draft_document(context_id: int):
    """
    Draft a document from a chat context and get a streaming response.
    """
    async def stream_generator():
        for chunk in chat_manager.draft(context_id):
            yield f"data: {json.dumps({'content': chunk})}\n\n"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")
