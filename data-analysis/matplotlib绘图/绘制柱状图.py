import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pylab import mpl

#自定义配置文件和绘图风格
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#######################绘图步骤###########################
# 0、读数据
data=pd.read_excel("学校上课数据分析代码\matplotlib绘图\data\交通数据.xlsx",sheet_name='建国以来公路建设情况')


# 1、创建画布，画布大小10*6、dpi为100
f=plt.figure(figsize=(10,6),dpi=100)
# 2、绘制柱状图，以年份为横坐标，对应的公路里程为纵坐标，绘制建国以来公路建设情况柱状图
#要求：柱宽0.75，颜色red

x_data = np.arange(1,16)
#取出读取的数据里面公路里程这一行数据，作为Y轴
y_data = data['公路里程']

#使用bar函数把x,y轴1填充好
plt.bar(x_data,y_data,width=0.75,color='red')
#使用for循环,zip打包函数
for x,y in zip(x_data,y_data):
    plt.text(x,y,y,ha='center')

#3、添加标签。x轴刻度:数据源中各年份数据，x轴名称:年份，y轴名称:公路总里程，图例:公路总里程(万公里)，标题:建国以来我国公路里程变化柱状图
plt.title('建国以来我国公路里程变化柱状图')
plt.xlabel('年份')
plt.ylabel('公路总里程')
plt.xticks(x_data,data['年份'],rotation=45)
plt.legend(['公路总里程(万公里)'])

#4、保存和显示图表，保存为png图片，保存路径resultpng/result.png
plt.savefig('resultpng/result.png')
plt.show()

#######################Begin############################
# 0、读数据
data=pd.read_excel("学校上课数据分析代码\matplotlib绘图\data\交通数据.xlsx",sheet_name='建国以来公路建设情况')