from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
import seaborn as sns
#自定义一个文件和绘制图片风格
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
#数据的读取
data=pd.read_excel("E:\python社区版\python项目\学校上课数据分析代码\matplotlib绘图\data\交通数据(1).xlsx",sheet_name='运输服务')
data=data.set_index("年份")
xdata=data.loc[2001][::2]
labels=data.columns[::2]
data_pair=[list(z) for z in zip(labels,xdata)]
init_opts = opts.InitOpts(page_title="2001年各交通运输行业客运量占比图",width="600px",height="300px")
pie = Pie(init_opts=init_opts)
pie.add(
   series_name="",data_pair=data_pair
)
# pie.render(path="Bing1.html")
pie.render_notebook()

pie.set_global_opts(title_opts=opts.TitleOpts(title="2001年各交通运输行业客运量占比图"),legend_opts=opts.LegendOpts(pos_bottom=200,pos_top=100))


