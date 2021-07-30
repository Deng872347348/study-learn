from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
import pandas as pd
#导入csv表
df=pd.read_csv(r"covid_19_data.csv",encoding='gbk')

df["extant"]=df["Confirmed"]-df["Deaths"]-df["Recovered"]

#建立映射表，与pyecharts调用接口保持一致
province_dict={"Anhui":"安徽",
"Beijing":"北京",
"Chongqing":"重庆",
"Fujian":"福建",
"Gansu":"甘肃",
"Guangdong":"广东",
"Guangxi":"广西",
"Guizhou":"贵州",
"Hainan":"海南",
"Hebei":"河北",
"Heilongjiang":"黑龙江",
"Henan":"河南",
"Hong Kong":"香港",
"Hubei":"湖北",
"Hunan":"湖南",
"Inner Mongolia":"内蒙古",
"Jiangsu":"江苏",
"Jiangxi":"江西",
"Jilin":"吉林",
"Liaoning":"辽宁",
"Macau":"澳门",
"Ningxia":"宁夏",
"Qinghai":"青海",
"Shaanxi":"陕西",
"Shandong":"山东",
"Shanghai":"上海",
"Shanxi":"山西",
"Sichuan":"四川",
"Taiwan":"台湾",
"Tianjin":"天津",
"Tibet":"西藏",
"Xinjiang":"新疆",
"Yunnan":"云南",
"Zhejiang":"浙江"}

#生成时间列表
date_list=list(df['ObservationDate'])
# ********* Begin *********#
p_list=[]
d_list=[]
for i in range(0, len(df)):
    #选择并添加2020年1月31日的满足映射表中的数据
    if date_list[i]=="01/31/2020" and df.iloc[i]['Province/State'] in province_dict.keys():
            p_list.append(province_dict[df.iloc[i]['Province/State']])
            d_list.append(df.iloc[i]['extant'])

c = (
  #设置地图的尺寸
  Map(init_opts=opts.InitOpts(width = '1000px', height='500px'))
  #添加绘制地图的数据及数据名称
  .add("新冠疫情现存确诊数据", [list(z) for z in zip(p_list, d_list)], "china")
  #设置地图名称及图例最大值
  .set_global_opts(
      title_opts=opts.TitleOpts(title="全国新冠疫情现存确诊数据地图"),
      visualmap_opts=opts.VisualMapOpts(max_=300),
  )
  #将地图渲染成HTML文件
  .render("studentanswer/level_1/base_map.html")
)
# ********* End *********#
