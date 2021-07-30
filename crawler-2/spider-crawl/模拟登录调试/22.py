import requests
import play_audio

# 天气播报方式
zh_to_en = {
    "温度": "temperature",
    "湿度": "humidity",
    "天气": "info",
    "风向": "direct",
    "风力": "power",
    "空气质量指数": "aqi"
}

# 提取出方便python进行处理的数据  dict
response = requests.get(
    # 回家是不是需要选择一个路线,到家是不是要钥匙开门
    url="http://apis.juhe.cn/simpleWeather/query",
    params={
        "city": "长沙",
        "key": "79f5c61eac3185e23ef675b454036e10"
    }
).json()

import pprint
pprint.pprint(response)

result = response["result"]["realtime"]

output_str = "长沙当前天气情况,\n"
# 音频转换  获取数据 => 筛选数据(字典) => 字符串（根据使用的工具） => 音频

# print(zh_to_en.items())
# 基本语法  requests爬虫  讲大纲
for key, value in zh_to_en.items():
    # print(key, value)
    output_str += (key + ":" + result[value] + ",\n")

play_audio.play(output_str)