# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import  pymysql
from .items import NovelItem,NovelItem2
class NovelPipeline:
    def process_item(self, item, spider):
        # ********** Begin **********#
        # 1.和本地的数据库mydb建立连接
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            port=3306,  # 端口号
            user='root',  # 自己的mysql用户名
            passwd='root',  # 自己的密码
            db='mydb',  # 数据库的名字
            charset='utf8',  # 默认的编码方式：
        )
        # 2.处理来自NovelprojectItem的item（处理完成后return返回item）
        if isinstance(item, NovelItem):
            # 从items里取出数据
            name = item['name']
            author = item['author']
            state = item['state']
            description = item['description']
            try:
                with connection.cursor() as cursor:
                    # 小说信息写入
                    sql1 = 'Create Table If Not Exists novel(name varchar(20) CHARACTER SET utf8 NOT NULL,author varchar(10) CHARACTER SET utf8,state varchar(20) CHARACTER SET utf8,description text CHARACTER SET utf8,PRIMARY KEY (name))'
                    sql2 = 'Insert into novel values (\'%s\',\'%s\',\'%s\',\'%s\')' % (name, author, state, description)
                    cursor.execute(sql1)
                    cursor.execute(sql2)
                # 提交本次插入的记录
                connection.commit()
            finally:
                # 关闭连接
                connection.close()
            return item
        # 3.处理来自NovelprojectItem2的item（处理完成后return返回item）
        elif isinstance(item, NovelItem2):
            tablename = item['tablename']
            title = item['title']
            try:
                with connection.cursor() as cursor:
                    # 小说章节的写入
                    sql3 = 'Create Table If Not Exists %s(title varchar(20) CHARACTER SET utf8 NOT NULL,PRIMARY KEY (title))' % tablename
                    sql4 = 'Insert into %s values (\'%s\')' % (tablename, title)
                    cursor.execute(sql3)
                    cursor.execute(sql4)
                connection.commit()
            finally:
                connection.close()
            return item
