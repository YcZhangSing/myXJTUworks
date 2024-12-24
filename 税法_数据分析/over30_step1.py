import pandas as pd

def process_excel(file_path, output_path):
    # 读取Excel文件
    df = pd.read_excel(file_path, header=None, names=["event_id", "date", "pledge_ratio"])
    print("原始数据：")
    print(df.head())

    # 如果 pledge_ratio 列为空值，用 0 替代
    df["pledge_ratio"] = df["pledge_ratio"].apply(lambda x: float(x) if not pd.isnull(x) else 0.0)

    # 筛选出质押比例大于30%的事件
    filtered_df = df[df["pledge_ratio"] > 30.0].copy()
    print("质押比例 > 30 的数据：")
    print(filtered_df.head())

    # 提取年份和季度
    def get_quarter(date_str):
        try:
            if pd.isnull(date_str) or not isinstance(date_str, str):
                return None
            year, month, _ = map(int, date_str.split("-"))
            quarter = (month - 1) // 3 + 1
            return f"{year}-Q{quarter}"
        except Exception as e:
            print(f"日期解析失败：{date_str}, 错误信息：{e}")
            return None

    # 添加季度列
    filtered_df["quarter"] = filtered_df["date"].apply(get_quarter)
    print("添加季度后的数据：")
    print(filtered_df.head())

    # 确保 `quarter` 列存在且无缺失值
    filtered_df = filtered_df[filtered_df["quarter"].notnull()].copy()
    print("过滤掉缺失季度的数据：")
    print(filtered_df.head())

    # 将 filtered_df 写入 Excel 文件进行调试
    debug_path = "filtered_debug.xlsx"
    filtered_df.to_excel(debug_path, index=False)
    print(f"调试文件已保存到 {debug_path}")


# 示例用法
if __name__ == "__main__":
    input_file = "/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/30_pure_data.xlsx"  # 替换为你的输入文件路径
    output_file = "output.xlsx"  # 替换为你的输出文件路径 没用
    process_excel(input_file, output_file)
