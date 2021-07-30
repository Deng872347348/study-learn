#任务40
import pandas as pd
import  numpy as np
# student=["张三"]
# ss=pd.Series(["张三","张三","张三","李四","李四","李四","王五"])

#
# df4=[("张三","期末"),("张三","期中"),("王五","期末"),("王五","期中"),("李四","期末"),("李四","期中")]
# multi_index=pd.MultiIndex.from_tuples(tuples=df4)
# print(multi_index)
# df2=pd.DataFrame(np.random.randint(100,size=(6,3)),
#                  index=multi_index,columns=['python','java','php'])
# print(df2)
# print(df2['python']['张三']['期中'])
# print(df2['张三']['期中']['python'])


# aa=pd.DataFrame(np.random.randint(100,size=(6,3)))
# print(aa)
# ss=pd.Series([aa],index=[["张三","张三","王五","王五","李四","李四"],["期末","期中","期末","期中","期末","期中"]])
# print(ss)
# print(df2['python']['张三']['期末'])
# print(type(df2['python']['张三']['期末']))
# print(df2.loc['张三'].loc['期末'])
# print(type(df2.loc['张三'].loc['期末']))
# mulitindex_series = pd.Series([15848,13472,12073.8,7813,7446,6444,15230,8269],
#                         index=[['河北省','河北省','河北省','河北省',
#                                 '河南省','河南省','河南省','河南省'],
#                                ['石家庄市','唐山市','邯郸市','秦皇岛市','郑州市','开封市','洛阳市','新乡市']])
# print(mulitindex_series)
# name=["张三","李四","王五"]
# num=["期末","期中"]
# df2=pd.DataFrame(np.random.randint(100,size=(6,3)),
#                  index=pd.MultiIndex.from_product(iterables=[name,num]),columns=['python','java','php'])
# print(df2)
# print(df2[['python','java']].loc['张三'])
# print(df2[['python','java']].loc['张三':'王五',:])
# print(df2.loc[:,"python":'java'])
# pd.MultiIndex.from_product(iterables=[numbers,colors],names=['number','color'])
# list_tuples=[('A','A'),('A','A2'),('B','B'),('B','B2'),('B','B3')]
# multi_index=pd.MultiIndex.from_tuples(tuples=list_tuples,names=['外层索引','内层索引'])
# print(multi_index)
# mulitindex_series = pd.DataFrame([15848,13472,12073.8,7813,7446,6444,15230,8269],
#                         index=[['河北省','河北省','河北省','河北省',
#                                 '河南省','河南省','河南省','河南省'],
#                                ['石家庄市','唐山市','邯郸市','秦皇岛市','郑州市','开封市','洛阳市','新乡市']],columns=['占地运动'])
# print(mulitindex_series)
# name=['python','java','php']
# ss=['期末','期中']
# df2=pd.DataFrame(np.random.randint(0,150,size=(6,6)),index=['A','B','C','D','E','F'],
#                  columns=pd.MultiIndex.from_product(iterables=[name,ss],names=['name','ss']))
# print(df2)

# data1=pd.DataFrame(np.random.randint(0,150,size=(6,6)),index=['A','B','C','D','E','F'],
#                   columns=pd.MultiIndex.from_product([['python','cn','math'],['期中','期末']]))
#
# print(data1)
# print(data1['python'])
# print(data1['python','期末']['A':'C'])
# print(data1['A':'C']['python','期末'])

# df2=pd.DataFrame(np.random.randint(0,150,size=(6,6)),index=['A','B','C','D','E','F'],
#                  columns=pd.MultiIndex.from_product([['python','java','php'],['期末','期中']]))
# print(df2)
# multi_product=pd.MultiIndex.from_product(iterables=[numbers,colors],names=['number','color'])