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



#>>>>>>>>> 预警弹窗 >>>>>>>>>

import tkinter as tk
from tkinter import Label

# 设置窗口居中显示函数 center_window(root, width, height)
def center_window(root, width, height):
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    print(size)
    root.geometry(size)
    root.update()
    print(root.winfo_x())

root = tk.Tk()
root.title('预警信息')
root.wm_attributes('-topmost',1)  # 置顶窗口
center_window(root, 500, 80)
txt = Label(root, text = "\n\n{}年{}月{}日, 水流变化剧烈，请注意防护。\n\n".format(date, month, day)).pack()  # 窗口显示具体提示内容
root.mainloop()

# 弹窗代码参考连接1：https://blog.csdn.net/dhjabc_1/article/details/105428853?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522166316153316782412548863%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=166316153316782412548863&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-105428853-null-null.142^v47^pc_rank_34_1,201^v3^control_2&utm_term=tkinter%E7%AA%97%E5%8F%A3%E5%BC%B9%E5%87%BA%E4%BD%8D%E7%BD%AE&spm=1018.2226.3001.4187
# 弹窗代码参考链接2：https://jingyan.baidu.com/article/a378c960ce4f02f229283047.html

# from tkinter import *

# win = Tk()
# win.title("预警信息")

# txt = Label(win, text = "\n\n{}年{}月{}日,水流变化剧烈，请注意防护。\n\n".format(date, month, day)).pack()
# win.mainloop()

#<<<<<<<<< 预警弹窗 <<<<<<<<<