# -OCR
> 本项目工具来源 百度飞浆 https://www.paddlepaddle.org.cn/hubdetail?name=ch_pp-ocrv3&en_category=TextRecognition 
##  1. 项目简述
服务于从大量图片提取文字的需求，可以用于pdf转txt
#### 主要流程如下：
- 使用Adobe Acrobat DC或者python脚本将pdf拆分成逐个的图片文件
- 对每张图进行ocr识别，提取文字
## 2.项目配置
```
需要依赖的环境:
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple 
```
## 3. 基本代码
```
import paddlehub as hub
import cv2

ocr = hub.Module(name="ch_pp-ocrv3", enable_mkldnn=True)       # mkldnn加速仅在CPU下有效
result = ocr.recognize_text(images=[cv2.imread('/PATH/TO/IMAGE')])

# or
# result = ocr.recognize_text(paths=['/PATH/TO/IMAGE'])
```
## 4. 实战代码
```
import paddlehub as hub
import cv2
import pandas as pd
import os
ocr = hub.Module(name="ch_pp-ocrv3", enable_mkldnn=True)       # mkldnn加速仅在CPU下有效

# 修改文件名
for filename in os.listdir(r'E:\new\pdfs\\'):   #‘logo/’是文件夹路径，你也可以替换其他
	newname = filename.replace('_页面', '')  #把jpg替换成png
	os.rename("E:/new/pdfs/"+filename, """E:/new/pdfs/"""+newname)  

num_page = int(input("请输入文件页数:"))
data = []
sum = 0 
for page in range(1, num_page+1):
    name_str = r"E:\new\pdfs\book1_{:03d}.jpg".format(page)
    result = ocr.recognize_text(images=[cv2.imread(name_str)])
    raw_data =  result[0]['data']
    row = 0
    for row, single_data in enumerate(raw_data):
        data.append([page, row, single_data['text']])
        sum += 1
    print(f"已经转换了{page}/{num_page}页")
final_data = pd.DataFrame(data=data,
             columns = ['page','row', 'text'],
             index=range(1, sum+1))
# print(final_data)
final_data.to_excel("模拟电子技术(第四版)文本数据.xlsx")
```