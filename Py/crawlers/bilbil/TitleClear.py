import re as r
import pandas as pd

data = pd.read_excel("b站抗日主题视频信息.xlsx").iloc[:, 4].tolist()
rstr = "(<.*?>)"
i = 0
for content in data:
    data[i] = r.replace(rstr, '')
    i+=1

print(data)