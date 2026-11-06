import pandas as pd
df = pd.read_csv("../data/sleep.csv")
df["sleep_duration_category"] = pd.cut(df["sleep_duration"], bins=[0, 4, 6, 8, 10])
df["stress_level_category"] = pd.cut(df["stress_level"], bins=[0, 2, 4, 6, 8, 10] )
# print(df.pivot_table(index="sleep_duration_category", columns="occupation", values="sleep_quality", aggfunc="mean"))
print(df.pivot_table(values="sleep_quality", index=["sleep_duration_category", "stress_level_category"], aggfunc="mean"))
# 添加列维度
print(df.pivot_table(values="sleep_quality", index=["sleep_duration_category", "stress_level_category"], columns = ["occupation","gender"],aggfunc="mean"))