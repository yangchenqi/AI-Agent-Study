# ndArray的创建方式
# array和asarray的区别
# array会拷贝数据，会将输入的数据转换成ndarray
# 而asarray不会拷贝数据，如果输入已经是ndarray，则返回原数组。
from email.mime import base

import numpy as np # 导入numpy
data = [1, 2, 3]
print("id(data)",id(data)) # 查看data的内存地址
arr1 = np.array(data) # 使用array创建ndarray
print(arr1)
print(type(arr1)) # 查看arr1的类型
print(id(arr1)) # 查看arr1的内存地址

# 如果传递的参数已经是ndarray，asarray不会拷贝数据，而是返回原数组。
arr2 = np.asarray(arr1) # 使用asarray创建ndarray
print(arr2)
print(type(arr2)) # 查看arr2的类型
print(id(arr2)) # 查看arr2的内存地址

# zeros()、ones()、empty()与zeros_like()、ones_like()、empty_like()

# zeros()：返回给定形状和类型的新数组，用0填充。
n = np.zeros((2, 3)) # 创建一个2行3列的全零数组
print(n)
# ones()：返回给定形状和类型的新数组，用1填充。

# empty()：返回给定形状和类型的未初始化的新数组。

# full()：返回给定形状和类型的新数组，用指定的值填充。
n = np.full((5, 3), 7) # 创建一个2行3列的   全7数组
print(n)
np.full_like(n, 9) # 创建一个与n形状相同的全9数组
print(np.full_like(n, 9))

# arange()：返回一个有规律的数组，类似于Python内置的range()函数。
n = np.arange(0, 10, 2) # 创建一个从0到10，步长为2的数组
print(n)  # [0 2 4 6 8]

# linspace()：返回在指定间隔内均匀分布的数字。
n = np.linspace(0, 10, 5) # 创建一个从0到10，包含5个均匀分布的数组,包含终点10
print(n)  # [ 0.   2.5  5.   7.5 10.  ]
endpoint = False
n = np.linspace(0, 10, 5, endpoint=endpoint) # 创建一个从0到10，包含5个均匀分布的数组，不包含终点
print(n)  # [0.  2.  4.  6.  8.]

# 创建一个start为2，stop为10，包含5个均匀分布的对数刻度数组
n = np.logspace(start=2, stop=10, num=5,base =2) 
print(n)  # [   4.   16.   64.  256. 1024.]

# random
# rand()：生成[0, 1)之间均匀分布的随机数。
n = np.random.rand(2, 3) # 创建一个2行3列的随机数组
print(n)
# [[0.54043448 0.13737936 0.01717373]
#  [0.51312326 0.69282679 0.71509578]]

# randint()：生成指定范围内的随机整数。
n = np.random.randint(low=0, high=10, size=(2, 3)) # 创建一个2行3列的随机整数数组，范围[0, 10)
print(n)
# [[2 6 8]
#  [4 0 9]]

# uniform()：生成指定范围内均匀分布的随机数。
n = np.random.uniform(low=0.0, high=1.0, size=(2, 3)) # 创建一个2行3列的均匀分布随机数组
print(n)
# [[0.12345678 0.23456789 0.34567890]
#  [0.45678901 0.56789012 0.67890123]]

# randn()：生成标准正态分布（均值为0，方差为1）的随机数。
n = np.random.randn(2, 3) # 创建一个2行3列的标准正态分布随机数组
print(n)
# [[ 0.12345678 -0.23456789  0.34567890]
#  [-0.45678901  0.56789012 -0.67890123]]
 
#  matrix
m = np.matrix([[1, 2, 3], [4, 5, 6]]) # 创建一个2行3列的矩阵
print(m)
print(type(m)) # 查看m的类型
print(m.shape) # 查看m的形状
print(m.dtype) # 查看m的元素类型