import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 设置中文字体
rcParams['font.sans-serif'] = ['Songti SC']
rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 读取Excel文件
excel_file = '/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/行业_puredata.xlsx'  # 请替换为实际的Excel文件路径
df = pd.read_excel(excel_file, header=None)  # 无表头，直接读取数据

# 获取比例和行业名称数据
ratios = df.iloc[:, 0]  # 第一列为比例
industries = df.iloc[:, 1]  # 第二列为行业名称

# 将比例列中的非数字值（如空值、'-'、'--'等）转换为0
ratios = pd.to_numeric(ratios, errors='coerce').fillna(0)  # 非数字值转为NaN，再填充为0

# 统计超过30%的记录个数
industry_counts = industries[ratios > 0.3].value_counts()

# 保留前30个行业
industry_counts_top30 = industry_counts.head(30)

# 绘制柱状图
plt.figure(figsize=(14, 8))  # 扩大画布，调整图表大小
industry_counts_top30.plot(kind='bar', color='orange')  # 使用纯橙色

# 去掉上边框和右边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# 设置标题和标签
plt.title('行业类型超过30%的记录个数')
plt.xlabel('行业名称')
plt.ylabel('记录个数')

# 将X轴标签旋转90度，避免重叠
plt.xticks(rotation=90)

# 显示图表
plt.tight_layout()
plt.savefig('/Users/zhangyuchen/Desktop/MyGitRepos/myXJTUworks/税法_数据分析/行业类型超过30%的记录个数.png')
