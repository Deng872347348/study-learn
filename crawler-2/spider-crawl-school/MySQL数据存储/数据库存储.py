# import pymysql
# import uuid
# from hashlib import md5
# #连接数据库
# conn=pymysql.connect("127.0.0.1","root", "root", "trafficdb", charset='utf8' )
# # print(conn)
# #2,生成游标对象
#
# cursor=conn.cursor()
#
# 3,创建表
# cursor.execute("DROP TABLE IF EXISTS  USER ")
# sql='''
#     CREATE TABLE USER(
#     ID VARCHAR(64) NOT NULL PRIMARY KEY,
#     USERNAME VARCHAR(32) NOT NULL,
#     PASSWORD VARCHAR(32)  NOT NULL
#     )
# '''
# cursor.execute(sql)
# cursor.close()
# conn.close()
#
# password=md5('2332'.encode('utf-8')).hexdigest()#把密码通过md5加密
# print(password)
#
# sql='''
#   INSERT INTO USER(ID,USERNAME,PASSWORD) VALUES ('%s','%s','%s')
# '''%(uuid.uuid1(),'root','root')
# try:
#     cursor.execute(sql)
#     conn.close()
# except:
#     conn.rollback()#数据库回滚
# cursor.close()
# conn.close()
#
# sql='''INSERT INTO USER(ID,USERNAME,PASSWORD) VALUES (%s,%s,%s)'''
# data=[str(uuid.uuid1()),'user2',md5('123'.encode('utf-8')).hexdigest(),
#       str(uuid.uuid1()),'user2',md5('123'.encode('utf-8')).hexdigest(),
#       str(uuid.uuid1()),'user2',md5('123'.encode('utf-8')).hexdigest()]
# print(sql)
# try:
#     cursor.executemany(sql,data)
# except:
#     print("插入失败")







import pymysql
import uuid
from hashlib import md5
#连接数据库
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',charset='utf8', db ='trafficdb')
# print(conn)
#2,生成游标对象
cursor=conn.cursor()
# table="traffic"
#
# all_data =[{'Id':str(uuid.uuid1()),'traffic_time': '2020年10月27日', 'traffic_place': '宁乡市宁乡大道与永佳路交叉路口', 'traffic_code': '湘A9JF75', 'traffic_type': '机动车', 'traffic_action': '机动车逆向行驶', ' traffic_rule': '记三分，罚款200元'},
#        {'Id':str(uuid.uuid1()),'traffic_time': '2020年10月28日', 'traffic_place': '望城市宁乡大道与永佳路交叉路口', 'traffic_code': '湘A9JF75', 'traffic_type': '机动车', 'traffic_action': '机动车逆向行驶', ' traffic_rule': '记三分，罚款200元'}]
# data=all_data[0]
# fields=",".join("`{}`".format(i) for i in data.keys())#拼装出字段
# values=",".join("%({})s".format(i) for i in data.keys())#拼装出values里面的值
#
#
# # print(values)
# # 第一种
# # sql = "INSERT INTO "+table+"("+fields+") values ("+values+")"
# # print(sql)
# # 第二种
# sql = "INSERT INTO "+table+" (%s) values(%s)"
# rel_sql = sql%(fields,values)
# print(rel_sql)
# # 执行sql语句
# cursor.executemany(rel_sql,data)  # 插入一条数据，data是字典
# conn.commit()
# cursor.close()
# conn.close()


#2,生成游标对象
# cursor=conn.cursor()
table='traffic'
all_data =[{'Id':str(uuid.uuid1()),'traffic_time': '2020年10月27日', 'traffic_place': '宁乡市宁乡大道与永佳路交叉路口', 'traffic_code': '湘A9JF75', 'traffic_type': '机动车', 'traffic_action': '机动车逆向行驶', 'traffic_rule': '记三分，罚款200元'},
       {'Id':str(uuid.uuid1()),'traffic_time': '2020年10月28日', 'traffic_place': '望城市宁乡大道与永佳路交叉路口', 'traffic_code': '湘A9JF75', 'traffic_type': '机动车', 'traffic_action': '机动车逆向行驶', 'traffic_rule': '记三分，罚款200元'}]
data=all_data[0]
fields=",".join("`{}`".format(i) for i in data.keys())
value=",".join("%({})s".format(i) for  i in data.keys())
"%({})s"
print(fields)
print(value)
# sql="insert into"+table+"("+fields+") values("+value+")"
# print(sql)
# 第二种拼装方法
sql="insert into"+table+"(%s) value(%s)"
rel_sql=sql%(fields,value)
print(rel_sql)
#执行数据库代码
cursor.execute(rel_sql,data)
conn.commit()
cursor.close()
conn.close()













