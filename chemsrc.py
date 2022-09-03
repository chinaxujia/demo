import os
import random
import sys
from time import sleep

import requests
from bs4 import BeautifulSoup

from crawlerhelp import crawlerHelp


def loadCAS(index):
    filePath = './chemsrc/'
    Filehash = []
    Filelist = []
    for home, dirs, files in os.walk(filePath):
        path_list = home.split("/")
        currentPage = path_list[2]
        if currentPage != "" and int(currentPage) >= index:
            if Filehash.count(currentPage) == 0:
                Filehash.append(currentPage)
                Filelist.append({"page": currentPage, "files": []})
            for filename in files:
                Filelist[len(Filelist) - 1]["files"].append(filename)

    return Filelist


def pageLoad(list, page):
    result = True
    for i in range(0, len(list)):
        if page != 1:
            if int(list[i]["page"]) == page and len(list[i]["files"]) != 50:
                result = True
                break
            else:
                result = False
    return result


def CASLoad(list,CAS):
    result = False
    for i in range(0, len(list)):
        if list[i]["files"].count(CAS+".html") > 0:
            result = True
            break
        else:
            result = False
    return result

startpage = 22

CASList = loadCAS(startpage)

baseurl = "https://m.chemsrc.com"

pagelength = 100
# encoding: utf-8

count=1

proxyIP = crawlerHelp.getproxyip()

if proxyIP == "":
    print("未获取到代理IP")
    sys.exit()

for x in range(startpage, pagelength):

    page = x + 1

    pageload = True

    if pageload is True:
        print(u"开始爬：" + str(page) + "页")
        my_headers = [
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 "
            "Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 "
            "Safari/537.75.14",
            "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 "
            "Chrome/16.0.912.77 Safari/535.7",
            "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "
        ]

        proxy = {"http": "http://" + proxyIP, "https": "http://" + proxyIP}

        headers = {'User-Agent': random.choice(my_headers), 'Connection': 'close'}

        req = requests.get(baseurl + "/casindex/" + str(page) + ".html", headers=headers, proxies=proxy)

        req.encoding = "utf-8"

        if req.status_code != 200:
            print(req.text)

        soup = BeautifulSoup(req.text, features="lxml")

        icsc_item = soup.findAll("tr", class_="rowDat")

        detail_url = ""
        try:
            for item in icsc_item:
                detail_url = item.select("a")[0].get("href")
                print(detail_url)
                CASNo=detail_url.split("_")[0].split("/cas/")[1]
                print(CASNo)
                isLoad=CASLoad(CASList, CASNo)
                if isLoad is False:
                    itemurl = baseurl + detail_url
                    itemreq = requests.get(itemurl, headers=headers, proxies=proxy)
                    itemreq.encoding = "utf-8"
                    if itemreq.status_code == 200:
                        itemsoup = BeautifulSoup(itemreq.text, features="lxml")
                        if os.path.exists("chemsrc/" + str(page)) is False:
                            os.makedirs("chemsrc/" + str(page))
                        f_obj = open("chemsrc/" + str(page) + "/" + CASNo + ".html", 'w', encoding="utf-8")
                        f_obj.write(itemreq.text)
                        f_obj.close()
                        print(u"已爬："+str(count)+"条")
                        count=count+1
                        sleep(1)
        except 1:
            print(detail_url)
            print(detail_url.split("_")[1])
