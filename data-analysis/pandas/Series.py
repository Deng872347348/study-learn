import pandas as pd
import  numpy as np


df=pd.read_excel('E:\\python社区版\\python项目\\学校上课数据分析代码\\3-11\data\\朝阳区药品销售数据.xlsx',header=0)

pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', None) # 设置打印宽度(**重要**)
# 任务26
# df["日销售金额"]=df.loc[:,"销售数量"]*df.loc[:,"实收金额"]
# print(df)
# 任务27
# df['被删除的应收金额']=df.drop(labels='应收金额',axis=1,inplace=True)
# print(df)
# df['被删除的应收金额']=df.drop(labels=2,axis=0,inplace=True)
# print(df)
#任务28
# print(df.dtypes)
# df.loc[:,'社保卡']=df.loc[:,'社保卡号'].astype('float32')
# print(df.dtypes)
#任务29
# 修改列名
# df.rename(columns={'销售时间':'销售时间'},inplace=True)
# print(df)
#任务30
#修改索引，将购药时间改为索引
# df.set_index(keys='购药时间',inplace=True)
# print(df)

#任务31
#修改索引，重置索引
# df.reset_index(inplace=True)
# print(df)

#任务32
# 将Series对象重新索引
# se1=pd.Series([1,7,3,9],index=['d','c','a','f'])
# print(se1)
# se2=se1.reindex(['a','b','c','d','e','f'])
# print(se2)
#任务33
# se3=pd.Series(['blue','red','black'],index=[0,2,4])
# se4=se3.reindex(range(6),method='ffill')
# print(se4)

#任务34
#实现层次化索引，最常见的构造方法就是在index参数中传入一个嵌套列表
mulitindex_series=pd.Series([15848,13472,12073.8,7813,7446,6444,15230,8269],index=[['河北省','河北省','河北省','河北省','河南省','河南省','河南省','河南省'],
        ['石家庄市','唐山市','邯郸市','秦皇岛','郑州市','开封市','洛阳市','新乡市']])
mulitindex_series = pd.Series([15848,13472,12073.8,7813,7446,6444,15230,8269],
                        index=[['河北省','河北省','河北省','河北省',
                                '河南省','河南省','河南省','河南省'],
                               ['石家庄市','唐山市','邯郸市','秦皇岛市','郑州市','开封市','洛阳市','新乡市']])
print(mulitindex_series)

#任务35
# mulitindex_series = pd.DataFrame([15848,13472,12073.8,7813,7446,6444,15230,8269],
#                         index=[['河北省','河北省','河北省','河北省',
#                                 '河南省','河南省','河南省','河南省'],
#                                ['石家庄市','唐山市','邯郸市','秦皇岛市','郑州市','开封市','洛阳市','新乡市']],columns=['占地运动'])
# print(mulitindex_series)

#任务36
# df4=pd.DataFrame({"year":[2001,2001,2002,2002,2003],"fruit":["apple","banana","apple","banana","apple"],
#                   "production":[2345,5632,3245,6432,4532],
#                   "profits":[245.6,432.7,534.1,354,467.8]})
#
# print(df4)
# print("========层次索引==========")
# df4=df4.set_index(['year','fruit'])
# print(df4)
#任务37
#创建层次化索引
list_tuples=[('A','A'),('A','A2'),('B','B'),('B','B2'),('B','B3')]
multi_index=pd.MultiIndex.from_tuples(tuples=list_tuples,names=['外层索引','内层索引'])
print(multi_index)
# #任务38
#
# multi_array = pd.MultiIndex.from_arrays(arrays=[['A','A','B','B','B'],
#                                         ['A1','A2','B1','B2','B3']],
#                                         names=['外层索引','内层索引'])
# print(multi_array)

#
# data=pd.DataFrame(np.arange(15).reshape(5,3),index=multi_array)
# print(data)

#任务39
# from_product()方法表示从多个集合的笛卡尔乘积
# numbers=[0,1,2]
# colors=['green','purple']
# multi_product=pd.MultiIndex.from_product(iterables=[numbers,colors],names=['number','color'])
# print(multi_product)