import os

from langchain.chat_models import init_chat_model 

from langchain_core.messages import SystemMessage,HumanMessage

# 1.获取大模型的实例
model = init_chat_model(
    model="qwen-plus", #模型名称
    model_provider="openai",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key=os.environ["DASHSCOPE_API_KEY"], #API秘钥
)

# 2.构造一个提示词模板或者提示词


# (1) 文本提示列表构建
# resp = llm.invoke("你好")

# (2) 消息提示列表构建
# messages = [
# SystemMessage("你是个诗人"),
# HumanMessage("写首关于春天的诗"),
# ]

# (3) 字典方式构建消息列表
messages = [    
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "今天周几"},
]

#3.调用model的invoke方法去获取模型的结果
result = model.invoke(messages)
print(result.content)
