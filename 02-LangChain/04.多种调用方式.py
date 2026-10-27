from asyncio import tasks
import os

import time

import asyncio

from langchain.chat_models import init_chat_model

from langchain_core.messages import SystemMessage,HumanMessage

# 1.获取大模型的实例
model = init_chat_model(
    model="qwen-plus", #模型名称
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.environ["DASHSCOPE_API_KEY"], #API秘钥
)

#  流式调用，返回的结果是一个可迭代对象，通过for循环遍历
# result = model.stream("你好，我是谁")
# for chunk in result:
#     print(chunk.content,end="") # 打印流式返回的结果，end=""表示不换行

messages = [
# 批次调用，返回的结果是一个列表，列表中的每个元素是一个消息对象
[
 {"role": "system", "content": "你是一位诗人"},
 {"role": "user", "content": "写一首关于春天的诗"},
],
[
 {"role": "system", "content": "你是一位诗人"},
 {"role": "user", "content": "写一首关于夏天的诗"},
],
[
 {"role": "system", "content": "你是一位诗人"},
 {"role": "user", "content": "写一首关于秋天的诗"},
 ],
]
# resp = model.batch(messages) # 批量调用,返回一个消息列表

# print(resp[0].content) # 打印第一个消息的内容



# 并行调用，返回的结果是一个列表，列表中的每个元素是一个消息对象
# start_time = time.time()

# resps = [model.invoke(messages) for messages in messagess]
# print(resps)
# end_time = time.time()
# print(f"Total time: {end_time - start_time}") #Total time: 17.35268759727478

async def async_invoke():
    tasks = [model.ainvoke(messages) for messages in messages]
    return await asyncio.gather(*tasks)

#异步调用
start_time = time.time()
resps = asyncio.run(async_invoke())
print(resps)

end_time = time.time()
print(f"Total time: {end_time - start_time}") #Total time: 6.678410053253174

