import requests
import jsonpath
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
}


response = requests.get('http://www.lagou.com/lbs/getAllCitySearchLabels.json',headers=headers)

dict_data = json.loads(response.content) # json.loads 打印字典的时候 json数据自动按Unicode存储

# print(dict_data)
citylist = jsonpath.jsonpath(dict_data,"$..name")

# 写入文件
with open('city_name.txt','w') as f:
    content = json.dumps(citylist,ensure_ascii=False)
    f.write(content)