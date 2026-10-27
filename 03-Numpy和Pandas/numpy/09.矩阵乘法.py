
import numpy as np
# 通过*运算符和np.multiply()对两个数组相乘进行的是对位乘法而非矩阵乘法运算。

# arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# arr2 = np.array([[6, 5, 4], [3, 2, 1]])
# print(arr1 * arr2)
# print(np.multiply(arr1, arr2))

# 使用np.dot()、ndarray.dot()、@可以进行矩阵乘法运算。
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[6, 5], [4, 3], [2, 1]])

#对于矩阵乘法来说，要求第一个矩阵的列数等于第二个矩阵的行数
print(arr1)
print(arr2) 
print(arr1.shape, arr2.shape) #（2, 3） (3, 2)
# 矩阵乘法的结果是一个新的二维数组，其行数等于第一个矩阵的行数，列数等于第二个矩阵的列数
print(np.dot(arr1, arr2))
#[20,14]
#[56, 41]
# 20 = 1*6 + 2*4 + 3*2
# 14 = 1*5 + 2*3 + 3*1
# 56 = 4*6 + 5*4 + 6*2
# 41 = 4*5 + 5*3 + 6*1


print(arr1.dot(arr2))
print(arr1 @ arr2)

# # 一个二维数组跟一个大小合适的一维数组的矩阵点积运算之后将会得到一个一维数组
# arr3 = np.array([6, 5, 4])
# print(arr1 @ arr3)