import pandas as pd
import numpy as np
# Series的apply方法调用的函数，参数接收的是Series中的一个元素
def func(item,p1):
    print("Processing item:", item *20 + p1)
    return item * 20 + p1

s = pd.Series([10, 20, 30])
s.apply(func, p1=5)

# DataFrame使用apply()
# DataFrame的apply方法调用的函数，参数接收的是DataFrame中的一个Series
def func(s):
    print("Processing series:", s.sum())
    return s.sum()

df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 50, 60]})
df.apply(func)
# Processing series: 60
# Processing series: 150

#默认axis=0，按行方向进行操作，对列进行统计；
#可以设置axis=1，按照列的方向进行操作，对行进行统计
df.apply(func, axis=1)
# Processing series: 50
# Processing series: 70
# Processing series: 90

# 向量化函数
def f(x, y):
    if y == 0:
        return np.nan
    return x / y

df = pd.DataFrame({"a": [10, 20, 30], "b": [40, 0, 60]})
f_vec = np.vectorize(f)
print(f_vec(df["a"], df["b"]))  # 使用向量化函数处理

