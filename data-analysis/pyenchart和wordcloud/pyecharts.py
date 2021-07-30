from pyecharts.charts import Line
from pyecharts.charts import opts
line=(
    Line(init_opts=opts.InitOpt(theme=ThemeType.WESTEROS))
    .add_xaxis(['衬衫','羊毛衫','裤子','高跟鞋','袜子','雪纺衫'])
    .add_yaxis("商家A",[5,20,36,10,75,90])
    .add_yaxis('商家B',[15,6,45,20,35,66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题",subtitle="副标题"))
)
line.render_notebook()
