import requests as re
re.packages.urllib3.disable_warnings()
headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"
}
url = "https://fanyi.baidu.com/sug"
# 设置参数      在负载处可以看到参数列表
print("欢迎使用这个小demo！")
k = 98
while(k != 27):
    kw = input("请输入需要翻译的词语：")
    param = {
        "kw":kw
    }
    # 发送请求
    response_json = re.post(url=url, params=param).json()
    if (len(response_json['data'])!=0):
        print()
        print('='*20)
        print(response_json['data'][0]['v'])
        print('=' * 20)
        print()

    else:
        print("没有翻译结果")


# 使用的时候不能开系统代理