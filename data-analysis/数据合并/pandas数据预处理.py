# -*- coding: utf-8 -*-
'''
第2关 数据清洗
'''
import pandas as pd
import numpy as np
d1 = pd.read_csv('data/economy-60-78.csv',index_col = 0)
d2 = pd.read_csv('data/economy-79-19.csv',index_col = 0)
d3 = pd.read_csv('data/population-60-78.csv',index_col = 0)
d4 = pd.read_csv('data/population-79-19.csv',index_col = 0)
d12 = pd.concat([d1,d2],axis = 1)
d34 = pd.concat([d3,d4],axis = 1)
ChinaData = pd.concat([d34,d12])

# 2.1 删除空白行
# 提示：dropna,inplace
############begin############
# print("原表形状 {}".format(ChinaData.shape))
#
# df=ChinaData.dropna(axis=0,how='all',inplace=False)
# print("新表形状 {}".format(df.shape))
# # print("+count(df)+")
# print("{}个空白行被删除。".format(len(ChinaData)-len(df)))
#############end#############

# 2.2 查找数据最完整（空值最少）的年份并输出
# 提示：notnull(),根据值找索引（上课讲过的方法）

# df1=pd.notnull(ChinaData).sum()
# df2=df1[df1.values==df1.max()].index
# print(df2[0])

#############end#############

# 2.3 前向填充"男性吸烟率（吸烟男性占所有成年人比例）"，输出2000年至2019年的数据
# fillna,ffill
############begin############

# df3=ChinaData.loc["男性吸烟率（吸烟男性占所有成年人比例）",'2000':'2019']
# df4=df3.fillna(axis=0,method='ffill')
# print(df4)

#############end#############

# 2.4 用2015年到2018年4年的gdp数据对2019年GDP数值进行拉格朗日插值预测，输出预测结果
# lagrange,
# 注意：x的取值从0开始，即x = np.array([0,1,2,3])，代表2015至2018 4年，2019年的x取值为4。
############begin############
# from scipy.interpolate import lagrange
# formula = ChinaData.loc['GDP','2015':'2018']
# print(lagrange(np.array([0,1,2,3]),formula.values)(4))


#############end#############

# 2.5 用线性插值法填充“入学率，高等院校，男生（占总人数的百分比）”1995年到2002年数据,并输出插值后的94年至03年的数据
# interp1d
############begin############
from scipy.interpolate import interp1d#1是数字一


# formula1 =ChinaData.loc['入学率，高等院校','男生（占总人数的百分比)','1994':'2003']
# print(formula1.interpolate())


# 3.1 对“人口，总数”数据（1960-2018）进行离差标准化，并输出。
# 提示：自定义离差标准化函数，注意统计年份区间
############begin############
# puplation=ChinaData.loc["人口，总数",'1960':'2018']
# a = 1 # 分为7个等宽区间
# # 等宽离散
# d1 = pd.cut(puplation, 2)
# print(d1)

x_max = ChinaData.loc["人口，总数",'1960':'2018'].max()
x_min = ChinaData.loc["人口，总数",'1960':'2018'].min()
x = (ChinaData.loc["人口，总数",'1960':'2018'] - x_min) / (x_max - x_min)
print(x)
#############end#############
# 2015    0.970631
# 2016    0.980796
# 2017    0.991350
# 2018    1.000000
# Name: 人口，总数, dtype: float64
# (5.994, 12.647]       37
# (12.647, 19.3]        11
# (-0.659, 5.994]        5
# (-7.311, -0.659]       4
# (-27.317, -20.617]     1
# (-13.964, -7.311]      0
# (-20.617, -13.964]     0

# 3.2 对“GDP 增长率（年百分比）”（1961-2018）数据进行等宽离散化为7类，输出分布情况
# 提示：cut，注意统计年份区间
############begin############
# puplation1=ChinaData.loc["GDP 增长率（年百分比）",'1961':'2018']
# k = 7 # 分为7个等宽区间
# # 等宽离散
# d1 = pd.cut(puplation1, k)
# print(d1.value_counts())








