import pyecharts.options as opts
from pyecharts.charts import Line
week_name_list = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
high_temperature = [11, 11, 15, 13, 12, 13, 10]
low_temperature = [1, -2, 2, 5, 3, 2, 0]
line=(
    Line()
    .add_xaxis(xaxis_data=week_name_list)
    .add_yaxis(series_name="最高温度",y_axis=high_temperature,symbol="arrow",is_symbol_show=True)
    .add_yaxis(series_name="最低气温",y_axis=low_temperature)
    .set_global_opts(title_opts=opts.TitleOpts(title="未来一个星期的气温变化"))
)
line.render_notebook()