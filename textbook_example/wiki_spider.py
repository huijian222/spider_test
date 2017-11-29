#-*- coding:utf-8 -*-
import re
import random
import requests
from bs4 import BeautifulSoup as BS

def getInterLinks(bsobj, includeLink):
    interLinks = []
    for link in bsobj.findAll("a", href = re.compile("^(/|.*"+includeLink+")")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in interLinks:
                interLinks.append(link.attrs['href'])
    return interLinks

def getOuterLinks(bsobj, incloudelink):
    outerLinks = []
    for link in bsobj.findAll("a", href = re.compile("^(http|www)((?!"+incloudelink+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in outerLinks: 
                outerLinks.append(link.attrs['href'])
    return outerLinks

def getInterPageUrl(pageUrl):
    pageUrl = re.subn("https?://", "",pageUrl)
    pageUrl = str(pageUrl[0]).split("/")
    #$pageUrl = pageUrl.replace("https?://", "").split("/")
    return pageUrl[0]

def getRandomExternalLink(startingPage):
    headers = {'User-Agent' : '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 
                                 (KHTML, like Gecko)Chrome/23.0.1271.64 Safari/537.11'''}
    html = requests.get(startingPage, headers)
    bsobj = BS(html.text, 'lxml')
    outerLink = getOuterLinks(bsobj, getInterPageUrl(startingPage))
    if len(outerLink) == 0:
        innerHtml = getInterLinks(bsobj, "")
        return getRandomExternalLink(innerHtml[random.randint(0, len(innerHtml) - 1)])
    else:
        return outerLink[random.randint(0, len(outerLink) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite) 
    print("随机外链是:"+externalLink) 
    followExternalOnly(externalLink)
    
followExternalOnly("http://oreilly.com")
# print(getInterPageUrl("https://oreilly.com/temp/tem1.html"))
# links = set()
# def GetWikiLinks(url = None):
#     '''
#     可以用维基百科词条/wiki/<词条名称>形式的URL链接作为参数， 然后以同样的形式返回一个列表，里面包含所有的词条 URL 链接。 
#     '''
#     global links
#     headers = {'User-Agent' : '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 
#                                  (KHTML, like Gecko)Chrome/23.0.1271.64 Safari/537.11'''}
#     url = 'http://en.wikipedia.org' + url
#     html = requests.get(url,headers)
#     bsobj = BS(html.text , 'lxml')
#     try:
#         print(bsobj.h1.get_text())
#         print(bsobj.find('', {'id' : 'mw-content-text'}).findAll('p')[0])
#         print(bsobj.find(id="ca-edit").find("span").find("a").attrs['href'])
#     except AttributeError:
#         print('page attrs miss')
#     for link in  bsobj.findAll("a" , href = re.compile("^(/wiki/)")):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in links:
#                 newPage = link.attrs['href'] 
#                 print("----------------\n"+newPage)
#                 links.add(newPage) 
#                 GetWikiLinks(newPage)

# GetWikiLinks("")
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs["href"] 
#     print(newArticle)
#     links = GetWikiLinks(newArticle)