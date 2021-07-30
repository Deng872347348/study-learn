import requests
import MySQLdb
from lxml import etree
def get_address(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text


def pase_data(html,Xpath1):
    html=etree.HTML(html)
    trs=html.xpath(Xpath1)
    print(trs)
    messeage=[]
    for tr in trs:
        ipAddress={}
        ipAddress['address']=tr.xpath('./td[1]/text()')[0].strip()
        ipAddress['port']=tr.xpath('./td[2]/text()')[0].strip()
        ipAddress['Location']=tr.xpath('./td[3]/text()')[0].strip()
        ipAddress['datetime']=tr.xpath('./td[5]/text()')[0].strip()
        messeage.append(ipAddress)
    return messeage
def Save_Datepase(messeage,dbs):
    cursor=dbs.cursor()
    for ipAddress in messeage:
        sql="select count(*) from address_table1 WHERE address=\"" + ipAddress['address'] + "\""
        cursor = dbs.cursor()
        cursor.execute(sql)
        count=cursor.fetchone()[0]
        if count==0:
            sql="INSERT INTO address_table1(address,type,port,Location,times) VALUES(%s,%s,%s,%s,%s)"
            param=(ipAddress['address'],"HTTP",ipAddress['port'],ipAddress['Location'],ipAddress['datetime'])
            cursor.execute(sql,param)
            dbs.commit()
        else:
            pass

if __name__ == '__main__':
    num=0
    dbs = MySQLdb.connect(host="0.0.0.0",user= "user",passwd= "wydiisasdsd##&user",db= "AddressPool", charset="utf8")
    while(1):
        num+=1
        url = "http://www.89ip.cn/index_"+str(num)+".html"#西刺：https://www.xicidaili.com/wn/1
        xpath1='.//table/tbody/*'

        html=get_address(url)
        messeage=pase_data(html,Xpath1=xpath1)
        Save_Datepase(messeage,dbs)
        if(num==26):
            break
    print("数据已存取完毕")
