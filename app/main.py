from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import root_agent
import uvicorn, uuid

app = FastAPI(title="Intent Classification Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

session_service = InMemorySessionService()
APP_NAME = "intent_agent"

class IntentRequest(BaseModel):
    text: str

class IntentResponse(BaseModel):
    intent_result: str

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/classify", response_model=IntentResponse)
async def classify(request: IntentRequest):
    session_id = str(uuid.uuid4())
    user_id = "cloud-run-user"

    await session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )

    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=request.text)]
    )

    result_text = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=user_message
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    result_text += part.text

    return IntentResponse(intent_result=result_text)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
