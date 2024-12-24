import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

def plot_and_save(data_path):
    """
    根据 .dta 数据绘制图表并保存。

    Args:
        data_path (str): .dta 文件路径。
    """
    try:
        # 设置中文字体
        rcParams['font.sans-serif'] = ['Songti SC']
        rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

        # 读取数据
        data = pd.read_stata(data_path)
        data['EndDate1'] = pd.to_datetime(data['EndDate1'])  # 确保日期格式
        data = data.sort_values(by='EndDate1')  # 按时间排序

        # 计算总质押股数
        data['sum_TotPledShares'] = data['sum_LockedShares'] + data['sum_TradableShares']

        # 去除异常值：根据 IQR 方法
        Q1 = data['sum_TotPledShares'].quantile(0.25)  # 第 25 百分位
        Q3 = data['sum_TotPledShares'].quantile(0.75)  # 第 75 百分位
        IQR = Q3 - Q1  # 四分位距
        lower_bound = Q1 - 1.5 * IQR  # 下限
        upper_bound = Q3 + 1.5 * IQR  # 上限

        # # 记录并过滤异常值
        # outliers = data[(data['sum_TotPledShares'] < lower_bound) | (data['sum_TotPledShares'] > upper_bound)]
        # print(f"检测到 {len(outliers)} 个异常值：\n", outliers[['EndDate1', 'sum_TotPledShares']])

        # data = data[(data['sum_TotPledShares'] >= lower_bound) & (data['sum_TotPledShares'] <= upper_bound)]



        # 创建绘图
        fig, ax1 = plt.subplots(figsize=(14, 8))

        # 堆叠柱状图
        x_positions = range(len(data))
        bar_width = 0.6
        ax1.bar(
            x_positions,
            data['sum_LockedShares'],
            label="限制股质押股数 LockedShares",
            color='blue',
            alpha=0.7,
        )
        ax1.bar(
            x_positions,
            data['sum_TradableShares'],
            bottom=data['sum_LockedShares'],
            label="流通股质押股数 TradableShares",
            color='orange',
            alpha=0.7,
        )

        # 设置左侧 y 轴
        ax1.set_ylabel("质押股数", fontsize=12)
        ax1.set_title("近年来质押股数变化及其组成部分", fontsize=16)
        ax1.grid(axis='y', linestyle='--', alpha=0.6)
        ax1.set_xlabel("时间", fontsize=12)

        # 限制 x 轴显示标签
        tick_positions = x_positions[::30]
        tick_labels = data['EndDate1'].dt.strftime('%Y-%m-%d').iloc[::30]
        ax1.set_xticks(tick_positions)
        ax1.set_xticklabels(tick_labels, rotation=45, fontsize=10)

        # 折线图：流通股/质押股的比率
        ax2 = ax1.twinx()  # 创建右侧 y 轴
        ax2.plot(
            x_positions,
            data['r'],
            color='green',
            linewidth=2,
            label="流通股/质押股比率",
        )
        ax2.set_ylabel("比率 (流通股/质押股)", fontsize=12)
        ax2.set_ylim(0, 1)  # 假设比率范围为 0 到 1

        # 图例
        lines_1, labels_1 = ax1.get_legend_handles_labels()
        lines_2, labels_2 = ax2.get_legend_handles_labels()
        ax1.legend(lines_1 + lines_2, labels_1 + labels_2, fontsize=12, loc='upper left')

        plt.tight_layout()

        # 保存图表
        plt.savefig("质押股数变化堆叠柱状图_含比率折线_r.png")
        plt.close()

        print("图表已成功保存为：质押股数变化堆叠柱状图_含比率折线_r.png")

    except Exception as e:
        print(f"绘制图表时出错：{e}")

# 示例用法
if __name__ == "__main__":
    data_path = "/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/data_full.dta"  # 替换为实际路径
    plot_and_save(data_path)
