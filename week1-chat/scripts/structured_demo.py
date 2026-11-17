import asyncio
import json
from app.llm import chat
from pydantic import BaseModel, ValidationError
# 结构化输出能正确解析成Person
class Person(BaseModel):
    name: str
    years: int
    skills: list[str]
TEXT = "张伟有 5 年 Python 和后端开发经验，熟悉 FastAPI、PostgreSQL 和 Docker。"
async def extract(text: str) -> Person:
    # 构建提示，要求从文本中抽取信息并返回 JSON
    prompt = f"""
从下面的文本中抽取信息，只返回 JSON，不要解释：
{{"name": "姓名", "years": 工作年限数字, "skills": ["技能1", "技能2"]}}
文本：{text}
"""
    # 尝试两次解析，若失败则重试一次，最终仍失败则抛出异常
    for attempt in range(2):
        # 调用 chat 获取模型输出
        content, _ = await chat([{"role": "user", "content": prompt}])
        # 去掉可能的代码块标记，确保只保留 JSON 内容
        content = content.strip().removeprefix("```json").removesuffix("```").strip()
        try:
            # 尝试将 JSON 内容解析为 Person 对象
            return Person.model_validate_json(content)
        except (ValidationError, json.JSONDecodeError):
            if attempt == 1:
                raise
    raise RuntimeError("unreachable")
async def main() -> None:
    person = await extract(TEXT)
    print(person)
    

if __name__ == "__main__":
    asyncio.run(main())