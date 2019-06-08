# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 16:59:24 2019

@author: 王玙璠
"""
from PIL import Image
import os
#import cv2
from glob import glob



files = os.path.join('./data','*.jpg')
filelist = glob(files)
fout = './data/crop'
for k in range(len(filelist)):
    image = Image.open(filelist[k])
    print(image.size[0])
    print(image.size[1])
    cropped = image.crop((0, 0, 1000, 1000))  # 裁剪坐标为[y0:y1, x0:x1]
    number = str(k)
    cropped.save(fout + '/'+ number+'.jpg')
