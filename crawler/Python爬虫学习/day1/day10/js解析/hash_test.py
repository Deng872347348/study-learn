import hashlib

# data = 'https://cs.58.com/pinpaigongyu/?PGTID=0d200001-0019-eb7b-8486-f6818b0b9d41&ClickID=1'
data='https://cs.58.com/iphonesj/?PGTID=0d100000-0019-eadd-571b-0c33b1c7b6a9&ClickID=2'
# 创建hash对象

md5 = hashlib.md5()

# 向hash对象添加需要做hash运算的字符串

md5.update(data.encode())

# 获取字符串的hash值
result = md5.hexdigest()

print(result)