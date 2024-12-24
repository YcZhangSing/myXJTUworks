import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

def plot_summary(output_path):
    # 读取统计结果 Excel 文件
    summary_df = pd.read_excel(output_path)
    
    print("读取的统计结果：")
    print(summary_df.head())
    
    # 检查数据是否包含 'quarter' 和 'count' 列
    if "quarter" not in summary_df.columns or "count" not in summary_df.columns:
        raise ValueError("Excel 文件中缺少 'quarter' 或 'count' 列")

    # 绘制柱状图
    rcParams['font.sans-serif'] = ['Songti SC']  # 设置中文字体
    
    plt.figure(figsize=(10, 6))  # 设置图表大小
    plt.bar(summary_df['quarter'], summary_df['count'], color='orange')
    
    # 设置标题和标签
    plt.title("每个季度质押比例超过30%的事件数量", fontsize=14)
    plt.xlabel("季度", fontsize=12)
    plt.ylabel("事件数量", fontsize=12)
    
    # 设置 x 轴坐标每隔 5 个季度显示一次
    step = 5
    ticks = summary_df['quarter'][::step]  # 每5个季度取一次标签
    plt.xticks(ticks=ticks, rotation=45)
    
    # 移除右边和上边的边框
    ax = plt.gca()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # 显示图表
    plt.tight_layout()  # 自动调整布局
    plt.show()

# 示例用法
if __name__ == "__main__":
    output_file = "summary_output.xlsx"  # 替换为你生成的 summary_output.xlsx 文件路径
    plot_summary(output_file)
