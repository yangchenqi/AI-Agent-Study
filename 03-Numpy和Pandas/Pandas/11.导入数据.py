import os
import pandas as pd
import pymysql
conn = pymysql.connect(host="localhost", user="root", password="123456", database="test")

df_from_csv = pd.read_csv("data/df.csv", index_col="id")
print(df_from_csv)

df_from_json = pd.read_json("data/df.json", orient="records")
print(df_from_json)

df_from_sql = pd.read_sql("SELECT * FROM df", conn)
print(df_from_sql)