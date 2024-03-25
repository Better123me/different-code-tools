import re 
import pandas as pd

# 读取原始 Excel 表格
data = pd.read_excel("b站心理健康主题视频信息.xlsx")

# 提取需要清理的列数据，并进行清理
column_to_clean = data.iloc[:, 4].tolist()
rstr = "<[^>]+>"
cleaned_column = []
for content in column_to_clean:
    cleaned_content = re.sub(rstr, '', str(content))
    cleaned_column.append(cleaned_content)

# 将清理后的数据替换回原 DataFrame 中相应的列
data.iloc[:, 4] = cleaned_column

# 保存修改后的 DataFrame 回原 Excel 表格
data.to_excel("b站心理健康主题视频信息_cleaned.xlsx", index=False)