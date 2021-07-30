# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import  pymysql
class MaoyanMoviesPipeline:
    def process_item(self, item, spider):
        #连接数据库
        connection=pymysql.connect(
            host='localhost', #连接到的是本地的数据库
            port=3306,  #数据库的端口号
            user="root",  #自己的mysql用户名
            passwd='root', #自己的密码
            db='mydb',
            # charset='utf-8' #默认的编码格式
        )
        # 2.建表、给表插入数据，完成后关闭数据库连接，return返回item
        name = item['name']
        starts = item['starts']
        releasetime = item['releasetime']
        score = item['score']
        try:
            with connection.cursor() as cursor:
                sql1 = 'Create Table If Not Exists mymovies(name varchar(50) CHARACTER SET utf8 NOT NULL,starts text CHARACTER SET utf8 NOT NULL,releasetime varchar(50) CHARACTER SET utf8 DEFAULT NULL,score varchar(20) CHARACTER SET utf8 NOT NULL,PRIMARY KEY(name))'
                # 单章小说的写入
                sql2 = 'Insert into mymovies values (\'%s\',\'%s\',\'%s\',\'%s\')' % (
                    name, starts, releasetime, score)
                cursor.execute(sql1)
                cursor.execute(sql2)
            # 提交本次插入的记录
            connection.commit()
        finally:
            # 关闭连接
            connection.close()
            return item
