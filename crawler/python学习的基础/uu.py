

list1=['math','english','python','hbase']

list2=['0010','0011','0012','0013','0014']
dict1=dict(zip(list1,list2))#zip函数可以把2个列表相互对应，dict函数可以强制转化一个列表成字典

print(dict1)
#
# var=dict1.get('0016','没有对应的课程码')#查找
# print(var)
# #添加元素
# dict1['0015']='hive'
# print(dict1)
# dict1['0015']='信息检索'
# dict1['0016']='hive刘璟老师'
#遍历所有的健
# for key in dict1.keys():
#     print(key)
# for val in dict1.values():
#     print(val)
#遍历所有的键值的
# for key,val in dict1.items():
#     print(key,val)
# k=input()
# v=input()
# dict1={'北京' : '北京' ,  '山东' : '济南' }
# dict1[k]=v
# print(dict1)
# dict2=input()
# result=dict1.get(dict2)
# if result==None:
#     print("%s不存在"%dict1)
# print(result)
str=input()
count={}
for i in str:

 count[i]=str.count(i)

print(count)