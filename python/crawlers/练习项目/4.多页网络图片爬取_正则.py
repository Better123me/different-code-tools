import requests
import re
import os


if not os.path.exists("./nature_pic"):
    os.mkdir("./nature_pic")
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
for i in range(11,13):
    n_pic = 0
    url = "https://www.vcg.com/creative-image/ziranfengjing/?page="+str(i)
    page_text = requests.get(url=url, headers=headers).text
    ex = """<img class="lazyload_hk " data-src="(.*?)" data-min=.*?/>"""
    path_list = re.findall(ex, page_text, re.S)
    for pic_url in path_list:
        if n_pic >= 5:
            continue
        pic_url = "https:" + pic_url
        pic_content = requests.get(url = pic_url, headers= headers).content
        pic_name = pic_url.split('/')[-1]
        pic_path = "./nature_pic/" + pic_name
        print(pic_name)
        with open(pic_path, "wb") as fp:
            fp.write(pic_content)
            print(pic_path + "写入成功")
            n_pic = n_pic + 1
