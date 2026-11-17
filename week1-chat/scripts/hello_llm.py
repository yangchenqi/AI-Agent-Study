import asyncio
from app.llm import chat, chat_stream
async def main():
    content, usage = await chat([{"role": "user", "content": "我是ycq"}])
    print(content)
    print(usage)
if __name__ == "__main__":
    asyncio.run(main())