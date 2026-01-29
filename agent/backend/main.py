from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import run_agent, state  # import the global state from orchestrator
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Blismos Academy Agent")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def home():
     base_dir = os.path.dirname(os.path.abspath(__file__))
     index_path = os.path.join(base_dir, "frontend", "index.html")  
     with open(index_path, "r", encoding="utf-8") as f:
        return f.read()

# Chat endpoint
@app.post("/chat")
async def chat(req: ChatRequest):
    reply = await run_agent(req.message)
    return {"reply": reply}

# New endpoint to reset agent memory
@app.post("/reset_memory")
async def reset_memory():
    state.clear()  # Clear all memory in the AgentState
    return {"status": "memory_reset"}
