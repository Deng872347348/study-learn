import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightStyle as LS
#执行API调用并储存响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code)

#将API响应储存在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#探索有关仓库的信息
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
#可视化
my_style = LS(base_style=LCS)

my_config = pygal.Config()
my_config.x_labels_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config .show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, sytle=my_style)
chart.title = 'Most_starred Python Projects on Github'
chart.x_labels = names
#处理结果
chart.add('', stars)
chart.render_to_file('python_repos.svg')