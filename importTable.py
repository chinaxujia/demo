import os
import psycopg2
from bs4 import BeautifulSoup
#encoding=utf-8
def loadCASHtml(index):
    filePath = './chemsrc/'
    Filelist = []
    for home, dirs, files in os.walk(filePath):
        path_list = home.split("/")
        currentPage = path_list[2]
        if currentPage != "" and int(currentPage) >= index:
            for filename in files:
                f = open(home+"/"+filename,'r', encoding='utf-8')
                text = f.read()
                itemsoup = BeautifulSoup(text, features="lxml")
                # 中文名
                CNName= ""
                # 英文名称
                ENName= ""
                # 中文别名
                Alias=""
                #分子式
                ChemFormula=""
                # 密度
                Density=""
                # 状态：形态
                State = ""
                # 危险性类别：危险类别
                CATEGHP= ""
                #危化品类别
                HAZCHEM= "普通化学品"
                # 管制类
                COR= "无"
                #更新时间
                UpdateTime=""
                if text.count("粉末") > 0 or text.count("晶体") > 0 or text.count("固体") > 0 or text.count("片状") > 0 or text.count("尖状") > 0 or text.count("块状") > 0:
                    State = "固体"
                elif text.count("液体") > 0 or text.count("溶液") > 0 :
                    State = "液体"
                elif text.count("气体") > 0 :
                    State = "气体"

                for item in itemsoup.find_all(class_="detail"):
                    if item.find("th") is not None:
                        th = item.find("th").text.strip()
                        if th == "中文名":
                            CNName = item.find("td").text.strip().replace(",","，").replace("'","‘")
                        elif th == "中文别名":
                            Alias = item.find("td").text.strip().replace('\n','').replace('\t','').replace(' ','').strip().replace(",","，").replace("'","‘")
                        elif th == "密度":
                            Density = item.find("td").text.strip()
                        elif th == "危险类别" or th == "危险性类别":
                            CATEGHP = item.find("td").text.strip().replace("(a)","").replace("(b)","").replace("(c)","")
                        elif th == "分子式":
                            ChemFormula = item.find("td").text.strip()
                        elif th == "英文名":
                            ENName = item.find("td").text.strip()
                #CAS号
                CASID = filename.replace(".html", "")
                if CNName!="":
                    UpdateTime = itemsoup.find(class_="text-center font-grey").text.replace("更新时间：", "")
                    Filelist.append({"CNName":CNName, "Alias":Alias, "CASID":CASID, "ChemFormula":ChemFormula, "Density":Density, "State":State,
                                 "CATEGHP":CATEGHP, "HAZCHEM":HAZCHEM, "COR":COR, "UpdateTime":UpdateTime})
                else:
                    print(CASID)
    return Filelist

CASList = loadCASHtml(0)

conn = psycopg2.connect(database="SmartApp", user="postgres", password="pgsql@things", host="192.168.0.205", port="5432")

print("Opened database successfully")

cursor = conn.cursor()

def get_i_sql(table, dict):
    keys=[]
    values=[]
    fileds=[]
    for k, v in dict.items():
        keys.append(str(k))
        values.append(str(v))
        fileds.append('%s')
    sql = "insert into " +table + '(\"'+'\",\"'.join(keys)+"\") values('"+"','".join(fileds)+"')"
    return sql % (values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8],values[9])
# sql语句


for i in range(0,len(CASList)):
    sql="select * from chemicalinfo where \"CASID\"='"+CASList[i]["CASID"]+"'"
    cursor.execute(sql)
    row = cursor.fetchone()
    if row is None:
        sql=get_i_sql("chemicalinfo",CASList[i])
        #print(sql)
        cursor.execute(sql)
conn.commit()
conn.close()
# 关闭数据库连接
