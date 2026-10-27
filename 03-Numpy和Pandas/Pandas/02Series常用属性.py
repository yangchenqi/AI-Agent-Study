import pandas as pd

# 创建一个Series
s = pd.Series([1, 2, 3], index=['a', 'b', 'c'], name='example')

# 常用属性
print("索引:", s.index)
print("值:", s.values)
print("名称:", s.name)
print("数据类型:", s.dtype)
print("大小:", s.size)
print("维度:", s.ndim)
print("内存占用字节数:", s.nbytes)
print("按标签访问元素:", s.loc['a'])
print("按标签快速访问元素:", s.at['a'])
print("隐式索引，按位置访问元素:", s.iloc[0])
print("按位置快速访问元素:", s.iat[0])