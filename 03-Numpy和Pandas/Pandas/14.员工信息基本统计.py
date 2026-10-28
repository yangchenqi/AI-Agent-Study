import os
import pandas as pd

df_from_csv = pd.read_csv("data/employees.csv")
# 加载员工信息数据
print(df_from_csv)

# # 查看前5行
# df_from_csv.head()
# # 查看数据信息
# df_from_csv.info()
# # 查看统计信息
# df_from_csv.describe()
# # 查看数据形状
# df_from_csv.shape

print(df_from_csv.nsmallest(1, 'salary'))  # 获取薪资最小的员工信息
print(df_from_csv.loc[df_from_csv['salary'] == df_from_csv['salary'].min()])  # 获取薪资最小的员工信息
print(df_from_csv.sort_values('salary').head(1))  # 按薪资排序,从低到高

print(df_from_csv.nlargest(10, 'salary'))  # 获取薪资最大的员工信息
print(df_from_csv.sort_values('salary',ascending=False).head(10))  # 按薪资排序的前10名，从高到低

print(df_from_csv['department_id'].unique())  # 获取部门的唯一值

 # 获取每个部门的员工数量
print(df_from_csv.groupby('department_id')['employee_id'].value_counts())  # 获取每个部门的员工数量
print(df_from_csv['department_id'].value_counts())  # 获取每个部门的员工数量
print(df_from_csv.groupby('department_id')['employee_id'].count().rename("employee_count"))

# 获取每个部门的平均薪资
print(df_from_csv.groupby('department_id')['salary'].mean().head(1)) # 平均薪资最低的部门
print(df_from_csv.groupby("department_id")["salary"].mean().nlargest(1))  # 平均薪资最高的部门