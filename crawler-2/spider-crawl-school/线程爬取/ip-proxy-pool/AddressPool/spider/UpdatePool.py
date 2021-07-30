import requests
import MySQLdb
import time
def get_data():
    dbs =MySQLdb.connect(host="0.0.0.0", user="user", passwd="wydiisasdsd##&user", db="AddressPool", charset="utf8")
    cursor=dbs.cursor()
    cursor.execute("SELECT * FROM address_table1 where type='https'")
    AddressPool=cursor.fetchall()
    print("总共搜索到" + str(len(AddressPool)) + "条https类型的代理")
    for data in AddressPool:
        verification(data,dbs=dbs)
    dbs.close()
def verification(data,dbs):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36'
    }
    proxies={
        "http":"http://%s:%s"%(data[1],data[3]),
    }
    url ="https://www.baidu.com/"#https://19ncc.medmeeting.org/cn
    if data[2]=="https":
        proxies={
            "https": "https://%s:%s" % (data[1], data[3])
        }
        url="https://www.baidu.com/"
    start=(int)(time.time()*1000)
    try:
        response=requests.get(url=url,headers=headers,proxies=proxies,timeout=5)
        code=response.status_code
    except:
        print("代理失效")
        return
    stop=(int)(time.time()*1000)
    if code==200:
        speed=str(stop-start)
        times=str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start/1000)))
        sql='''UPDATE address_table1 SET speed=%s,times="%s" WHERE id=%s'''%(speed,times,str(data[0]))
        dbs.cursor().execute(sql)
        sql='''INSERT INTO address_table2(address,type,port,isAnonymity,Location,times,speed) VALUES("%s","%s","%s","%s","%s","%s",%s)'''%(data[1],data[2],data[3],data[4],data[5],times,speed)
        dbs.cursor().execute(sql)
        dbs.commit()
        print("IP:"+data[1]+" \t"+"time:"+speed+"ms")
def delect_data():
    dbs = MySQLdb.connect(host="0.0.0.0", user="user", passwd="wydiisasdsd##&user", db="AddressPool", charset="utf8")
    dbs.cursor().execute("TRUNCATE TABLE address_table2")
    dbs.commit()
    dbs.close()
if __name__ == '__main__':
    delect_data()
    get_data()
