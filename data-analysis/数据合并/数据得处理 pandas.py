import pandas as pd
from pandas import MultiIndex
import numpy as np
df=pd.DataFrame({'A':['A0','A1','A2'],
                  'B': ['B0', 'B1','B2'],
                  },index=[0,1,2])
result=df.stack(level=-1,dropna=True)
print(df)
print(result)

# value=[("A教室",26),("A教室",30),("B教室",20),("B教室",25),("A教室",22),("A教室",24),("B教室",26),("B教室",22)]
# df12=pd.DataFrame({"男生人数":['26','30','20','25'],"女生人数":['22','24','26','22']},index=['A教室','B教室','A教室','B教室'])
# print(df12)

# df1=MultiIndex.from_tuples(tuples=df12,names=["一楼","二楼"])
# print(df1)

#任务二
#多层次创建索引
df=pd.DataFrame(np.random.randint(0,100,size=(2,4)),index=["男生人数","女生人数"],
                columns=pd.MultiIndex.from_product(iterables=[["一楼","二楼"],['A教室','B教室']]))
print(df)
print(df.stack(level=0))

#元组方式创建多层次索引
A =pd.DataFrame(np.random.randint(0,100,size=(2,4)),index=["男生人数","女生人数"],

             columns=pd.MultiIndex.from_tuples([("一楼","A教室"),("一楼","B教室"),("二楼","A教室"),("二楼","B教室")]))
print(A)
# df=pd.DataFrame(np.random.randint(0,100,size=(2,4)),index=["男生人数","女生人数"],
#                 columns=pd.MultiIndex.from_product(iterables=[["一楼","二楼"],["男生人数","女生人数"]]))


#任务三
# df1=pd.DataFrame([[(0,0),(0,1),(0,2)],[(1,0),(1,1),(1,2)]],index=[['r0','r0'],['r00','r01']],
#                  columns=pd.MultiIndex.from_arrays([['c0','c0','c1'],['c00','c01','c10']]))
# print(df1)
# print(df1.stack())
# print(df1.unstack())


#任务四
# df2=pd.DataFrame({"出售日期":['2017年5月25日','2017年5月25日','2017年5月25日',
#                                 '2017年6月18日','2017年6月18日','2017年6月18日'],
#                   "商品名称":["荣耀9青春版","小米6x","OPPO A1","荣耀9青春版","小米6x","OPPO A1"],
#                   "价格":[999,1399,1399,800,1200,1250]})
# print(df2)
#
#
df3=pd.DataFrame({'区域':['天心区','天心区','雨花区','雨花区','岳麓区','岳麓区'],
                 '门店': ['门店1', '门店2', '门店3', '门店4', '门店5', '门店6'],
                 '销售': [0.756858, 0.143079, 0.153846, 0.190877, 0.853948, 0.075344],
                 '人员数量': [0.617847, 0.719965, 0.447641, 0.528728, 0.802414, 0.689698]})


# df4=df3.pivot(columns={"销售":"1月份销售","人员数量":"1月份人员数量"},inplace=True)
df5=df3.rename(columns={"销售":"1月份销售","人员数量":"1月份人员数量"})
print(df5)
print(df3.rename(index={0:2}))

#任务六


# print(pd.cut(age,bins=[np.random.randint(0,100,size=(10))],right=False))


#任务7
# df=pd.DataFrame({'职业':['工人','学生','司机','教师','导游']}) #分类变量
# print(pd.get_dummies(df))

#任务8
# df=pd.DataFrame({'Key':['C','B','C','A','B','B','A','C','A'],
#                  'Data':[2,4,6,8,10,1,14,16,18]})
# print(df)
# print(df.groupby)
# print(type(df.groupby))
# print(df.groupby('Key'))
# for a,b in df.groupby('Key'):
#     print(a)
#     print(b)
#
# print(df.agg('Key'))

#任务9
# df=pd.DataFrame({'Key1':['A','A','B','B','A'],
#                  'Key2':['one','two','one','two','one'],
#                  'data1':[2,3,4,6,8],
#                  'data2':[3,5,6,3,7]})
# print(df)
#
# s=pd.Series(['a','a','c','b','c'])#修改为['a','a','b']
# group=df.groupby(s)
# for i,j in group:
#     print(i)
#     print(j)

#任务10
df=pd.DataFrame({'a':[1,2,3,4,5],
                  'b':[6,7,8,9,10],
                  'c':[11,12,13,14,15],
                  'd':[5,4,3,2,1],
                  'e':[10,9,8,7,6]})
print(df)
mapping={'a':'第一组','b':'第二组','e':'第三组','d':'第三组','e':'第二组'}
group=df.groupby(mapping)
for i,j in group:
    print(i)
    print(j)
#
#
#任务11
# df=pd.DataFrame({'a':[1,2,3,4,5],
#                   'b':[6,7,8,9,10],
#                   'c':[5,4,3,2,1]},
#                 index=['Sun','Jack','Alice','Helen','Job'])
# mapp={'a':'Sun','b':'Jack','e':'Alice','d':'Helen','e':'Job'}
# group=df.groupby(mapp)
# for i,j in group:
#     print(i)
#     print(j)



