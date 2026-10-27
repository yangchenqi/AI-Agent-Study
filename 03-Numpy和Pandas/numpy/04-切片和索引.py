# 切片
import numpy as np
arr1 = np.array([1, 2, 3, 4, 5,6,7,8,9,10])
print(arr1[1:4])  # 切片，从索引1到索引3（不包括索引4）
print(arr1[:3])   # 切片，从开头到索引2（不包括索引3）
print(arr1[2:9:2])   # 切片，从索引2到索引8（不包括索引9），步长为2
print(arr1[:])    # 切片，整个数组

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]])
print(arr2[0:2, 0:1])  # 切片，取前两行，第一列
print(arr2[1:4, 1:3])  # 切片，取第2到第4行，第2到第3列
print(arr2[:, 1])      # 切片，取所有行的第二列

# 'D:\AI Agent开发\.venv\Scripts\Activate.ps1'
# python .\04-切片和索引.py