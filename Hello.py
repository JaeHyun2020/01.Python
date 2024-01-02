import cv2 
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image 
from io import BytesIO 

print('---------------------------------------------------------------------------------------------------- 001. Start')
print('Hello Python')

url = 'https://cafeptthumb-phinf.pstatic.net/MjAxODA4MDRfMTMz/MDAxNTMzMzY4NzgyODky.yogSRvpzWgy9I39zZ0dfFi1lK-DjCpUJZ91pV_lSbgkg.shBbhXwhE7k15KKwlUVQ21A7HA0qKAFCmkEy3yQCo-Yg.JPEG.polar2000/20180802_151259.jpg?type=w800'
response = requests.get(url)
pic = Image.open(BytesIO(response.content))
pic_arr = np.asarray(pic)
# print(pic_arr.shape)
# print(pic_arr)
plt.imshow(pic_arr)
plt.show()
print('---------------------------------------------------------------------------------------------------- 999. End')

# 45분부터