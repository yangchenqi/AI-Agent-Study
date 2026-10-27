import os
import pandas as pd
os.makedirs("data", exist_ok=True) #创建data文件夹用于存放数据文件

df = pd.DataFrame({"age": [20, 30, 40, 10], "name": ["张三", "李四", "王五", "赵六"], "id": [101, 102, 103, 104]})

# df.set_index("id", inplace=True)
# df.to_csv("data/df.csv") # 将DataFrame导出为CSV文件

# 从CSV文件导入DataFrame
df_from_csv = pd.read_csv("data/df.csv", index_col="id")
print(df_from_csv)

# 将DataFrame导出为JSON文件, orient="records"表示每一行数据作为一个独立的JSON对象
df.to_json("data/df.json", orient="records")

# # 将DataFrame导出到剪贴板
df.to_clipboard()
# 	age	name	id
# 0	20	张三	101
# 1	30	李四	102
# 2	40	王五	103
# 3	10	赵六	104
