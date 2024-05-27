import requests
import re
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
# 创建一个存储图片的文件夹
if not os.path.exists("./pic"):
    os.mkdir("./pic")
url = "https://ibaotu.com/guanggao/"
page_txt = requests.get(url=url, headers=headers).text
ex = """(?<=<img class="scrollLoading"  data-url=").*?(?=" alt=.*?)"""
src_list = re.findall(ex, page_txt, re.S)
print(src_list)
for src_path in src_list:
    src_name = src_path.split("/")[-1] + '.jpg'
    src_url = "https:" + src_path
    src_path = "./pic/" + src_name
    src = requests.get(url=src_url, headers=headers).content

    with open(src_path, "wb") as fp:
        fp.write(src)
        print(src_name + "写入成功")


