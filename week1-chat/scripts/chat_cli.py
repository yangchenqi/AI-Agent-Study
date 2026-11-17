import asyncio
from app.llm import chat_stream
async def main():
    messages = [{"role": "system", "content": "我是ycq"}]
    print("输入 /exit 退出。")
    while True:
        # 提示用户输入内容
        user_input = input("你: ")
        if user_input.strip() == "/exit":
            break
        # 将用户输入添加到消息列表中
        messages.append({"role": "user", "content": user_input})
        parts = []
        # 调用 chat_stream 获取助手的回复并实时输出
        async for token in chat_stream(messages):
            # 实时输出助手的回复
            print(token, end="", flush=True)
            parts.append(token)
        print("助手: " + "".join(parts))
        # 将助手的回复添加到消息列表中
        messages.append({"role": "assistant", "content": "".join(parts)})
    
if __name__ == "__main__":
    asyncio.run(main())