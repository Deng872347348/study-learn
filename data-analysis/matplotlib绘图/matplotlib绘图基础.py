import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
#自定义一个文件和绘制图片风格
# mpl.rcParams['font.sans-serif']=['SimHei']
# mpl.rcParams['axes.unicode_minus']=False
#
# #数据的读取
# data=pd.read_excel("data/交通数据.xlsx",sheet_name='铁路公路建设情况')
# #确定x,y轴
# data_x=data['年份']
# #确定y轴
# data_y=data['公路密度']
# plt.figure(figsize=(10,6),dpi=100)
# plt.bar(data_x,data_y,width=0.75)
# #使用zip打包函数
# plt.plot(data_x,data_y,color="red",linewidth=1.5,linestyle='-',label='Jolon income', marker='*')
# for x,y in zip(data_x,data_y):
#     plt.text(x,y,"%.1f"%y,ha="center",fontsize=10)
# #添加标签
# plt.title("2001-2019年我国公路密度变化柱状图")
# #x轴的标签
# plt.xlabel("年份")
# #y轴的标签
# plt.ylabel("公路密度")
#
# plt.xticks(data_x)
#
# plt.legend("公里密度程(公里/百平方公里)")
#
# #4、保存和显示图表，保存为png图片，保存路径resultpng/result.png
# plt.savefig('data/result1.png')
# plt.show()

#创建多子图
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#数据的读取
data=pd.read_excel("data/交通数据.xlsx",sheet_name='铁路公路建设情况')
#确定x,y轴
data_x=data['年份']
#确定y轴
data_y1=data["公路总里程"]
data_y2=data['公路密度']

#创建画布
plt.figure(figsize=(10,6),dpi=100)
#创建多子图
ax1=plt.subplot(2,2,1)
ax1.bar(data_x,data_y1,width=0.75,color="red")
# for x,y in zip(data_x,data_y1):
#     plt.text(x,y,"%.1f"%y,ha="center",fontsize=10)
ax1.set_title("2001-2019年我国公路里程变化柱状图")
#x轴的标签
ax1.set_xlabel("年份")
#y轴的标签
ax1.set_ylabel("公路密度")

ax1.set_xticks(data_x)
ax1.set_xticklabels(data_x,fontsize=8,rotation=45)#画刻度的标签
ax1.legend("公路总里程(万公里)")

#创建第二个
ax2=plt.subplot(2,2,2)
ax2.bar(data_x,data_y2,width=0.75)
ax2.plot(data_x,data_y2,color="red",linewidth=1.5,linestyle='-',label='Jolon income', marker='*')
# for x,y in zip(data_x,data_y2):
#     plt.text(x,y,"%.1f"%y,ha="center",fontsize=10)
ax2.set_title("2001-2019年我国公路密度变化柱状图")
#x轴的标签
ax2.set_xlabel("年份")
#y轴的标签
ax2.set_ylabel("公路密度")

ax2.set_xticks(data_x)
# ax2.set_xticklabels(data_x,fontsize=8,rotation=45)#画刻度的标签
ax2.legend("公里密度程(公里/百平方公里)")
# ax2=plt.subplot(2,2,2)  #一行两列
# ax2.plot(data_x,data_y2,color='yellow',marker='.')
# #利用循环和text方法添加柱高标签
# for x,y in zip(data_x,data_y2):
#     plt.text(x,y,"%.1f"%y,ha='center',fontsize=6)
# #添加标签
# ax2.set_title('2001-2019年我国公路密度变化折线图')
# ax2.set_xlabel('年份')
# ax2.set_ylabel('公路密度')
# ax2.set_xticks(data_x)
# ax2.set_xticklabels(data_x,fontsize=8,rotation=45)
# ax2.legend(['公路密度(公里/百平方公里)'])


ax3=plt.subplot(2,1,2)  #一行两列
ax3.plot(data_x,data_y2,color='yellow',marker='.')
#利用循环和text方法添加柱高标签
for x,y in zip(data_x,data_y2):
    plt.text(x,y,"%.1f"%y,ha='center',fontsize=6)
#添加标签
ax3.set_title('2001-2019年我国公路密度变化折线图')
ax3.set_xlabel('年份')
ax3.set_ylabel('公路密度')
ax3.set_xticks(data_x)
ax3.set_xticklabels(data_x,fontsize=8,rotation=45)
ax3.legend(['公路密度(公里/百平方公里)'])


# ax3=plt.subplot(2,3,1)
# ax3.bar(data_x,data_y1,width=0.75)
# # for x,y in zip(data_x,data_y1):
# #     plt.text(x,y,"%.1f"%y,ha="center",fontsize=10)
# ax3.set_title("2001-2019年我国公路里程变化柱状图")
# #x轴的标签
# ax3.set_xlabel("年份")
# #y轴的标签
# ax3.set_ylabel("公路密度")
#
# ax3.set_xticks(data_x)
# ax3.set_xticklabels(data_x,fontsize=8,rotation=45)#画刻度的标签
# ax3.legend("公路总里程(万公里)")
plt.show()
