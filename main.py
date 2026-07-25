from fastapi import FastAPI, HTTPException

from models import ChatRequest
from services import get_ai_response
from utils import get_timestamp

app = FastAPI(title="ICEBEAR Chat API")


@app.get("/")
def home():
    return {"message": "Welcome to ICEBEAR Chat API"}


@app.post("/chat")
def chat(request: ChatRequest):

    if request.message.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Message cannot be empty."
        )

    reply = get_ai_response(request.message)

    return {
        "reply": reply,
        "time": get_timestamp()
    }