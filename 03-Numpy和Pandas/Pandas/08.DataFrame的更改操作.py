# 1.设置行索引
import pandas as pd

# 1.创建DataFrame时如果不指定行索引，pandas会自动添加从0开始的索引。
df = pd.DataFrame({"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"], "id": [101, 102, 103, 104]})
print(df)

# (1)通过set_index()设置行索引,
# inplace=True：这是一个布尔类型的参数。当设为 True 时，会直接在原 DataFrame上进行修改；
# 若设为 False（默认值），则会返回一个新的 DataFrame，原DataFrame 保持不变
df.set_index("id",inplace=True)
print(df)

# (2)通过reset_index()重置行索引
df.reset_index(inplace=True) # 重置索引
print(df)
# -----------------------------------------------

# 2修改行索引名和列名

# (1)通过rename()修改行索引名和列名
df.rename(index={0: "一", 1: "二", 2: "三", 3: "四"}, columns={"age": "年龄", "name": "姓名"}, inplace=True)
print(df)

# (2)将index和columns重新赋值
df.index = ["Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ"]
df.columns = ["編號","年齡", "名稱",]
print(df)

# -----------------------------------------------

# 3.添加列
# 通过 df[“列名”] 添加列。
df["phone"] = ["13333333333", "14444444444", "15555555555", "16666666666"]
print(df)

# 4.删除列
# (1)通过 df.drop(“列名”, axis=1) 删除，也可是删除行 axis=0
# df.drop("phone", axis=1, inplace=True) 
# print(df)

# (2)通过 del df[“列名”] 删除
# del df["phone"]
# print(df)

# 5.插入列
# 通过 insert(loc, column, value) 插入。该方法没有inplace参数，直接在原数据上修改。
df.insert(loc=len(df.columns), column="phone2", value= "12121212")
print(df)