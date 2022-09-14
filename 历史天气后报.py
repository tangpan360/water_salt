import requests
from bs4 import BeautifulSoup
import pandas as pd

# #====================================上海2020.11历史天气数据======================================'''
# # 目标url
# url = 'http://www.tianqihoubao.com/lishi/shanghai/month/202011.html'
# # 获取网页源代码
# req = requests.get(url)
# html = req.text
# soup = BeautifulSoup(html,'html.parser')
# tr_list = soup.find_all('tr')
# datas,condition,temp = [], [], []
# for data in tr_list[1:]:
#     sub_data = data.text.split()
#     a = sub_data[0].replace('年','/')
#     b = a.replace('月','/')
#     c = b.replace('日', '')
#     datas.append(c)
#     condition.append(''.join(sub_data[1:3]))
#     temp.append(''.join(sub_data[3:6]))
# # 数据保存
# _data = pd.DataFrame()   # 创建一个表格
# _data['日期'] = datas  #向表格内添加数据
# _data['天气状况'] = condition
# _data['温度'] = temp
# _data.to_csv('上海2020.11天气记录.csv',index=False, encoding='utf-8')


#====================================上海2020.11--2021.02的历史天气数据======================================'''

# 获取url
def get_data(url):
    req = requests.get(url)
    html = req.text
    # 数据提取
    soup = BeautifulSoup(html,'html.parser')
    tr_list = soup.find_all('tr')
    datas,condition,temp = [], [], []
    for data in tr_list[1:]:
        sub_data = data.text.split()
        # print(sub_data)
        a = sub_data[0].replace('年','/')
        b = a.replace('月','/')
        c = b.replace('日', '')
        datas.append(c)
        condition.append(''.join(sub_data[1:3]))
        temp.append(''.join(sub_data[3:6]))
    # 数据保存
    _data = pd.DataFrame()   # 创建一个表格
    _data['日期'] = datas  #向表格内添加数据
    _data['天气状况'] = condition
    _data['温度'] = temp
    # print(_data)
    return _data

data_01 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202011.html')
print('get202011')
data_02 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202012.html')
print('get202012')
data_03 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202101.html')
print('get202101')
data_04 = get_data('http://www.tianqihoubao.com/lishi/shanghai/month/202102.html')
print('get202102')

data = pd.concat([data_01,data_02,data_03,data_04]).reset_index(drop=True)
data.to_csv('上海2020.11--2021.02天气记录.csv',index=False, encoding='utf-8')
