import pandas as pd

def process_filtered_excel(debug_file_path, output_path):
    # 读取 filtered_debug.xlsx 文件
    df = pd.read_excel(debug_file_path, header=0)
    print("从 filtered_debug.xlsx 读取的数据：")
    print(df.head())

    # 确保数据至少有 4 列，且 pledge_ratio 列和 quarter 列存在
    if df.shape[1] < 4:
        raise ValueError("数据列数不足，检查数据文件")

    # 使用列号处理，索引2是 pledge_ratio，索引3是 quarter
    pledge_ratio_col = 2
    quarter_col = 3

    # 筛选出质押比例大于 30 的事件
    filtered_df = df[df.iloc[:, pledge_ratio_col] > 30.0].copy()
    print("质押比例 > 30 的数据：")
    print(filtered_df.head())

    # 按季度统计质押比例大于30的事件数量
    summary = (
        filtered_df.iloc[:, quarter_col]
        .value_counts()
        .reset_index()
        .rename(columns={"index": "quarter", quarter_col: "count"})
        .sort_values(by="quarter")
    )
    print("按季度统计质押比例大于30的事件数量：")
    print(summary)

    # 保存结果到 Excel 文件
    summary.to_excel(output_path, index=False)
    print(f"统计结果已保存到 {output_path}")


# 示例用法
if __name__ == "__main__":
    
    debug_file = "/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/filtered_debug.xlsx"  # 替换为 filtered_debug.xlsx 文件的路径
    output_file = "summary_output.xlsx"  # 替换为你希望保存的输出文件路径
    process_filtered_excel(debug_file, output_file)
    print('step2 done!')
