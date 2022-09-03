import re

import requests
from bs4 import BeautifulSoup

baseurl="http://icsc.brici.ac.cn/"

req = requests.get(baseurl+"index_suoyin.asp")

req.encoding = "utf-8"

html=req.text

soup = BeautifulSoup(req.text,features="html.parser")

company_item = soup.findAll("a",class_="zwname_detail")

icsc=[]

for items in company_item:
    detail_url = items.get('href')
    itemurl=baseurl+detail_url
    itemreq = requests.get(itemurl)
    itemreq.encoding = "utf-8"
    itemsoup = BeautifulSoup(itemreq.text,features="html.parser")

    r = re.findall('CAS登记号：(.*)\r\n', itemsoup.find("tr",class_="CardDetail").text)
    if len(r[0]) == 0 or r[0].find(';') != -1:
        print(itemurl)
    else:
        CAS={}
        CAS["CASNO"]=r[0]
        f_obj = open(r[0] + ".html", 'w', encoding="utf-8")
        f_obj.write(itemreq.text)
        f_obj.close()

        r = re.findall('中文名称：(.*)\r\n', itemsoup.find("td", class_="CardDetail").text)
        CAS["CASName"] = r[0]
        icsc.append(CAS)

print(icsc)


