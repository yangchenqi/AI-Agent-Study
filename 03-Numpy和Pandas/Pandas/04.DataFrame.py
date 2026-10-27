# DataFrame是Pandas 中的另一个核心数据结构，类似于一个二维的表格或数据库中的数据表。
# 它是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值），既有行索引也有列索引。

# DataFrame中的数据是以一个或多个二维块存放的（而不是列表、字典或别的一维数据结构）。
# 它可以被看做由Series组成的字典（共同用一个索引）。提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作，
# 广泛用于数据分析、清洗、转换、可视化等任务。

import pandas as pd

# 直接通过字典创建DataFrame
df = pd.DataFrame({"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [20, 30, 40]})
print(df)
# ids = pd.Series([101, 102, 103],name="id")
# names = pd.Series(["张三", "李四", "王五"], name="name")
# ages = pd.Series([20, 30, 40], name="age")
# df2 = pd.DataFrame({"id": ids, "name": names, "age": ages})
# print(df2)

# 通过字典创建时指定列的顺序和行索引
df3 = pd.DataFrame(
    {"id": [101, 102, 103], "name": ["张三", "李四", "王五"], "age": [20, 30, 40]},
    columns=["name", "age", "id"],
    index=["a", "b", "c"]
)
print(df3)
