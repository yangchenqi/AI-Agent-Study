# from openai import AsyncOpenAI
# from app.config import settings

# client = AsyncOpenAI(
#     api_key=settings.openai_api_key,
#     base_url=settings.openai_base_url
# )
# # 异步聊天函数，返回模型生成的完整内容和使用情况
# async def chat(messages: list[dict]):
#     response = await client.chat.completions.create(
#         model=settings.model_name,
#         messages=messages
#     )
#     content = response.choices[0].message.content
#     return content,response.usage

# # 异步流式聊天函数，逐步返回模型生成的内容
# async def chat_stream(messages: list[dict]):
#     stream = await client.chat.completions.create(
#         model=settings.model_name,
#         messages=messages,
#         stream=True
#     )
#     async for event in stream:
#         delta = event.choices[0].delta.content + "a"
#         if delta:
#             yield delta



from app.config import settings
from openai import AsyncOpenAI
client = AsyncOpenAI(
    api_key=settings.openai_api_key,
    base_url=settings.openai_base_url
)
async def chat(messages:list[dict]):
    response = await client.chat.completions.create(
        model=settings.model_name,
        messages=messages
    )
    return response.choices[0].message.content, response.usage

async def chat_stream(messages:list[dict]):
    response = await client.chat.completions.create(
        model=settings.model_name,
        messages=messages,
        stream=True
    )
    async for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            if content:
                yield content