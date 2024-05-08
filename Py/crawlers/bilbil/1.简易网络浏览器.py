import requests as re
# 伪装UA
headers = {
    'User-Agent':"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
# 获取url
#       这里有一个需要谨慎的点，网址的url不是以.com结尾即可，而是需要对应修改
url2 = "https://www.baidu.com/s"

# 获取参数，封装到字典中
kw = input("输入关键词")
#       这里需要注意的地方是，字典参数对应不同网页需要改名，不同搜索引擎传参格式不一样
param = {
    'query':kw
}
# 网络爬取
response = re.get(url=url2, headers=headers, params=param)
response_txt = response.text
# 写html文件
file_name = "./htmlFiles/" + kw + ".html"
with open(file_name, "w", encoding='utf-8') as fp:
    fp.write(response_txt)
print("保存成功")
