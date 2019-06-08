# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:35:33 2019

@author: 王玙璠
"""
import cv2
import numpy as np
img = cv2.imread('./data/crop/8.jpg')
# 可以自己定义α和β的大小
res = np.uint8(np.clip((1 * img + 25), 0, 255))

cv2.imwrite('./data/crop' + '/'+ '78'+'.jpg',res)
