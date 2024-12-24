import pandas as pd

def read_and_display_dta(file_path, num_rows=5):
    """
    读取 .dta 格式文件，并展示前几行内容。

    Args:
        file_path (str): .dta 文件的路径。
        num_rows (int): 要显示的行数，默认为 5。

    Returns:
        None
    """
    try:
        # 读取 .dta 文件
        data = pd.read_stata(file_path)
        
        # 输出文件的基本信息
        print("数据集的基本信息：")
        print(data.info(), "\n")
        
        # 输出前几行数据
        print(f"数据集的前 {num_rows} 行：")
        print(data.head(num_rows))
    
    except Exception as e:
        print(f"读取 .dta 文件时出错：{e}")

# 示例用法
if __name__ == "__main__":
    # 替换为你的 .dta 文件路径
    file_path = "your_file_path.dta"  # 替换为实际路径
    read_and_display_dta(file_path)
