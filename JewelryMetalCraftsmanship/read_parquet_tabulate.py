import pandas as pd

# 使用绝对路径读取 Parquet 文件
# df_documents = pd.read_parquet('./output/documents.parquet')  # 替换为实际路径
# df_text_units = pd.read_parquet('./output/text_units.parquet')  # 替换为实际路径


# 显示documents.parquet文件的前5行
# print(df_documents.head(5))

from tabulate import tabulate

# 其中，headers='keys' 表示使用列名作为表头，tablefmt='pretty' 表示使用 pretty 格式化输出，showindex=False 表示不显示行索引，stralign='left' 表示左对齐，maxcolwidths=[20, 20, 20, 20, 20] 表示每列的最大宽度为20
# print(tabulate(df_documents[:1], headers='keys', tablefmt='pretty', showindex=False, stralign='left', maxcolwidths=[20, 20, 20, 20, 20]))

# new_df_documents = pd.read_parquet('./output/documents.parquet')  # 替换为实际路径
# 假设 df 是你的 DataFrame
# print(tabulate(new_df_documents[:1], headers='keys', tablefmt='pretty', showindex=False, stralign='left', maxcolwidths=[20, 20, 20, 20, 20]))


# 使用绝对路径读取 Parquet 文件
df_entities = pd.read_parquet('./output/entities.parquet')  # 替换为实际路径
df_relations = pd.read_parquet('./output/relationships.parquet')  # 替换为实际路径

print(tabulate(df_relations[:2], headers='keys', tablefmt='pretty', showindex=False, stralign='left', maxcolwidths=[20, 20, 20, 20, 20]))
