import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import mpl
#自定义一个文件和绘制图片风格
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#数据的读取
data=pd.read_excel("data/交通数据.xlsx",sheet_name='铁路公路建设情况')
#确定x,y轴
data_x=data['年份']
#确定y轴
data_y=data['公路总里程']

plt.figure(figsize=(10,6),dpi=100)

plt.bar(data_x,data_y,width=0.75)
#使用zip打包函数
for x,y in zip(data_x,data_y):
    plt.text(x,y,"%.1f"%y,ha="center",fontsize=10)
#添加标签
plt.title("2001-2019年我国公路里程变化柱状图")
#x轴的标签
plt.xlabel("年份")
#y轴的标签
plt.ylabel("公路里程")

plt.xticks(data_x)

plt.legend("公里总里程(万公里)")

#4、保存和显示图表，保存为png图片，保存路径resultpng/result.png
plt.savefig('data/result.png')
plt.show()
