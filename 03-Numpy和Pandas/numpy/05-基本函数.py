import numpy as np
arr = np.array([[1.3, -2.6, 3.5, 4, 5],[4.7, 5.2, -1.1, 0, 3.3]])
print(np.abs(arr))  # 绝对值
floor = np.floor(arr)  # 向下取整
print(floor)
rint = np.rint(arr)  # 四舍五入
# 五成双舍入：当恰好是5，会看5前面的数字是奇数还是偶数，奇数舍入到偶数，偶数保持不变
print(rint)

arr2 =np.array([[1, np.nan, 9], [16, 25, np.nan]])
print(type(np.nan))  # <class 'float'>

# multiply是将两个数组对应元素相乘，返回一个新数组
arr3 = np.array([[1, 2, 3], [4, 5, 6]])
arr4 = np.array([[7, 8, 9], [10, 11, 12]])
multiply = np.multiply(arr3, arr4)
print(multiply)

# divide是将两个数组对应元素相除，返回一个新数组
divide = np.divide(arr3, arr4)
print(divide)

where = np.where(arr3 > 0, arr3, 0)  # 返回满足条件的元素的索引
print(where)

 