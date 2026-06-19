from fastapi import FastAPI
from agents.support_agent import answer

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Persona Support Agent Running"
    }

@app.post("/ask")
def ask(question: str):
    return answer(question)