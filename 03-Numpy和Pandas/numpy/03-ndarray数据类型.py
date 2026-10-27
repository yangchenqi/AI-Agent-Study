from email.mime import base

import numpy as np # 导入numpy
# 数据类型
arr = np.array([1, 2, 3]) # 创建一个包含整数的ndarray
print(arr)
print(arr.dtype) # 查看arr的元素类型
arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1)
print(arr1.dtype) # 查看arr1的元素类型
arr2 = np.array([0.2, 2.5, 4.8], dtype="i8")
print(arr2)
print(arr2.dtype) # 查看arr2的元素类型 int64
# astype
arr3 = arr2.astype(np.float64) # 将arr2的元素类型转换为float64
print(arr3)
print(arr3.dtype) # 查看arr3的元素类型