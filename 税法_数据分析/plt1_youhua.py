import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

def plot_and_save(data_path):
    """
    根据 .dta 数据绘制优化后的折线图并保存。

    Args:
        data_path (str): .dta 文件路径。
    """
    try:
        # 设置中文字体（Songti SC）
        rcParams['font.sans-serif'] = ['Songti SC']
        rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

        # 读取数据
        data = pd.read_stata(data_path)

        # 确保日期列为 datetime 类型，并按时间升序排序
        data['EndDate1'] = pd.to_datetime(data['EndDate1'])
        data = data.sort_values(by='EndDate1').reset_index(drop=True)

        # 过滤质押比率低于0.025的数据
        data = data[data['ratio'] >= 0.025]

        if data.empty:
            print("所有数据的质押比率均低于0.025，无法绘制图表。")
            return

        # 准备绘图数据
        x_positions = range(len(data))

        # 绘制折线图
        plt.figure(figsize=(14, 8))
        plt.plot(
            x_positions,
            data['ratio'],
            color='orange',
            linewidth=1.5,
            label="质押比率",
        )

        # 数据点标记：每隔 5 个点标记一个点
        mark_every = 7
        plt.scatter(
            x_positions[::mark_every],
            data['ratio'].iloc[::mark_every],
            color='orange',
        )

        # 限制 x 轴显示标签，确保每个年份只显示一次
        unique_years = data['EndDate1'].dt.year.drop_duplicates().sort_values()
        tick_positions = [
            data[data['EndDate1'].dt.year == year].index[0] for year in unique_years
        ]
        tick_labels = unique_years
        plt.xticks(tick_positions, tick_labels, rotation=0, fontsize=10)

        # 去除上和右的边框
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # 添加标题和标签
        plt.title("近年来A股质押比率变化", fontsize=16)
        plt.xlabel("年份", fontsize=12)
        plt.ylabel("质押比率", fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.legend(fontsize=12)
        plt.tight_layout()

        # 保存图表
        plt.savefig("质押比率变化折线图_优化版.png")
        plt.close()

        print("图表已成功保存为：质押比率变化折线图_优化版.png")

    except Exception as e:
        print(f"绘制图表时出错：{e}")

# 示例用法
if __name__ == "__main__":
    data_path = "/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/ori_data.dta"  # 替换为实际路径
    plot_and_save(data_path)
