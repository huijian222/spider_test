#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from requests import request

def GetRankPage():
    '''
    此处的网址应固定为：https://bcy.net/coser/allcoser
    获得网址内所有COSER的个人网址，为下一步的跳转准备
    后期可以加入代理功能
    '''
    url = 'https://bcy.net/coser/allcoser'
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    headers = {'User-Agent':user_agent}
    r = requests.get(url, headers=headers)
GetRankPage()
