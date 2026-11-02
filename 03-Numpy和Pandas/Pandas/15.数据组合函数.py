# concat连接（用于沿指定轴将多个对象连接在一起）
# 1）Series与Series连接
import os
import pandas as pd


s1 = pd.Series(["A", "B"], index=[1, 2])
s2 = pd.Series(["D", "E"], index=[4, 5])
s3 = pd.Series(["G", "H"], index=[7, 8])
print(pd.concat([s1, s2, s3]))  # 连接三个Series对象

# 按照列连接
print(pd.concat([s1, s2, s3], axis=1))  # 按列连接三个Series对象
#      0    1    2
# 1    A  NaN  NaN
# 2    B  NaN  NaN
# 4  NaN    D  NaN
# 5  NaN    E  NaN
# 7  NaN  NaN    G
# 8  NaN  NaN    H

# 2) DataFrame与Series连接
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
s1 = pd.Series(data=[7, 10], index=[1, 2], name="a")
print(pd.concat([df1, s1]))  # 将DataFrame与Series按行连接
#      a    b
# 1    1    4
# 2    2    5
# 1    7  NaN
# 2   10  NaN
print(pd.concat([df1, s1], axis=1))  # 将DataFrame与Series按列连接
#      a    b     a
# 1    1    4     7
# 2    2    5    10

# DataFrame与DataFrame连接
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])
print(pd.concat([df1, df2]))  # 将两个DataFrame按行连接
#      a    b
# 1    1    4
# 2    2    5
# 1    7   10
# 2    8   11

print(pd.concat([df1, df2], axis=1))  # 将两个DataFrame按列连接
#      a    b    a    b
# 1    1    4    7   10
# 2    2    5    8   11

# 4)重置索引
df = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"a": [7, 8], "b": [10, 11]}, index=[1, 2])
pd.concat([df1, df2], ignore_index=True)  # 重置索引
#      a    b
# 0    1    4
# 1    2    5
# 2    7   10
# 3    8   11

# 5）类似join的连接
# 默认的合并方式是对其他轴进行并集合并（join=outer），可以用join=inner实现其他轴上的交集合并。
df1 = pd.DataFrame(data={"a": [1, 2], "b": [4, 5]}, index=[1, 2])
df2 = pd.DataFrame(data={"b": [7, 8], "c": [10, 11]}, index=[2, 3])

pd.concat([df1, df2])
#      a  b     c
# 1  1.0  4   NaN
# 2  2.0  5   NaN
# 2  NaN  7  10.0
# 3  NaN  8  11.0

pd.concat([df1, df2], join="inner")
#    b
# 1  4
# 2  5
# 2  7
# 3  8

# ---------------------------------------------------------------------
#merge合并：通过一个或多个列将行连接。
# 1）数据连接的类型
# merge()实现了三种数据连接的类型：一对一、多对一和多对多。
df1 = pd.DataFrame(
    {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
print(df1)
print(df2)

print(pd.merge(df1, df2))  # 一对一合并
#   employee        group  hire_date
# 0      Bob   Accounting       2008
# 1     Jake  Engineering       2012
# 2     Lisa  Engineering       2004
# 3      Sue           HR       2014

# 2）多对一连接
# 在需要连接的两个列中，有一列的值有重复。通过多对一连接获得的结果将会保留重复值。

df1 = pd.DataFrame(
    {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"group": ["Accounting", "Engineering", "HR"], "supervisor": ["Carly", "Guido", "Steve"]})
print(pd.merge(df1,df2))

# （3）多对多连接
# 如果左右两个输入的共同列都包含重复值，那么合并的结果就是一种多对多连接。
df1 = pd.DataFrame(
    {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame(
    {
        "group": ["Accounting", "Accounting", "Engineering", "Engineering", "HR", "HR"],
        "skills": ["math", "spreadsheets", "coding", "linux", "spreadsheets", "organization"],
    }
)
# 多对多连接产生的是行的笛卡尔积。由于左边有2个Engineering，右边有2个Engineering，所以最终结果有4个Engineering。
print(pd.merge(df1,df2))
#   employee        group        skills
# 0      Bob   Accounting          math
# 1      Bob   Accounting  spreadsheets
# 2     Jake  Engineering        coding
# 3     Jake  Engineering         linux
# 4     Lisa  Engineering        coding
# 5     Lisa  Engineering         linux
# 6      Sue           HR  spreadsheets
# 7      Sue           HR  organization

# 2）设置合并的键与索引
# merge()会将两个输入的一个或多个共同列作为键进行合并。但由于两个输入要合并的列通常都不是同名的，因此merge()提供了一些参数处理这个问题。
# （1）通过on指定使用某个列连接，只能在有共同列名的时候使用
df1 = pd.DataFrame(
    {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2, on="employee")
print(df3)
#   employee        group  hire_date
# 0      Bob   Accounting       2008
# 1     Jake  Engineering       2012
# 2     Lisa  Engineering       2004
# 3      Sue           HR       2014

# （2）两对象列名不同，通过left_on和right_on分别指定列名
df1 = pd.DataFrame(
    {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "salary": [70000, 80000, 120000, 90000]})
df3 = pd.merge(df1, df2, left_on="employee", right_on="name")
print(df3)
# （3）通过left_index和right_index设置合并的索引
# 通过设置merge()中的left_index、right_index参数将索引设置为键来实现合并。
df1 = pd.DataFrame(
    {"employee": ["Bob", "Jake", "Lisa", "Sue"], "group": ["Accounting", "Engineering", "Engineering", "HR"]}
)
df2 = pd.DataFrame({"employee": ["Lisa", "Bob", "Jake", "Sue"], "hire_date": [2004, 2008, 2012, 2014]})
df1.set_index("employee", inplace=True)
df2.set_index("employee", inplace=True)
# 设置索引后，如果不指定关联列会报错，建议通过以下方式指定，on="employee"也可#以实现，
# 但是不同的解释器可能效果不一样，因为设置索引后，employee就不算是列了
df3 = pd.merge(df1, df2, left_index=True, right_index=True)
print(df3)
#           group  hire_date
# employee                  
# Bob   Accounting       2008
# Jake  Engineering       2012
# Lisa  Engineering       2004
# Sue           HR       2014

df1 = pd.DataFrame({
    'key': ['A', 'B', 'C'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['B', 'C', 'D'],
    'value2': [4, 5, 6]
})

# 合并两个 DataFrame，并处理列名冲突，如果通过on指定列，只是指定的df1。会用
# df1指定的列和df2的索引连接，会报错。除非df2.set_index指定索引。
print(df1.join(df2,lsuffix='_left',rsuffix='_right'))
#   key_left  value1 key_right  value2
# 0        A       1         B       4
# 1        B       2         C       5
# 2        C       3         D       6


# 3）设置数据连接的集合操作规则
# 当一个值出现在一列，却没有出现在另一列时，就需要考虑集合操作规则了。
df1 = pd.DataFrame({"name": ["Peter", "Paul", "Mary"], "food": ["fish", "beans", "bread"]}, columns=["name", "food"])
df2 = pd.DataFrame({"name": ["Mary", "Joseph"], "drink": ["wine", "beer"]}, columns=["name", "drink"])
print(pd.merge(df1,df2))
#    name   food drink
# 0  Mary  bread  wine
# 合并两个数据集，在name列中只有一个共同的值Mary。默认情况下，结果中只会包含两个输入集合的交集，这种连接方式被称为内连接（inner join）。

# 我们可以通过how参数设置连接方式，默认值为inner。how参数支持的数据连接方式还有outer、left和right。外连接（outer join）返回两个输入列的并集，所有缺失值都用 NaN 填充。
print(pd.merge(df1, df2, how="outer"))
#      name   food drink
# 0  Joseph    NaN  beer
# 1    Mary  bread  wine
# 2    Paul  beans   NaN
# 3   Peter   fish   NaN

# 左连接（left join）返回左侧输入集合的所有值，以及右侧输入集合中与之匹配的值，缺失值用 NaN 填充。
print(pd.merge(df1, df2, how="left"))
#     name   food drink
# 0  Peter   fish   NaN
# 1   Paul  beans   NaN
# 2   Mary  bread  wine
# 右连接（right join）返回右侧输入集合的所有值，以及左侧输入集合中与之匹配的值，缺失值用 NaN 填充。
print(pd.merge(df1, df2, how="right"))
#     name   food drink
# 0  Mary  bread  wine
# 1  Joseph    NaN  beer
# 通过设置how参数，我们可以灵活地控制合并的方式，根据实际需求选择内连接、外连接、左连接或右连接。

# 4）重复列名的处理
# 可能会遇到两个输入DataFrame有重名列的情况，merge()会自动为其增加后缀_x和_y，也可以通过suffixes参数自定义后缀名。
df1 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [1, 2, 3, 4]})
df2 = pd.DataFrame({"name": ["Bob", "Jake", "Lisa", "Sue"], "rank": [3, 1, 4, 2]})
print(pd.merge(df1, df2, on="name")) # 不指定后缀名，默认为_x和_y
print(pd.merge(df1, df2, on="name", suffixes=('_left', '_right'))) # 自定义后缀名
 
