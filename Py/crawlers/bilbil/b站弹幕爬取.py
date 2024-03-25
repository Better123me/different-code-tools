import random
import json
import pandas as pd
import requests
import time
import re

PAGES = 3
MAX_COMMENT_PAGE = 5
headers_list = [
    {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.109 Safari/537.36 CrKey/1.54.248666'
    }, {
        'user-agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
    }, {
        'user-agent': 'Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+'
    }, {
        'user-agent': 'Mozilla/5.0 (PlayBook; U; RIM Tablet OS 2.1.0; en-US) AppleWebKit/536.2+ (KHTML like Gecko) Version/7.2.1.0 Safari/536.2+'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.3; en-us; SM-N900T Build/JSS15J) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.0; en-us; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G950U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G965U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T837A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.80 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; en-us; KFAPWI Build/JDQ39) AppleWebKit/535.19 (KHTML, like Gecko) Silk/3.13 Safari/535.19 Silk-Accelerated=true'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; LGMS323 Build/KOT49I.MS32310c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 550) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/14.14263'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 10 Build/MOB31T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 5X Build/OPR4.170623.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Nexus 6P Build/OPP3.170518.006) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7 Build/MOB30X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; NOKIA; Lumia 520)'
    }, {
        'user-agent': 'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Pixel 3 Build/PQ1A.181105.017.A1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
    }, {
        'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
    }
]
headers = random.choice(headers_list)
headers['Cookie'] = """"""  # 输入cookies
#　根据搜索主题爬取前５面所有视频的链接和基本数据
    # 两个变量page_num 和 key
urls = ["""https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=1&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=抗日&qv_id=LPJ4kGtXkfWWXrJm3YrL59iG1yYDRtxE&ad_resource=5654&source_tag=3&gaia_vtoken=&category_id=&search_type=video&dynamic_offset=24&web_location=1430654&w_rid=37daad3cfc34c9134c80da84124c99b7&wts=1691074216""",
        """https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=2&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=抗日&qv_id=LPJ4kGtXkfWWXrJm3YrL59iG1yYDRtxE&ad_resource=5654&source_tag=3&gaia_vtoken=&category_id=&search_type=video&dynamic_offset=24&web_location=1430654&w_rid=37daad3cfc34c9134c80da84124c99b7&wts=1691074216""",
        """https://api.bilibili.com/x/web-interface/wbi/search/type?__refresh__=true&_extra=&context=&page=3&page_size=42&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword=抗日&qv_id=LPJ4kGtXkfWWXrJm3YrL59iG1yYDRtxE&ad_resource=5654&source_tag=3&gaia_vtoken=&category_id=&search_type=video&dynamic_offset=24&web_location=1430654&w_rid=37daad3cfc34c9134c80da84124c99b7&wts=1691074216"""]
# 获取页面上所有的视频的bvid、观看量play、点赞量like、视频名称title. 弹幕oid
# contents = {'bvid':[], 'play':[], 'like':[], 'title':[],  'kind':[]}
contents = []

for cnt in range(PAGES):
    url = urls[cnt]
    response = requests.get(url, headers=headers)
    result_list = json.loads(response.text)
    print(result_list)
    result = result_list['data']['result']      #　所有的数据都在result中
    for i in range(42):                         #　一面42个视频
        contents.append({'oid':result[i]['aid'],
                         'play':result[i]['play'],
                         'like':result[i]['like'],
                         'title':result[i]['title'],
                         'label':"unKnown",
                         'stage':1})

    print(f"搜索页第{cnt+1}页爬取完成")
webData = pd.DataFrame(contents)
webData.to_excel("b站抗日主题视频信息.xlsx", sheet_name='Sheet1')

# 爬取评论区
path_part_1 = "https://api.bilibili.com/x/v2/reply/main?csrf=80712918b34e2e3645d93764c36cadd6&mode=3" \
              "&oid="
path_part_2 = "&pagination_str=%7B%22offset%22:%22%7B%5C%22type%5C%22:1,%5C%22direction%5C%22:1,%5C%22data%5C%22:%7B%5C%22pn%5C%22:"
path_part_3 = "%7D%7D%22%7D&plat=1&type=1"
content_list = []
for tmp in contents:
    oid = tmp['oid']
    try:
        for page in range(MAX_COMMENT_PAGE):
            path = path_part_1 + str(oid) + path_part_2 + str(page + 1) + path_part_3
            response = requests.get(path, headers=headers)
            tmp_comment = re.findall('content":{"message":"(.*?)"', response.text)
            # 把最后两个打广告的去掉
            tmp_comment.pop()
            tmp_comment.pop()
            for each_comment in tmp_comment:
                content_list.append({"comments": each_comment, "stage": 1, "oid": oid})

        print(f"{oid}评论区爬取完成")
    except:
        print(f"{oid}评论区爬取失败！")
        pass
data = pd.DataFrame(content_list)
data.to_excel("b站评论区.xlsx", sheet_name='Sheet1')