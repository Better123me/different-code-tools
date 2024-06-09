import re
import requests

def translate(text):
    url = "https://fanyi.baidu.com/ait/text/translate"
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',

    }
    data = {
        'domain':'common',
        'from':'zh',
        'qcSettings':[f"{i}" for i in range(1, len(text))],
        'query':text,
        'reference':"",
        'to':'en',
        'milliTimestamp':1717641542277              ？？？
    }
    response = requests.post(url=url, headers=headers, data=data)
    print(response.text)

text = input("请输入翻译内容:")
translate(text)