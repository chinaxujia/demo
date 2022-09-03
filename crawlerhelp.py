import json

import requests

class crawlerHelp(object):
    @staticmethod
    def getproxyip():
        f = open('白名单IP.txt', encoding='gbk')
        ip = ""
        for line in f:
            ip = line.strip()
        url = r'http://api.tianqiip.com/white/add?key=wuxixujia&brand=2&sign=3c1e4d3f92044e98059909c250635c5d&ip=' + ip
        proxyip = ""
        req = requests.get(url)
        req.encoding = "utf-8"
        result = json.loads(req.text)
        if result['code'] != 200 and result['code'] != 1007:
            return proxyip
        url = r'http://api.tianqiip.com/getip?secret=0cjj5z4jbt9e1kso&num=1&type=json&port=2&time=3&sign' \
              r'=3c1e4d3f92044e98059909c250635c5d&ts=1'
        req = requests.get(url)
        result = json.loads(req.text)
        if result['code'] != 200 and result['code'] != 1000:
            return proxyip
        proxyip = result['data'][0]['ip'] + ":" + str(result['data'][0]['port'])
        return proxyip

    @staticmethod
    def TestConn():
        print('s')

