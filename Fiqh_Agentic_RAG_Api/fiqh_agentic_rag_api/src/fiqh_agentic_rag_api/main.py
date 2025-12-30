import os
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from crew import FiqhAgenticRagApi

load_dotenv()

app = FastAPI(
    title="Fiqh Agentic RAG API",
    version="1.0.0",
)

chat_sessions = {}

class QueryRequest(BaseModel):
    user_id: str = "default_user"
    question: str
    
class QueryResponse(BaseModel):
    answer: str
    
@app.post("/chat", response_model=QueryResponse)
def ask_question(request: QueryRequest):
    try:
        current_user_history = chat_sessions.get(request.user_id, "")
        history_context = "\n".join([f"{msg["role"]}: {msg["content"]}" for msg in current_user_history[-2:]])
        
        print(f"📩 Received Question ({request.user_id}): {request.question}")
        
        inputs = {
            'chat_history': str(history_context) if history_context else "New Conversation",
            'question': str(request.question).strip(),
        }
        
        result = FiqhAgenticRagApi().crew().kickoff(inputs=inputs)
        final_answer = str(result)
        
        if request.user_id not in chat_sessions:
            chat_sessions[request.user_id] = []
            
        chat_sessions[request.user_id].append({"role": "User", "content": request.question})
        chat_sessions[request.user_id].append({"role": "AI", "content": final_answer})
        
        return QueryResponse(answer=final_answer)
    
    except Exception as e:
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)
    