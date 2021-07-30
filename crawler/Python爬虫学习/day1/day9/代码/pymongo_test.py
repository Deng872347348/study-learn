# pip install pymongo 需要下载
# 无需权限认证的方式创建连接对象以及集合操作对象
from pymongo import MongoClient

# 创建数据库链接对象
client = MongoClient('127.0.0.1',27017)

# 选择一个数据库
db = client['admin']
db.authenticate('python','python')

# 选择一个集合
col = client['pydata']['test']

# 添加数据 insert
col.insert({"class":"python37"})  # 添加一条数据
# col.insert([{"class":'python38'},{"class":"python39"},{"class":"python40"}]) # 添加多条数据
# print(col.find_one())
#
# for data in col.find():
#     print(data)
#
# print("*" * 50)

#全文覆盖更新
# col.update({"class":"python40"},{"message":"helloworld"})
# print(col.find_one())