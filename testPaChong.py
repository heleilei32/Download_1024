#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests ##导入requests
import re
import os
import time
from bs4 import BeautifulSoup
from zcy_fun import get_format_filename
from zcy_fun import get_inner_link
from zcy_fun import Process_SubPage


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'Accept-Encoding': 'gzip, deflate, sdch',
    }


def getPage(page):
    file_path='E:\MyProjectFile'#存储的地址
    source = "国产高清"
    URL_1024 = 'http://1024.c2048ao.club/pw/thread.php?fid=3&page='+str(page)
    urlForce = "http://1024.c2048ao.club/pw/"
    start_html = requests.get(URL_1024, headers=headers)
    start_html.encoding='utf-8'
    print(start_html.text)
    bsObj = BeautifulSoup(start_html.text,'html.parser')
    aList=bsObj.find("tbody",{"style":"table-layout:fixed;"}).find_all("a")
    for a in aList:
        if ('href' in a.attrs) and ('title' not in a.attrs) and a.find("font")==None :
            if re.match(r'^htm_data/.+.html', a.attrs['href']):
                if source in a.getText():
                    print(a.getText())
                    toFile(a.getText());
                    getHTML(urlForce+a.attrs['href'].strip());


def toFile(data):
    file=open("bt1213.html","a+");
    file.write(data+"\n")
    file.close()

def getHTML(url):
    start_html = requests.get(url, headers=headers)
    start_html.encoding = 'utf-8'
    bsObj = BeautifulSoup(start_html.text, 'html.parser')
    alist = bsObj.find("div",{"class":"tpc_content"}).find_all("a")
    for a in alist:
        if re.match(r'^http:/.+.html', a.getText()):
            toFile(str(a))
            print(a);
    file = open("bt.txt", "a+");
    file.write("\n")
    file.close()


# getHTML(url = "http://1024.c2048ao.club/pw/htm_data/3/1710/830714.html");



# def sendPostFprDownLoan(type,id,name):
#     url="http://www3.uptorrentfilespacedownhostabc.biz/updowm/down.php";
#     data={"type":type,"id":id,"name":name}
#
#     print("downloading with requests")
#     x=requests.post(url,data=data)
#     print(x)

for x in range(1,12):
    print(x)
    getPage(x);


# sendPostFprDownLoan("torrent", "OY4RIPh", "73038.zip")