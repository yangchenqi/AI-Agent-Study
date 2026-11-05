import pandas as pd
df = pd.read_csv("data/employees.csv")  # 读取员工数据
print(df.groupby("department_id"))  # 按department_id分组，返回DataFrameGroupBy对象
print(df.groupby("department_id").groups)  # 查看每个分组的索引列表
# 90.0: [0, 1, 2] 表示索引 0、1、2 的三行都属于部门 90

# 通过get_group()方法获取分组。
print(df.groupby("department_id").get_group(50))  # 获取分组为50的数据

# 2）按列取值
print(df.groupby("department_id")["salary"].mean())  # 按department_id分组，取salary列

# 可以通过agg()或aggregate()进行更复杂的操作，如一次计算多个统计值
print(df.groupby("department_id")["salary"].agg(["min", "median", "max"]))

# 按department_id分组，统计job_id的种类数，commission_pct的平均值
print(df.groupby("department_id").agg({"job_id": "nunique", "commission_pct": "mean"}))

# 按department_id分组，统计job_id的种类数，commission_pct的平均值
print(
    df.groupby("department_id")
    .agg(
        {"job_id": "nunique", "commission_pct": "mean"},
    )
    .rename(
        columns={"job_id": "工种数", "commission_pct": "佣金比例平均值"},
    )
)

# ·····················································································
#分组转换
# transform()可以对每个分组进行转换操作，返回与原DataFrame相同索引的结果
print(
    df.groupby("department_id")["salary"].transform(lambda x: x - x.mean())
)

na_index = pd.Series(df.index.tolist()).sample(30)  # 随机挑选30条数据
df.loc[na_index, "salary"] = pd.NA  # 将这30条数据的salary设置为缺失值
print(df.groupby("department_id")["salary"].agg(["size", "count"]))  # 查看每组数据总数与非空数据数


# 分组过滤
# 过滤操作可以让我们按照分组的属性丢弃若干数据。
# 例如，我们可能只需要保留commission_pct不包含空值的分组的数据。
commission_pct_filter = df.groupby("department_id").filter(
    lambda x: x["commission_pct"].notnull().all()
)  # 按department_id分组，过滤掉commission_pct包含空值的分组
print(commission_pct_filter)
