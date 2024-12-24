import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['Songti SC']
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取Excel文件
excel_file = '/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/GuQuanZhiYa_puredata.xlsx'  # 修改为你的Excel文件路径
df = pd.read_excel(excel_file, header=None)  # 不考虑列名，直接读取

# 假设比例数据在第二列（索引为1），处理空值和"-"符号
data = df.iloc[:, 1]  # 取第二列

# 将空值或"-"替换为0
data = data.replace({'-': 0, np.nan: 0})

# 转换为数值类型，确保所有数据都是数值
data = pd.to_numeric(data, errors='coerce').fillna(0)

# 定义区间
bins = np.arange(0, 101, 10)  # 区间为 [0, 10, 20, ..., 100]


labels = [f'{i}-{i+10}' for i in bins[:-1]]

# 计算每个区间的样本个数
counts, _ = np.histogram(data, bins)

# 计算各区间占比
total_count = len(data)
proportions = counts / total_count * 100

# 绘制柱状图
fig, ax1 = plt.subplots(figsize=(10, 6))

# 去掉上和右的边框
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# 柱状图（样本个数），使用橙色
ax1.bar(labels, counts, color='orange', alpha=0.7, label='样本个数')

# 设置柱状图的Y轴
ax1.set_ylabel('样本个数', color='orange')
ax1.set_xlabel('比例区间')

# 创建第二个Y轴（用于占比折线图）
ax2 = ax1.twinx()

# 折线图（占比），使用粉色
ax2.plot(labels, proportions, color='red', marker='o', label='占比（%）', linewidth=2)

# 设置第二个Y轴
ax2.set_ylabel('占比（%）', color='red')

# 设置图形标题
plt.title('不同比例区间样本个数及占比')

# 显示图例
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 显示图形
plt.tight_layout()

plt.savefig('/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/plt3_doubel.png')  
