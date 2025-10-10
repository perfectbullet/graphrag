import pyarrow.parquet as pq
import pandas as pd
import os
from typing import Optional

# 设置pandas显示选项，避免省略号
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.width', None)  # 不限制显示宽度
pd.set_option('display.max_colwidth', 100)  # 不限制列宽
pd.set_option('display.expand_frame_repr', False)  # 不换行显示


def read_parquet_head(file_path: str, n: int = 5) -> Optional[pd.DataFrame]:
    """
    读取Parquet文件并返回前n行数据

    Args:
        file_path (str): Parquet文件路径
        n (int): 要读取的行数，默认为5

    Returns:
        Optional[pd.DataFrame]: 前n行数据的DataFrame，如果出错则返回None
    """
    try:
        # 检查文件是否存在
        if not os.path.exists(file_path):
            print(f"错误：文件 {file_path} 不存在")
            return None

        # 读取Parquet文件
        parquet_file = pq.ParquetFile(file_path)
        data = parquet_file.read().to_pandas()

        # 返回前n行
        return data.head(n)

    except Exception as e:
        print(f"读取文件时出错：{e}")
        return None


def print_parquet_head(file_path: str, n: int = 5, full_display: bool = True) -> None:
    """
    读取并打印Parquet文件的前n行数据

    Args:
        file_path (str): Parquet文件路径
        n (int): 要打印的行数，默认为5
        full_display (bool): 是否完整显示数据（不省略），默认为True
    """
    data = read_parquet_head(file_path, n)

    if data is not None:
        print(f"文件：{file_path}")
        print(f"数据形状：{data.shape}")
        print(f"前 {n} 行数据：")
        print("-" * 50)

        if full_display:
            # 临时设置显示选项确保完整显示
            with pd.option_context('display.max_columns', None,
                                   'display.max_rows', None,
                                   'display.width', None,
                                   'display.max_colwidth', 100,
                                   'display.expand_frame_repr', False):
                print(data)
        else:
            print(data)

        print("-" * 50)
        print(f"列名：{list(data.columns)}")
        print(f"数据类型：")
        print(data.dtypes)
    else:
        print("无法读取文件数据")


def print_parquet_full(file_path: str, n: int = 5) -> None:
    """
    完整显示Parquet文件数据（包括长文本内容）

    Args:
        file_path (str): Parquet文件路径
        n (int): 要打印的行数，默认为5
    """
    data = read_parquet_head(file_path, n)

    if data is not None:
        print(f"文件：{file_path}")
        print(f"数据形状：{data.shape}")
        print("-" * 80)

        # 逐行显示，确保长文本完整显示
        for idx, row in data.iterrows():
            print(f"第 {idx + 1} 行：")
            for col in data.columns:
                content = str(row[col])
                print(f"  {col}: {content[:300]}{'...' if len(content) > 300 else ''}")  # 显示前 300 字符
            print("-" * 40)
    else:
        print("无法读取文件数据")


def get_parquet_info(file_path: str) -> None:
    """
    获取Parquet文件的基本信息

    Args:
        file_path (str): Parquet文件路径
    """
    try:
        if not os.path.exists(file_path):
            print(f"错误：文件 {file_path} 不存在")
            return

        parquet_file = pq.ParquetFile(file_path)

        print(f"文件信息：{file_path}")
        print(f"行数：{parquet_file.metadata.num_rows}")
        print(f"列数：{parquet_file.metadata.num_columns}")
        print(f"文件大小：{os.path.getsize(file_path)} 字节")
        print(f"Schema：")
        print(parquet_file.schema)

    except Exception as e:
        print(f"获取文件信息时出错：{e}")


def reset_display_options() -> None:
    """
    重置pandas显示选项为默认值
    """
    pd.reset_option('display.max_columns')
    pd.reset_option('display.max_rows')
    pd.reset_option('display.width')
    pd.reset_option('display.max_colwidth')
    pd.reset_option('display.expand_frame_repr')


if __name__ == '__main__':
    parquet_file_path = './output/relationships.parquet'

    # 方式1：只读取数据并完整显示
    # data = read_parquet_head(parquet_file_path, n=5)
    # if data is not None:
    #     print("=== 基本显示 ===")
    #     print(data)

    # print("\n" + "=" * 60 + "\n")

    # 方式2：读取并打印详细信息（完整显示）
    print("=== 详细信息显示 ===")
    print_parquet_head(parquet_file_path, n=10, full_display=True)

    print("\n" + "=" * 60 + "\n")

    # 方式3：逐行完整显示（适合长文本内容）
    print("=== 逐行完整显示 ===")
    print_parquet_full(parquet_file_path, n=10)

    print("\n" + "=" * 60 + "\n")

    # 方式4：查看文件基本信息
    # print("=== 文件信息 ===")
    # get_parquet_info(parquet_file_path)
