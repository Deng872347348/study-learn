import requests
import MySQLdb
import random
from lxml import etree
def get_address(url,dbs):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
        'Referer':'https://www.xicidaili.com/'
    }
    #cursor =dbs.cursor()
    #cursor.execute("SELECT * FROM address_table1 where type='https'")
    #AddressPool = cursor.fetchall()
    #data=random.choice(AddressPool)
    #print(data)
    #proxies={
    #    "https": "https://%s:%s" % (data[1], data[3])
    #}
    try:
        response=requests.get(url=url,headers=headers)#,proxies=proxies,timeout=5)
    except:
        print("请求失败：代理IP无效")
        return
    if response.status_code==200:
        print("请求成功")
        return response.text
    else:
        print(response.status_code,"请求失败")
def pase_data(html,Xpath1):
    #print(html)
    sous=etree.HTML(html)
    #print(sous)
    trs=sous.xpath(Xpath1)
    #print(Xpath1,trs)
    messeage=[]
    for tr in trs:
        ipAddress={}
        ipAddress['address']=tr.xpath('./td[2]/text()')[0].strip()#IP地址
        ipAddress['port']=tr.xpath('./td[3]/text()')[0].strip()#端口
        #ipAddress['Location']=tr.xpath('./td[4]/a/text()')[0].strip()#服务器地址
        ipAddress['isAnonymity'] = tr.xpath('./td[5]/text()')[0].strip()#是否高匿
        ipAddress['type'] = tr.xpath('./td[6]/text()')[0].strip()#代理类型
        ipAddress['datetime']=tr.xpath('./td[10]/text()')[0].strip()
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
            sql="INSERT INTO address_table1(address,type,port,isAnonymity,times) VALUES(%s,%s,%s,%s,%s)"
            print(ipAddress['address'],ipAddress['type'],ipAddress['port'],ipAddress['isAnonymity'],ipAddress['datetime'])
            param=(ipAddress['address'],ipAddress['type'],ipAddress['port'],ipAddress['isAnonymity'],ipAddress['datetime'])
            cursor.execute(sql,param)
            dbs.commit()
        else:
            print("地址已存在")

if __name__ == '__main__':
    num=0
    dbs = MySQLdb.connect(host="0.0.0.0",user= "user",passwd= "wydiisasdsd##&user",db= "AddressPool", charset="utf8")
    #while(1):
    num+=4
    url = "https://www.xicidaili.com/nn/"+str(num)#西刺：
        #url="https://www.baidu.com/"
    xpath1='.//table[@id="ip_list"]/tr[@class]'
    html=get_address(url,dbs)
    messeage=pase_data(html,Xpath1=xpath1)
    Save_Datepase(messeage,dbs)
    if(num==4049):
        pass
print("数据已存取完毕")
