# 有一些限制
# 1. 所有元素必须是相同的数据类型。
# 2. 大小固定，创建后不能改变。
# 3. 支持多维数组。形状必须是规则的，即每个维度的大小固定。
import numpy as np # 导入numpy
a = np.array([[1, 2, 3], [4, 5, 6]]) # 创建一个二维数组

print(a)

print("a.ndim", a.ndim) # 维度

print("a.shape", a.shape) # 形状 （2,3）二行三列

print("a.size", a.size) # 元素个数 6 总的个数

print("a.dtype", a.dtype) # 数据类型

print("a.itemsize", a.itemsize) # 每个元素字节数大小
