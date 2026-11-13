# import asyncio

# from openai import AsyncOpenAI

# from app.llm import chat, chat_stream
# async def main():
#     content, usage = await chat([{"role": "user", "content": "用一句话介绍你自己。"}])
#     print(content)
#     print(usage)

# if __name__ == "__main__":
#     asyncio.run(main())


 

import asyncio
from app.llm import chat, chat_stream
async def main():
    content, usage = await chat([{"role": "user", "content": "翻译你好"}])
    print(content)
    print(usage)
if __name__ == '__main__':
    asyncio.run(main())