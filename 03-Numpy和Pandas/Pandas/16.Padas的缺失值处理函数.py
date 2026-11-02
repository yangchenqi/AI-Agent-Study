# pandas使用浮点值NaN（Not a Number）表示缺失数据，使用NA（Not Available）表示缺失值。
# 可以通过isnull()、isna()或notnull()、notna()方法判断某个值是否为缺失值。
import os
import pandas as pd

df_from_csv = pd.read_csv("data/weather_withna.csv")
print(df_from_csv.tail(5)) # 打印最后5行数据，查看缺失值情况
#             date  precipitation  temp_max  temp_min  wind weather
# 1456  2015-12-27            NaN       NaN       NaN   NaN     NaN
# 1457  2015-12-28            NaN       NaN       NaN   NaN     NaN
# 1458  2015-12-29            NaN       NaN       NaN   NaN     NaN
# 1459  2015-12-30            NaN       NaN       NaN   NaN     NaN
# 1460  2015-12-31           20.6      12.2       5.0   3.8    rain

#可以通过keep_default_na参数设置是否将空白值设置为缺失值。
df = pd.read_csv("data/weather_withna.csv",keep_default_na=False)
print(df.tail(5))
#             date precipitation temp_max temp_min wind weather
# 1456  2015-12-27                                             
# 1457  2015-12-28                                             
# 1458  2015-12-29                                             
# 1459  2015-12-30                                             
# 1460  2015-12-31          20.6     12.2      5.0  3.8    rain

# 可通过na_values参数将指定值设置为缺失值
df = pd.read_csv("data/weather_withna.csv", na_values=["2015-12-27"])
print(df.tail(5))
#             date  precipitation  temp_max  temp_min  wind weather
# 1456         NaN            NaN       NaN       NaN   NaN     NaN
# 1457  2015-12-28            NaN       NaN       NaN   NaN     NaN
# 1458  2015-12-29            NaN       NaN       NaN   NaN     NaN
# 1459  2015-12-30            NaN       NaN       NaN   NaN     NaN
# 1460  2015-12-31           20.6      12.2       5.0   3.8    rain


# 查看缺失值
print(df.isnull())
print(df.isnull().sum())

# 填充缺失值
# 1.固定值填充
# 通过fillna()方法，传入值或字典进行填充。
df = pd.read_csv("data/weather_withna.csv")
print(df.fillna("缺失值").tail())  # 使用固定值填充

# 2）使用统计值填充
# 可以使用均值、中位数、众数等统计值进行填充
df = pd.read_csv("data/weather_withna.csv")
print(df.fillna(df.mean()).tail())  # 使用均值填充数值列

# 3）使用前后的有效值填充
# 通过ffill()或bfill()方法使用前面或后面的有效值填充
df = pd.read_csv("data/weather_withna.csv")
print(df.ffill().tail())  # 使用前面的有效值填充
print(df.bfill().tail())  # 使用后面的有效值填充
