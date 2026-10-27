from langchain_core.prompts import PromptTemplate
template = PromptTemplate(
    input_variables=["product"],
    template="Describe the product: {product}"
)

template2 = PromptTemplate.from_template(
    "XXXX: {product}"
)
PromptTemplate(
    input_variables=["product"],
    template=template2.template
 );

#具体调用：
# 通过format方法传入参数，返回一个字符串
# invoke方法传入参数，返回一个消息对象
print(template.format(product="LangChainlallala"))
print(template2.invoke({"product": "LangChain2"}))