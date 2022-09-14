import numpy as np
import cv2
import os
import matplotlib.pyplot as plt
import csv
data = []
all_data = []
count = 0
count1 = 0
path = "C:\\Users\\watermelon\\Desktop\\watersalt\\salt\\original_img\\original"  # 图像读取地址
filelist = os.listdir(path)  # 打开对应的文件夹
total_num = len(filelist)
#水盐模块：遍历，存储所有img数据于data.npy
for i,img_path in enumerate(os.listdir(path)):
    image = cv2.imread(os.path.join(path,img_path))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # print(filename)
    low_hsv = np.array([85, 43, 46])
    high_hsv = np.array([124, 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i, j] >= 10 :
                count1 = count1 + 1
    all_data.append(count1)
np.save('data.npy',np.asarray(all_data))

#天气模块
weather_path = "上海2020.11--2021.02天气记录.csv"
with open(weather_path, encoding='utf-8') as f:
    csv_as_list = list(csv.reader(f, delimiter=","))
    for i in range(len(csv_as_list)):
        for j in range(len(csv_as_list[0])):
            if '中雨' in csv_as_list[i][j]:
                data.append(csv_as_list[i][0])
                
#预警模块
data1 = np.load('data.npy')
date = '2020'#年份
month = 11#月份
day = 24#img0日期-1
time = -8#时间-8
water_list = []
coupe = []
nvar = []
for i,j in enumerate(list(data1)):
    if (i+1)%3==0:#按日期分组
        coupe.append(j)
        water_list.extend([coupe])
        coupe = []
    else:
        coupe.append(j)
for i in water_list:
    var = int(np.var(i))#求每组方差
    nvar.append(var)
avar = np.percentile(nvar,85)# gives the 85th percentile

for i in nvar:
    day = day + 1
    if day % 31 == 0:
        day = day % 31 + 1
        month = month + 1
    if i > avar:
        if "{}/{}/{}".format(date, month, day) in data:
            print("{}年{}月{}日,水流变化剧烈，请注意防护。".format(date, month, day))












