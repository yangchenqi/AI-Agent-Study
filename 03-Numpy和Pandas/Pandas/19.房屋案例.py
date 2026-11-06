import pandas as pd
data = pd.read_csv("data/house_sales.csv")
print(data["price"].mean(skipna=True))

# 数据清洗 去掉为空的值
data.isnull().sum()
data = data.dropna()

Q1=data["price"].quantile(0.25)  # 使用 IQR（Inter - Quartile Range，四分位距）方法来检测和处理房价数据中的异常值
Q3=data["price"].quantile(0.75)  #有 75% 的数据小于这个值
IQR=Q3-Q1
# 过滤异常值:使用 IQR（Inter - Quartile Range，四分位距）方法来检测和处理房价数据中的异常值
lower_bound = Q1 - 1.5 * IQR #如果某个数据点小于这个下限，就可能被视为异常值
upper_bound = Q3 + 1.5 * IQR #如果某个数据点大于这个上限，就可能被视为异常值
data = data[(data["price"] >= lower_bound) & (data["price"] <= upper_bound)]

# 时间序列分析
data["date"] = pd.to_datetime(data["date"])  # 将日期列转换为日期时间类型
# 计算房屋的使用年限
data['age'] = data['date'].dt.year - data['yr_built']
# 创建新特征：是否翻新
data['is_update'] = data['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)

# 选择数值型列
numeric_data = data.select_dtypes(include=["number"]) # 选择数据中所有数值型列
# 计算描述性统计信息：均值、中位数、标准差等
description = numeric_data.describe(percentiles=[0.25, 0.5, 0.75])  # 计算 25%、50%、75 百分位数的描述性统计信息
print('数值型列的描述性统计：', description)
# 计算不同特征与房价的相关性
correlation = numeric_data.corr()["price"].sort_values(ascending=False)
print('各特征与房价的相关性：', correlation)
# 相关性从高到低排列，便于观察哪些特征与房价关系最密切
# 可以根据相关性选择特征进行建模或进一步分析

# 平均房价：各邮政编码区域内房屋的平均销售价格，用于对比不同区域的房价水平。
zipcode_data = data.groupby("zipcode").agg({
    "price": "mean",
    "sqft_living": "mean",
    "bedrooms": "mean"
})

zipcode_columns = ["avg_price","avg_sqft_living","avg_bedrooms"]
zipcode_data.columns = zipcode_columns
print('各邮政编码区域的平均房价、平均居住面积和平均卧室数：', zipcode_data)

update_data = data.groupby("is_update").agg({
    "price": "mean",
    "sqft_living": "mean",
    "bedrooms": "mean"
})
update_columns = ["avg_price","avg_sqft_living","avg_bedrooms"]
update_data.columns = update_columns
print('是否翻新的房屋的平均房价、平均居住面积和平均卧室数：', update_data)

# 按照房屋使用年限分组
data["age_group"] = pd.cut(data["age"], bins=5)  # 按照房屋使用年限分组
age_status = data.groupby("age_group").agg({
    "price": "mean",
    "sqft_living": "mean",
    "bedrooms": "mean"
})
age_columns = ["avg_price","avg_sqft_living","avg_bedrooms"]
age_status.columns = age_columns
print('各房屋使用年限分组的平均房价、平均居住面积和平均卧室数：', age_status)

avg_price =data.groupby(data["date"].dt.year)["price"].mean()  # 按年份计算平均房价
print('各年份的平均房价：', avg_price)

avg_isUpdate_price =data.groupby([data["date"].dt.year,"is_update"])["price"].mean()  # 按年份和是否翻新计算平均房价
print('各年份和是否翻新的平均房价：', avg_isUpdate_price)