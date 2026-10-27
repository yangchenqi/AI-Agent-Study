import pandas as pd

import numpy as np
arrs = pd.Series([11,22,np.nan,None,44,22],index=['a','b','c','d','e','f'])
# head()    查看前n行数据，默认5行
print(arrs.head())

# tail()    查看后n行数据，默认5行
print(arrs.tail(3))

# isin()    判断数组中的每一个元素是否包含在参数集合中
print(arrs.isin([11]))

# isna()    元素是否为缺失值
print("元素是否为缺失值", arrs.isna())

# sum() 求和，会忽略 Series 中的缺失值
print(arrs.sum())

# mean()    平均值
print(arrs.mean())

# min() 最小值
print(arrs.min())

# max() 最大值
print(arrs.max())

# var() 方差
print(arrs.var())

# std() 标准差
print(arrs.std())

# median() 中位数
# 若数据集的元素个数为奇数，中位数就是排序后位于中间位置的数值。
# 若数据集的元素个数为偶数，中位数则是排序后中间两个数的平均值。
# 去除缺失值之后，arrs 就变成了 [11, 22, 44, 22]。
# 对 [11, 22, 44, 22] 进行排序，得到 [11, 22, 22, 44]
print("中位数", arrs.median())

# mode()    众数
print(arrs.mode())

# quantile()    指定位置的分位数，如quantile(0.5)
# 分位数：分位数是把一组数据按照从小到大的顺序排列后，分割成若干等份的数值点。
# 0.25 分位数就是将数据从小到大排序后，位于 25% 位置处的数值。
# 插值方法：当计算分位数时，若位置不是整数，就需要借助插值方法来确定分位数值。# "midpoint" 插值方法是指当分位数位置处于两个数据点之间时，取这两个数据点
# 平均值作为分位数值。
# 插值方法 "midpoint","linear" 等，"midpoint" 表示取中点，"linear" 表示线性插值。
# 这里我们使用 "midpoint" 插值方法来计算 0.25 分位数。
# 对于有 n个数据点的有序数据集，q分位数的位置 i可以通过公式 i=(n−1)q来计
# 算。这里 n=4，q=0.25，则 i=(4−1)×0.25=0.75。这意味着 0.25 分位数处于第一个# 数据点（值为 11）和第二个数据点（值为 22）之间。使用 "midpoint" 插值方法，
# 分位数值就是这两个数据点的平均值，即 (11+22)÷2=16.5
print(arrs.quantile(0.25, interpolation="midpoint"))

# describe()    常见统计信息
print(arrs.describe())

# value_counts()    每个元素的个数
print(arrs.value_counts())

# count()   非缺失值元素的个数
print(arrs.count())

print(len(arrs))

# drop_duplicates() 去重  这里可以看出，底层None也作为NaN处理
print(arrs.drop_duplicates())

# unique()  去重后的数组
print(arrs.unique())

# nunique() 去重后非缺失值元素元素个数
print(arrs.nunique())

# sample()  随机采样
print(arrs.sample())

# sort_index()  按索引排序
print(arrs.sort_index())

# sort_values() 按值排序,ascending=True表示升序，ascending=False表示降序
print(arrs.sort_values())
print(arrs.sort_values(ascending=False))

# replace() 用指定值代替原有值,表示将所有出现的22都替换为"haha"
print(arrs.replace(22,"haha"))

# to_frame()    将Series转换为DataFrame
print(arrs.to_frame())

# equals()  判断两个Series是否相同
arr1 = pd.Series([1,2,3])
arr2 = pd.Series([1,2,3])
print(arr1.equals(arr2))

# keys()    返回Series的索引对象
print(arrs.index)
print(arrs.keys())

# corr()    计算与另一个Series的相关系数
# arr1.corr(arr2)：由于 arr1 和 arr2 的值完全相同，它们之间是完全正相关的，因此相关系数为 1。
# arr1.corr(arr3)：arr1 的值是递增的，而 arr3 的值是递减的，它们之间是完全负相关的，所以相关系数为 -1。
# arr1.corr(arr4)：arr1 和 arr4 的值都是递增的，且变化趋势一致，它们之间是完全正相关的，相关系数为 1。
# arr5.corr(arr6)：arr5 和 arr6 的值之间没有明显的线性关系，它们的相关系数
# 为 0。
arr1 = pd.Series([1,2,3])
arr2 = pd.Series([1,2,3])
arr3 = pd.Series([3,2,1])
arr4 = pd.Series([6,7,8])
arr5 = pd.Series([1, -1, 1, -1])
arr6 = pd.Series([1, 1, -1, -1])
print(arr1.corr(arr2)) #1
print(arr1.corr(arr3)) #-1
print(arr1.corr(arr4)) #1
print(arr5.corr(arr6)) #0

# cov() 计算与另一个Series的协方差
# 协方差用于衡量两个变量的总体误差，其值的正负表示两个变量的变化方向关系：
# 正值表示同向变化，负值表示反向变化。
print(arr1.cov(arr3)) #-1

# hist()    绘制直方图
arr7 = pd.Series([3,2,1,1,1,2,2])

# 绘制直方图，需要安装 matplotlib 库
# 直方图（Histogram）是一种用于展示数据分布的统计图表，它通过将数据划分为
# 若干个连续的区间（ bins ），统计每个区间内数据的频数或频率，并用矩形条的
# 高度表示该区间的数值分布情况

# arr7.hist(bins=3)

# items()   获取索引名以及值
for i,v in arr7.items():
    print(i,v)

# 布尔索引
s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
bools = s > s.mean() # 将大于平均值的元素标记为 True
print(bools)
# a    False
# b     True
# c     True
# d    False
print(s[bools])
# b    3.5
# c    6.8
# dtype: float64

# Series与标量运算
# 标量会与每个元素进行计算。

s = pd.Series({"a": -1.2, "b": 3.5, "c": 6.8, "d": 2.9})
print(s * 10)

# Series与Series运算
# 会根据标签索引进行对位计算，索引没有匹配上的会用NaN填充。
s1 = pd.Series([1, 1, 1, 1])
s2 = pd.Series([2, 2, 2, 2], index=[1, 2, 3, 4])
print(s1 + s2)
# 0    NaN
# 1    3.0
# 2    3.0
# 3    3.0
# 4    NaN
# dtype: float64



