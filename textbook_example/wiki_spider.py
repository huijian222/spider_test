#-*- coding:utf-8 -*-
import re
import random
import requests
from bs4 import BeautifulSoup as BS

links = set()
def GetWikiLinks(url = None):
    '''
    可以用维基百科词条/wiki/<词条名称>形式的URL链接作为参数， 然后以同样的形式返回一个列表，里面包含所有的词条 URL 链接。 
    '''
    global links
    headers = {'User-Agent' : '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 
                                 (KHTML, like Gecko)Chrome/23.0.1271.64 Safari/537.11'''}
    url = 'http://en.wikipedia.org' + url
    html = requests.get(url,headers)
    bsobj = BS(html.text , 'lxml')
    for link in  bsobj.findAll("a" , href = re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in links:
                newPage = link.attrs['href'] 
                print(newPage) 
                links.add(newPage) 
                GetWikiLinks(newPage)
            

GetWikiLinks("")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"] 
#     print(newArticle)
#     links = GetWikiLinks(newArticle)