import pandas as pd
import numpy as np
# 设置输出格式：这两个参数的默认设置都是False
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', None)  # 设置打印宽度(**重要**)
#任务1
# df1=pd.DataFrame({'A':['A0','A1','A2'],
#                   'C': ['C0', 'C1', 'C2']})
# df2=pd.DataFrame({'B': ['B3', 'B4', 'B5'],
#                   'C': ['C3', 'C4', 'C5'],
#                   'D': ['D3', 'D4', 'D5']})
# print(df1)
# print(df2)
# df3=pd.concat([df1,df2],axis=0,join='outer')
# df4=pd.concat([df1,df2],axis=0,join='inner')
# print(df3)
# print(df4)


#任务2
# df1=pd.DataFrame({'A':['A1','A2','A3','A4'],
#                   'B': ['B1', 'B2','B3','B4'],
#                   'C': ['C1', 'C2', 'C3','C4'],
#                   'D': ['D1', 'D2', 'D3', 'D4']},index=[1,2,3,4])
# df2=pd.DataFrame({'B': ['B2', 'B4', 'B6', 'B8'],
#                   'D': ['D2', 'D4', 'D6', 'D8'],
#                   'F': ['F2', 'F4', 'F6', 'F8']},index=[2,4,6,8])
# print(df1,'\n',df2)
# print(pd.concat([df1,df2],axis=0,join='outer',sort=True))
# print(pd.concat([df1,df2],axis=0,join='inner',sort=True))
#
# print("新表的形状{}".format(df2.shape))



#任务3
# data=pd.read_excel('超市营业额.xlsx',sheet_name='Sheet1')
# data1=pd.read_excel('超市营业额.xlsx',sheet_name='Sheet2')
# data2=pd.read_excel('超市营业额.xlsx',sheet_name='Sheet3')
# df=data[:3]
# df1=data2[50:54]
# print(pd.concat([data[:3],data[50:54],data1],axis=0,join="outer",sort=True))

# 任务4：针对行数据，主键合并
# left=pd.DataFrame({'A':['A1','A2','A3','A4'],
#                    'B': ['B1', 'B2', 'B3','B4'],
#                    'Key': ['K1', 'K2', 'K3','K4']},index=[1,2,3,4])
# print(left)
# right=pd.DataFrame({'C':['C1','C2','C3','C4'],
#                    'D': ['D1', 'D2', 'D3','D4'],
#                    'Key': ['K2', 'K1', 'K3','K4']},index=[1,2,3,4])
# print(right)
# df2=pd.merge(left,right,how='outer')
# print(df2)
# print(pd.merge(left,right,how="inner"))




#任务5
left=pd.DataFrame({'Key': ['K0', 'K1', 'K2'],
                   'A':['A0','A1','A2'],
                   'B': ['B0', 'B1', 'B2']
                   })
print(left)
right=pd.DataFrame({'Key': ['K0', 'K1', 'K2','K3'],
                    'B': ['B0', 'B1', 'B2','B3'],
                    'C':['C0','C1','C2','C3'],
                   'D': ['D0', 'D1', 'D2','D3']
                   })
print(right)
print(pd.merge(left,right,how='left'))
print(pd.merge(left,right,how='right'))
print(pd.merge(left,right,how='outer'))


# left=pd.DataFrame({'A':['A1','A2','A3','A4'],
#                    'B': ['B1', 'B2', 'B3','B4'],
#                    'K': ['K1', 'K2', 'K3','K4']})
# right=pd.DataFrame({'C':['C1','C2','C3','C4'],
#                    'D': ['D1', 'D2', 'D3','D4'],
#                    'K': ['K1', 'K2', 'K3','K4']})
#
#
# print(pd.merge(left,right,how='left'))
# print(pd.merge(left,right,how='right'))
# print(pd.merge(left,right,how='outer'))

#任务6
# df1=pd.read_excel('超市营业额.xlsx',sheet_name='Sheet1')
# print(df1)
# df2=pd.read_excel('超市营业额.xlsx',sheet_name='Sheet3')
# print(df2)
# print(pd.merge(df1,df2,how='right'))
# print(pd.merge(df1,df2,how='left'))
# print(pd.merge(df1,df2,how='outer'))
# #任务7
# left=pd.DataFrame({'userid':['a','b','c','d'],
#                    'age':[23,46,32,19]})
# right=pd.DataFrame([['a',2000],['c',3500]],columns=['userid','payment'])
# print(left,'\n',right)

#任务7
# left=pd.DataFrame({'userid':['a','b','c','d'],
#                    'age':[23,46,32,19]})
# right=pd.DataFrame([['a',2000],['c',3500]],columns=['userid','payment'])
# print(left,'\n',right)
# print(pd.merge(left,right,how='right'))
# print(pd.merge(left,right,how='left'))
# print(pd.merge(left,right,how='outer'))
# print(pd.merge(right,left,how='inner'))

#任务8
# left=pd.DataFrame({'userid':['a','b','c','d'],
#                    'age':[23,46,32,19]})
# right=pd.DataFrame([['a',2000],['c',3500],['a',500],['b',1000]],columns=['userid','payment'])
# print(left,'\n',right)
# print(pd.merge(left,right,how='left'))
# print(pd.merge(left,right,how='inner'))
# print(pd.merge(left,right,how='outer'))

#任务9
# left=pd.DataFrame({'userid':['a','b','c','d'],
#                    'age':[23,46,32,19]})
# right=pd.DataFrame([['a',2000],['c',3500],['e',600]],columns=['userid','payment'])
# print(left,'\n',right)
# print(pd.merge(left,right,how='left'))
# print(pd.merge(left,right,how='inner'))
# print(pd.merge(left,right,how='outer'))

#任务10
left=pd.DataFrame({'userid':['a','b','c','d'],
                   'age':[23,46,32,19]})
right=pd.DataFrame([['a',2000],['c',3500],['e',600]],columns=['userid','payment'])
print(left,'\n',right)
print(pd.merge(left,right,how='left'))
print(pd.merge(left,right,how='inner'))
print(pd.merge(left,right,how='outer'))



