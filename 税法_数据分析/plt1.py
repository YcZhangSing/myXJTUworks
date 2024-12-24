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
        # 确保日期列为 datetime 类型
        data['EndDate1'] = pd.to_datetime(data['EndDate1'])
        
        # 对 ratio 数据进行平滑处理（移动平均，窗口大小为5）
        data['ratio_smooth'] = data['ratio'].rolling(window=5, min_periods=1).mean()
        
        # # 对数据降采样（每隔10个点显示一个）
        # sampled_data = data.iloc[::5, :]

        # 图 1：ratio 和 EndDate1 的折线图（平滑 + 降采样）
        plt.figure(figsize=(10, 6))
        plt.plot(data['EndDate1'], data['ratio_smooth'], marker='', label="质押比率（平滑）", alpha=0.7)
        plt.scatter(data['EndDate1'], data['ratio_smooth'], color='red', label="采样点", s=10)
        plt.title("近年来A股质押规模变化", fontsize=14)
        plt.xlabel("时间", fontsize=12)
        plt.ylabel("质押比率", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        plt.savefig("质押比率变化折线图_优化版.png")
        plt.close()


        print("图表已成功保存为：")
        print("质押比率变化折线图0.png")


    except Exception as e:
        print(f"绘制图表时出错：{e}")

# 示例用法
if __name__ == "__main__":
    data_path = "/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/ori_data.dta"  # 替换为实际路径
    plot_and_save(data_path)
