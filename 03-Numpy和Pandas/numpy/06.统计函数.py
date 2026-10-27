import numpy as np
arr = np.array([[1, 2 ], [ 9, 10]])
# mean
print(np.mean(arr))
# sum
print(np.sum(arr))
# min
print(np.min(arr))
# max
print(np.max(arr))
# std 所有元素的标准差
print(np.std(arr))
# var 所有元素的方差
print(np.var(arr))
# argmin 返回最小值的索引
print(np.argmin(arr))
# argmax 返回最大值的索引
print(np.argmax(arr))
# cumsum 返回元素的累积和
print(np.cumsum(arr))
# cumprod 返回元素的累积积
print(np.cumprod(arr))
