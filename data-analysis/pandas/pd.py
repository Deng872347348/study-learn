import pandas as pd
# #任务点一：
# ser_obj_1=pd.Series([1,2,3,4,5])
# # print(ser_obj_1)
# #任务点二
# ser_obj=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# # print(ser_obj)
# year_data={2001:17.8,2002:20.1,2003:16.5}
# ser_obj_2=pd.Series(year_data)
# print(ser_obj_2)
#
# df=pd.DataFrame([1,2],[2,4])
# print('index:',df.index)
# print('index name:',df.index.name)
# print('columns dtype:',df.columns.dtype)

#任务三
# import pandas as pd
# import  numpy as np
# num_abc=pd.Series(np.random.randn(5),index=list('abcde'))
# num=pd.Series(np.random.randn(5))
#
# print(num)
# print(num_abc)

#任务四
# ser_obj=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
# print(ser_obj.index)
# print(ser_obj.values)
# print(type(ser_obj.values))

# 任务五
# data=pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
# print(data['b'])

#任务6
# data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
# print(data['a':'c'])

#任务7：
# import pandas as pd
import numpy as np
# s=pd.Series([9,'zheng','beijing',128,'usa',990],index=[1,2,3,'e','f','g'])
# print(s[1:3])
# print(s[[1,3]])
# print(s[:-1])

# 任务8
# classes=['语文','数学','英语','体育','数学']
# socre=[98,95,90,92,100]
# ser=pd.Series(socre,index=classes)
# math=ser['数学'].values
# print(math)
# print(ser[['数学','体育']])
# print(ser[[1,3,4]])

# 任务9
data=pd.read_excel('E:\\python社区版\\python项目\\学校上课数据分析代码\\3-11\data\\朝阳区药品销售数据.xlsx',header=0)
# print(data)
df=pd.DataFrame(data)
# print(df.shape)
#任务10
# print(df.index)
#任务11
# print(df.columns)

#任务12
# print(df.count())
#任务13
# print(df.head())
#任务14
# print(df.tail())

#任务15
# print(df['商品名称'])
#任务16
# print(df[['商品名称','销售数量']])

#任务17
# print(df[0:3])
# print(df.head(3))
#任务18
# print(df.loc[:,'购药时间'])
 #任务19
# print(df.loc[0:2,'购药时间'])
 #任务20
# print(df.loc[0:2,['购药时间','商品名称']])

#任务21
# print(df.iloc[:,0])
#任务22
# print(df.iloc[0:3,0])
#任务23
# print(df.iloc[0:3,[0,1]])

#任务24
# print(data.loc[data['商品名称']=='三九感冒灵',:])
#/
# print(df)
# dict1={"商品编码":['236701','236701','236701'],
#        "商品名称":['强力VC银翘片','清热解毒口服液','感康'],
#        "商品数量":[6,1,2]}
# df=pd.DataFrame(dict1)
# print(df)
# dict1={"商品编码":pd.Series(['236701','236701','236701']),
#        "商品名称":pd.Series(['强力VC银翘片','清热解毒口服液','感康']),
#        "商品数量":pd.Series([6,1,2])}
# df=pd.DataFrame(dict1)
# print(df)