import pandas as pd
import  numpy as np
from numpy import NaN

#任务一:
# obj=pd.Series([1,None,np.NAN])
# print(pd.isnull(obj))
# print(pd.isnull(obj).sum())
# print(type(pd.isnull(obj)))
# print(pd.notnull(obj))
#任务二:
# novel=pd.DataFrame({'类别':['小时','散文随笔','青春文学','传记'],
# '书名':[np.NaN,'《皮囊》','《旅游结束时》','《老舍自传》'],
# '作者':['老舍',None,'张共鑫','老舍']})
# print(pd.notnull(novel).sum())
# print(novel)
#
# print(novel.dropna())
# print(novel.dropna(axis=1))
# print(novel.dropna(axis=0))
# print(novel.dropna(thresh=1))
# print(novel.dropna(how='all'))
# print(novel.dropna(axis=0,subset=['书名','类别']))#删除行
# print(novel.dropna(axis=1,subset=[0,3]))#删除列
# print(pd.isnull(novel))
# print(pd.isnull(novel).sum())
# print(pd.notnull(novel).sum())

# print(novel.duplicated())


#任务三
# df_obj=pd.DataFrame({'A':[1,2,3,NaN],'B':[NaN,4,NaN,6],'C':['a',7,8,9],'D':[NaN,2,3,NaN]})
# print(df_obj)
# print(df_obj.fillna({'A':4.0,'B':5.0}))
# print(df_obj.fillna('66.0'))
# #向前填充数据
# print(df_obj.fillna(method='ffill'))
#
# print("纵向用缺失值替换缺少值")
# print(df_obj.fillna(axis=0,method='ffill'))
# print("3.用标量常数替换缺失值")
# print(df_obj.fillna(value=66))
# print("4。limit参数")
# print(df_obj.fillna(method='bfill',axis=1,))
# print("用字典实现缺少值替换")
# print(df_obj.fillna({'A':10,'B':20,'C':30,'D':40}))
# s=pd.DataFrame(np.arange(12).reshape(4,3),columns=list('ABC'))
# print(s)
# print(df_obj.fillna(s))
#
# print('7,用Series实现缺少值替换')
# a=pd.Series([np.nan,2,3,np.nan])
# print(a.fillna(pd.Series(np.arange(4))))
# print(df_obj.fillna(pd.Series(np.arange(4))))


#任务四:
# person_info=pd.DataFrame({'id':[1,2,3,4,4,5],'name':['小铭','小月月','彭岩','刘华','刘华','周华'],'age':[18,18,29,58,58,36],'height':[180,180,185,175,175,178],
#                           'gender':['女','女','男','男','男','男']})
# print(person_info.duplicated())
# print("3\ subset 、keep('first'/'last/False)")#参数
# print(person_info.drop_duplicates(subset=['name','age'],keep='first'))
#
# file_path=open('链家北京租房数据.csv')
# file_data=pd.read_csv(file_path)
# # print(file_data)
#
# #重复值和空值处理
# print(file_data.duplicated())
# print(file_data.notnull)
#
# print(file_data.isnull)
# print('========去空值=====')
# print(file_data.duplicated())
# print('============是空值的统计===========')
# print(file_data.isnull().sum())
# print('==============不是空值的统计===============')
# print(file_data.notnull().sum())
# print('============去重复值=============')
# print(file_data.drop_duplicates().sum())
#
# #数据类型转化
# data=file_data['面积(㎡)'].values#5773个面积
# print(data)
# print(file_data['面积(㎡)'])
# new_data=[]
# for i in data:
#     new_data.append(i[:-2:])
# print(new_data)
# file_data['面积(㎡)']=new_data
# file_data['面积(㎡)']=file_data['面积(㎡)'].astype('float64')
# print(file_data.dtypes)
# print(file_data['面积(㎡)'].values)
# data1=file_data['户型'].values
# print(data1)
# new_data1=[]
# for i in data1:
#     new=i.replace('房间','室')
#     new_data1.append(new)
# print(new_data1)
# print(type(new_data1))
# def three_sigma(ser1):
#     #求平均值、标准差
#     mean_value=ser1.mean()
#     std_value=ser1.std()
#     #ser1对象每个数据进行条件判断运算，结果rule依然是一个Series对象
#     rule=(mean_value-3*std_value>ser1)| (ser1>mean_value+3*std_value)
#     #print(rule)
#     index=np.arange(ser1.shape[0])[rule]      #布尔索引
#     #index=ser1.index[rule]
#     outrange=ser1[index]
#     return outrange
# data=pd.read_csv('example_data.csv')
# print(data)
# print('A列异常值：',three_sigma(data['A']))
# print('B列异常值：',three_sigma(data['B']))

# import pandas as pd
# df=pd.DataFrame({'A':[1,2,3,4],'B':[2,3,5,2],'C':[1,4,7,4],'D':[1,5,30,3]})
# df.boxplot(column=['A','B','C','D'])





