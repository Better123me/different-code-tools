import requests
import json
import cv2
from PIL import Image
import time
T1 = time.perf_counter()
input_image_name = 'img.jpg'
api_host = 'http://127.0.0.1:8002/hello'
type_rq = 'img_object_detection_to_json'

files = {'file': open(input_image_name, 'rb')}

response = requests.post(api_host, files=files)
T2 = time.perf_counter()
print(f"用时：{(T2-T1)*1000}毫秒")
