#任务40
import pandas as pd
import  numpy as np
#任务40
# print(mulitindex_series)
# name=['python','java','php']
# ss=['期末','期中']
# df2=pd.DataFrame(np.random.randint(0,150,size=(6,6)),index=['A','B','C','D','E','F'],
#                  columns=pd.MultiIndex.from_product(iterables=[name,ss],names=['name','ss']))
# print(df2)

#任务41:
# data1=pd.DataFrame(np.random.randint(0,150,size=(6,6)),index=['A','B','C','D','E','F'],
#                   columns=pd.MultiIndex.from_product([['python','cn','math'],['期中','期末']]))
#
# print(data1)
# print(data1['python'])
# print(data1['python','期末']['A':'C'])#取多行单列
# print(data1['A':'C']['python','期末'])
# print(data1.loc['A'])#loc方法取一行

# print(data1.mean(axis=1,level=1).round(2))
# print(data1.mean(axis=0).round(2))

#任务42取课程期中，期末的最高分
# print(data1.max(axis=0))

#课程每个同学创成绩中的最低分
# print(data1.min(axis=1))
#
# print(data1.describe())
# print(data1.value_counts())

#任务43
# a=pd.Series([9,8,7,6],index=list('abcd'))
# print(a.describe())
# print(type(a.describe()))
# print(a.describe()['count'])
# print(a.describe()['max'])

#任务43
# b=pd.DataFrame(np.arange(20).reshape(4,5),index=list('abcd'))

# print(b.describe())
# print(type(a.describe()))
# print(b.describe().loc['max'])
# print(b.describe()[2])

#任务44 sort_index 排序
# print(b)
#
# print(b.sort_index())#升序排序
#
# print(b.sort_index(ascending=False))#降序排序

#任务45
# print(b.sort_values(2,ascending=False))
#
# print(b.sort_values('a',axis=1,ascending=False))


df_obj=pd.read_excel('scores.xlsx',header=[0,1])
sorted_obj=df_obj.sort_index(ascending=False)
# print(df_obj)
# print(sorted_obj)
# print(sorted_obj.max)
# print(sorted_obj.min)
print(sorted_obj.describe())
# result=sorted_obj["一本分数线","文科"].ptp()
ser_obj1=sorted_obj["一本分数线","理科"]
ser_obj2=sorted_obj["一本分数线","文科"]
ser_obj3=sorted_obj["二本分数线","理科"]
ser_obj4=sorted_obj["一本分数线","文科"]
print(ser_obj1)
print(ser_obj2)
print(ser_obj3)
print(ser_obj4)
