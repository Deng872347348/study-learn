import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
#自定义一个文件和绘制图片风格
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#数据的读取
data=pd.read_excel("data/交通数据.xlsx",sheet_name='铁路公路建设情况')
#确定x,y轴
data_x=data['年份']
#确定y轴
data_y1=data["公路总里程"]
data_y2=data['公路密度']

#创建figure
f=plt.figure(figsize=(10,6),dpi=100)

#绘柱状图
plt.bar(data_x,data_y1,width=0.75,color=sns.color_palette("Greens",19))
for x,y in zip(data_x,data_y1):
    plt.text(x,y,"%.1f"%y,ha='center',fontsize=6)
plt.ylabel("公路里程")
plt.twinx()
#绘制折线图
plt.plot(data_x,data_y2,color="red",linewidth=1.5,linestyle='-',label='Jolon income', marker='>')
for x,y in zip(data_x,data_y2):
    plt.text(x,y-2,"%.1f"%y,ha='center',fontsize=6)
#添加标签
plt.title("2001-2019年公路建设情况")
plt.xlabel("年份")
plt.ylabel("公路密度")
plt.xticks(data_x,rotation=45)
f=plt.legend(["公路里程(万公里)","公路密度(公里/百平方公里)"])
# plt.legend(["公路密度(公里/百平方公里)", "公路里程(万公里)"])
#展示图片
plt.show()
