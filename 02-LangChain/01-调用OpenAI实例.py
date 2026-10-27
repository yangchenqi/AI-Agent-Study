from openai import OpenAI # pip install openai
import dotenv #可以加载.env文件中的环境变量
import os
dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = "sk-xxxxx"
# 构造一个客户端
client = OpenAI()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b:free",
    messages=[{"role": "user", "content": "将'你好'翻译成英文"}]
)
print(completion.choices[0].message.content)
