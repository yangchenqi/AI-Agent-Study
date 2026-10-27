import pandas as pd

df = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [20, 30, 40]},index=["aa", "bb", "cc"])

# index DataFrame的行索引
print("行索引",df.index)

# columns   DataFrame的列标签
print("列标签",df.columns)

# values    DataFrame的值
print("值",df.values)

# ndim  DataFrame的维度
print("维度",df.ndim) #(2)

# shape DataFrame的形状
print("形状",df.shape) #(3,3)

# size  DataFrame的元素个数
print("元素个数",df.size) #(9)

# dtypes    DataFrame的元素类型
print("元素类型",df.dtypes)

# T 行列转置
print("行列转置",df.T)

# loc[] 显式索引，按行列标签索引或切片 逗号前是行切片规则，后是列切片规则
print("显式索引按行切片",df.loc["aa":"cc"]) # 包含从aa到cc的所有行

print("显式索引按列切片",df.loc[:,["id","name"]]) # 包含id和name两列

# iloc[]    隐式索引，按行列位置索引或切片
print("隐式索引按行切片",df.iloc[0:1]) # 包含第0行
print("隐式索引按行列切片",df.iloc[0:3,2]) # 包含第0到第2行第2列的元素
print("----------")

# at[]  使用行列标签访问单个元素
print("使用行列标签访问单个元素",df.at["aa","name"]) # 访问第0行name列的元素

# iat[] 使用行列位置访问单个元素
print("使用行列位置访问单个元素",df.iat[0,1]) # 访问第0行第1列的元素