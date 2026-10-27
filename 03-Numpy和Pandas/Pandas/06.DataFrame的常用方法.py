import pandas as pd

df = pd.DataFrame(data={"id": [101, 102, 103,104,105,106,101], "name": ["张三", "李四", "王五","赵六","冯七","周八","张三"], "age": [10, 20, 30, 40, None, 60,10]},index=["aa", "bb", "cc", "dd", "ee", "ff","aa"])

# head()    查看前n行数据，默认5行
print("查看前2行数据",df.head(2))

# tail()    查看后n行数据，默认5行
print("查看后5行数据",df.tail())

# isin()    元素是否包含在参数集合中
print("元素是否包含在参数集合中",df.isin([103,106]))

# isna()    元素是否为缺失值
print("元素是否为缺失值",df.isna())

# sum() 求和
print("age列的和",df["age"].sum())

# mean()    平均值
print("age列的平均值",df["age"].mean())

# min() 最小值
print("age列的最小值",df["age"].min())

# max() 最大值
print("age列的最大值",df["age"].max())

# var() 方差
print("age列的方差",df["age"].var())

# std() 标准差
print("age列的标准差",df["age"].std())

# median()  中位数
print("age列的中位数",df["age"].median())

# mode()    众数
print("age列的众数",df["age"].mode())

# quantile()    指定位置的分位数，如quantile(0.5)
print("age列的0.5分位数",df["age"].quantile(0.5))

# describe()    常见统计信息
print("常见统计信息",df.describe())

# info()    基本信息
print("基本信息",df.info())

# value_counts()    每个元素的个数
print("每个元素的个数",df.value_counts())

# count()   非空元素的个数
print("非空元素的个数", df.count())

# drop_duplicates() 去重  duplicated()判断是否为重复行
print("判断age列是否为重复行",df.duplicated(subset="age"))

# sample()  随机采样
print("随机采样",df.sample())

# replace() 用指定值代替原有值
print("----------------")
print("用指定值代替原有值",df.replace(20,"haha"))

# equals()  判断两个DataFrame是否相同
df1 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
df2 = pd.DataFrame(data={"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [10, 20, 30]})
print(df1.equals(df2))

# cummax()  累计最大值
df3 = pd.DataFrame({'A': [2, 5, 3, 7, 4],'B': [1, 6, 2, 8, 3]})

# 按列  等价于axis=0 默认
print("按列累计最大值",df3.cummax(axis="index"))

# 按行  等价于axis=1
print("按行累计最大值",df3.cummax(axis="columns"))

# cummin()  累计最小值
print("累计最小值",df3.cummin())

# cumsum()  累计和
print("累计和",df3.cumsum())

# cumprod() 累计积
print("累计积",df3.cumprod())

# diff()    一阶差分
print("一阶差分",df3.diff())

# sort_index()  按行索引排序
print("按行索引排序",df.sort_index())

# sort_values() 按某列的值排序，可传入列表来按多列排序，并通过ascending参数设置升序或降序
print("按age列排序",df.sort_values(by="age"))

# nlargest()    返回某列最大的n条数据
print("age列最大的2条数据",df.nlargest(n=2,columns="age"))

# nsmallest()   返回某列最小的n条数据
print("age列最小的1条数据",df.nsmallest(n=1,columns="age"))

# 可以使用布尔索引从DataFrame中筛选满足某些条件的行。

df = pd.DataFrame(
 data={"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"]},

 columns=["name", "age"],

 index=[101, 104, 103, 102],
)

print(df["age"] > 25)

print(df[df["age"] > 25])