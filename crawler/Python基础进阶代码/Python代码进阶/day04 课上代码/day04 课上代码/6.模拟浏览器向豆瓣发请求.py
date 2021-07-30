import requests

# 豆瓣发请求，豆瓣返回内容：字符串
#   - 浏览器可以
#   - 代码不可以
# 豆瓣会识别，你到底人？还是机器？
res = requests.get(
    url="https://www.douban.com/group/topic/79870081/",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
    }
)
print(res.text)


# 获取文本信息后，提取里面的邮箱
"""
     - 正则
     - 模块
"""