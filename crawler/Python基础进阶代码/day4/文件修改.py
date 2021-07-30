# -*- coding:utf-8 -*-
# created by Alex Li - 路飞学城

f =open("stock_data","r+")

# 1. 加载到内存
data = f.read()
new_data = data.replace("吉贝尔","路飞学城")
print(new_data)
# 2. 清空文件
f.seek(0)
f.truncate()  # 截断文件

# 3. 把新内容写回硬盘
f.write(new_data)

f.close()