from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.chatbot_v1 import chatbot

app = FastAPI()
english_bot = chatbot()

class Question(BaseModel):
    question: str

@app.post('/ask')
async def ask(question: Question):
    response = english_bot.get_response(question.question)
    return {'response': str(response)}

