import numpy as np
arr1 = np.array([[1, 2 ], [ 9, 10]])
# 比较函数
# any 至少一个函数满足条件，就返回true
# all 所有元素都满足条件才返回true
print(np.any(arr1 > 5))
print(np.all(arr1 > 5))

#  排序函数
arr2 = np.array([[3, 6], [4, 2],[9,8]])
print(np.sort(arr2)) #不会创建新的对象
# [[3 6]
#  [2 4]
#  [8 9]]

# 按列排序
print(np.sort(arr2, axis=0)) #按列排序
# [[3 2]
#  [4 6]
#  [9 8]]
# 按行排序
print(np.sort(arr2, axis=1)) #按行排序
# [[3 6]
#  [2 4]
#  [8 9]]

# 去重函数
# np.unique()：计算唯一值并返回有序结果。
arr3 = np.random.randint(0, 5, (3, 3))# 生成一个3x3的随机整数数组，范围在0到4之间
print(arr3)
print(np.unique(arr3))