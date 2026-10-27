# Series 是 Pandas 中的一个核心数据结构，类似于一个一维的数组，具有数据和索引。

# Series 可以存储任何数据类型（整数、浮点数、字符串等），
# 并通过标签（索引）来访问元素。Series 的数据结构是非常有用的，
# 因为它可以处理各种数据类型，同时保持了高效的数据操作能力，
# 比如可以通过标签来快速访问和操作数据。

# Series 特点：

# 一维数组：Series 中的每个元素都有一个对应的索引值。
# 索引： 每个数据元素都可以通过标签（索引）来访问，默认情况下索引是从 0 开始的整数，但你也可以自定义索引。
# 数据类型： Series 可以容纳不同数据类型的元素，包括整数、浮点数、字符串、Python 对象等。
# 大小不变性：Series 的大小在创建后是不变的，但可以通过某些操作（如 append 或 delete）来改变。
# 操作：Series 支持各种操作，如数学运算、统计分析、字符串处理等。
# 缺失数据：Series 可以包含缺失数据，Pandas 使用NaN（Not a Number）来表示缺失或无值。
# 自动对齐：当对多个 Series 进行运算时，Pandas 会自动根据索引对齐数据，这使得数据处理更加高效。

# 示例：
import pandas as pd
# 直接通过列表创建Series
s = pd.Series([1, 2, 3])
print(s)
# 通过列表创建Series时指定索引
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# 通过列表创建Series时指定索引和名称
s2 = pd.Series([1, 2, 3], index=['a', 'b', 'c'], name='example')

#  直接通过字典创建Series
dic = {"a": 4, "b": 7, "c": -5, "d": 3}
s3 = pd.Series(dic)

print(s)
print(s1)
print(s2)
print(s3)
