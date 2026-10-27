
import pandas as pd
#将DataFrame导入到mysql
import pymysql
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
df = pd.DataFrame({"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"], "id": [101, 102, 103, 104]})

with pymysql.connect(host="localhost", user="root", password="123456") as conn:
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS test")

engine = create_engine(URL.create(
    "mysql+pymysql",
    username="root",
    password="123456",
    host="localhost",
    database="test",
))
df.to_sql("df", engine, if_exists="replace", index=False)
with engine.connect() as conn:
    rows = conn.execute(text("SELECT * FROM df")).fetchall()
    for row in rows:
        print(row)
engine.dispose()