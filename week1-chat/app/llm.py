from app.config import settings
from openai import AsyncOpenAI

open_api_key = settings.openai_api_key
open_base_url = settings.openai_base_url
model_name = settings.model_name
client = AsyncOpenAI(api_key=open_api_key, base_url=open_base_url)

async def chat(messages: list[dict]):
    response = await client.chat.completions.create(
        model=model_name,
        messages=messages
    )
    return response.choices[0].message.content, response.usage

async def chat_stream(messages: list[dict]):
    completion  = await client.chat.completions.create(
        model=model_name,
        messages=messages,
        stream=True
    )
    async for chunk in completion:
        if not chunk.choices or not chunk.choices[0].delta:
            continue
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta