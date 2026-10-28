import os
import pandas as pd

df_from_csv = pd.read_csv("data/weather.csv")
# 加载天气数据
print(df_from_csv)

#查看前五行
print(df_from_csv.head())

#加载一列数据
print(df_from_csv['date']) #得到的是series
print(type(df_from_csv['date'])) #查看类型，确认是series
print(df_from_csv[['date', 'temp_max']]) #得到的是DataFrame
print(type(df_from_csv[['date', 'temp_max']])) #查看类型，确认是DataFrame
# 获取行标签为1的数据
print(df_from_csv.loc[1])

# 获取行标签分别为1、10、100的数据
print(df_from_csv.loc[[1, 10, 100]])

# 获取行标签为0的数据
print(df_from_csv.iloc[0])

#获取行位置为最后一行的数据
print(df_from_csv.iloc[-1])

#获取行标签为1，列标签为precipitation的数据
print(df_from_csv.loc[1, 'precipitation'])

# 获取所有行，列标签为precipitation的数据
print(df_from_csv.loc[:, 'precipitation'])

# 获取所有行，列位置为3，5，最后一位的数据
print(df_from_csv.iloc[:, [3, 5, -1]])

# 获取前十行，列位置为2，3，4，5的数据
print(df_from_csv.iloc[:10, 2:6])

#分组聚合
# 将数据按月分组，并统计最大温度和最小温度的平均值
df_from_csv['month'] = pd.to_datetime(df_from_csv['date']).dt.to_period('M').astype(str)
print(df_from_csv.groupby('month')[['temp_max', 'temp_min']].mean())

# 统计每个月不同天气的种类数
print(df_from_csv.groupby("month")["weather"].nunique())

# print(df_from_csv.groupby('month')[['temp_max', 'temp_min']].plot())

# 获取最高温度前30名数据
print(df_from_csv.nlargest(30, 'temp_max'))

# 获取最高温度前30名中最低温度最小的前5名数据
print(df_from_csv.nlargest(30, 'temp_max').nsmallest(5, 'temp_min'))

# 找出每年的最高温度
df_from_csv['year'] = pd.to_datetime(df_from_csv['date']).dt.to_period('Y').astype(str)
df_sort = df_from_csv.sort_values(['year', 'temp_max'], ascending=[True, False])
print(df_sort.drop_duplicates('year'))
