from fastapi import FastAPI
from pydantic import BaseModel, Field
from app.llm import chat, chat_stream
from sse_starlette.sse import EventSourceResponse


app = FastAPI()

class Chat_request(BaseModel):
    message: str=Field()

class Chat_response(BaseModel):
    reply: str

@app.post("/chat",response_model=Chat_response)
async def chat_endpoint(request: Chat_request) -> Chat_response:
    reply, _ = await chat([{"role":"user", "content": request.message}])
    return Chat_response(reply=reply)


@app.post("/chat_stream",response_model=Chat_response)
async def chat_stream_endpoint(request:Chat_request):
    async def generate():
        async for chunk in chat_stream([{"role":"user", "content": request.message}]):
            yield {"data":chunk}
        yield {"data":"[DONE]"}
    return EventSourceResponse(generate())