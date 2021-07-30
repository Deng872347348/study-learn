import json
# data='[{"name":"张三","age":"20"},{"name":"李四","age":"22"}]'
# list_data=json.loads(data)
#
# print(data)
# print(list_data)
#
# list2=[{"name":"张三","age":20},{"name":"李四","age":22}]
# data_json=json.dumps(list2)
#
# print(data_json)
# print(list2)

# list2=list2=[{"name":"张三","age":20},{"name":"李四","age":22}]
# str_data=json.dumps(list2)
# with open("02json.json",'w',encoding="utf-8") as f:
#     f.write(str_data)
# list3=[{"name":"张三","age":20},{"name":"李四","age":22}]
# json.dump(list3,open('02new.json','w'))
#
# fp=open('02new.json','r')
# result=json.load(fp)
# print(result)

import json
import  csv
#需求 json  中的文件   转换  成   csv文件

#1.分别  读 ，创建文件
json_fp = open('02new.json','r')
csv_fp = open('03csv.csv','w')
#2.提出  表头，表内容
data_list= json.load(json_fp)
sheet_title = data_list[0].keys()
sheet_data = []

for data in data_list:
    sheet_data.append(data.values())
# print(sheet_data)
#3.csv写入器
writer = csv.writer(csv_fp)
#4.写入表头
writer.writerow(sheet_title)
#5.写入内容
writer.writerows(sheet_data)
#6.关闭两个文件
json_fp.close()
csv_fp.close()
