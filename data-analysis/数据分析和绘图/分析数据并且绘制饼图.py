
#********** Begin **********#
#1.导入基础包
import numpy as np
import pandas as pd
import matplotlib
#强制matplotlib不使用任何Xwindows后端（X Window图形用户接口）
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import re
# 防止中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'

#2.导入文档数据
path = r'step2/'
filePath = path+r'positions.csv'
display_column = ["edu"]
# step2\positions.csv
# 从xls表格文件中加载(`notebook`默认是`utf-8`编码，如果文件中的的中文是用`gbk`编码，要在这里声明编码方式，如：`encoding='gbk'`)
df=pd.read_csv(filePath,encoding='gbk')
# 重新设置列的顺序
df = df.reindex(columns=display_column)
#********** End **********#
d5 = df.head()
print(d5)  #显示前5行数据
#3.分析数据
# df = pd.read_excel(filePath)
# df = df.reindex(columns=display_column)
# display(df)
dd=df['edu'].value_counts()
print(dd)
# X = list(df['food'])       #列出食物名
# Y = list(df['morning'])    #列出早上每样菜的点菜数量
# sum = df['morning'].sum()  #求出早上‘morning’点菜的总数
# fig,ax = plt.subplots()    #plt.subplots() 返回一个 Figure实例fig 和一个 AxesSubplot实例ax 。fig代表整个图像，ax代表坐标轴和画的图。这条命令可以用来设置画多个图，然而这里我们只画一个，所以括号里不用做设置
# ax.pie(Y/sum,autopct='%1.1f%%',labels=X)  #参数（每一块的比例；控制饼图内百分比设置 '%1.1f'指小数点前后位数(没有用空格补齐)；每一块饼图外侧显示的说明文字）
# fig.set_size_inches(7,7)                  #设置圆的大小，如果两个数字不相等会变成椭圆
# #********** End **********#
# plt.savefig(path+r'/yourimg/'+r'pie.png') #存储图片