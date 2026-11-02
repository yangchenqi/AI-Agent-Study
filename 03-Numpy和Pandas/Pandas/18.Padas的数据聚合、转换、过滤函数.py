import pandas as pd
df = pd.read_csv("data/employees.csv")  # 读取员工数据
print(df.groupby("department_id"))  # 按department_id分组，返回DataFrameGroupBy对象
print(df.groupby("department_id").groups)  # 查看每个分组的索引列表
# 90.0: [0, 1, 2] 表示索引 0、1、2 的三行都属于部门 90

# 通过get_group()方法获取分组。
print(df.groupby("department_id").get_group(50))  # 获取分组为50的数据

# 2）按列取值
print(df.groupby("department_id")["salary"].mean())  # 按department_id分组，取salary列
