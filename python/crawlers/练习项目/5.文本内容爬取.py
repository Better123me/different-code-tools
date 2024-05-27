# -- coding:utf-8 --            #当出现中文识别不了的时候要特别注释这一行
import requests
import os
import re

if not os.path.exists("./poems"):
    os.mkdir("./poems")
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
poet = input("请输入你想要的诗人的名字:")
file_path = r"./poems/" + poet + ".txt"
with open(file_path, "wb") as fp:
    for i in range(1, 11):
        url = "https://so.gushiwen.cn/shiwens/default.aspx?page=" + str(i) + "&astr=" + poet
        page_text = requests.get(url=url, headers=headers).text
        ex_content = """<div class="contson" id=".*?>(.*?)</div>"""
        ex_name = """<a style="font-size:18px; line-height:22px; height:22px;".*?<b>(.*?)</b>"""
        poem_content_list = re.findall(ex_content, page_text, re.S)
        poem_name_list = re.findall(ex_name, page_text, re.S)
        cnt = 0
        for cur_poem in poem_content_list:
            poem_name = poem_name_list[cnt]
            cnt = cnt + 1
            cur_poem = re.sub("<br />", "\n", cur_poem)
            cur_poem = re.sub("[<p></p>]", "", cur_poem)
            print(poem_name, cur_poem)
            fp.write(bytes( '\n' + poem_name + '\n', encoding="utf8"))
            fp.write(bytes(cur_poem, encoding="utf8"))
            print("成功写入"+poem_name)

fp.close()