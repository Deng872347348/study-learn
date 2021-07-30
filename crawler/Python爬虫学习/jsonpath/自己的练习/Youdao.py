import requests
import json


class Youdao(object):

    def __init__(self, word):
        self.url = 'http://fanyi.youdao.com/translate'
        self.headers = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36'
        }
        self.formdata = {
            "i": word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": "16122720503537",
            "sign": "83fec6d53385b6fe34ce5ac460ee9df0",
            "lts": "1612272050353",
            "bv": "4f7ca50d9eda878f3f40fb696cce4d6d",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME"
        }
    def post_data(self):
       response = requests.post(self.url,headers=self.headers,data=self.formdata)
       # print(response)
       return response.content

    def parse_data(self,data):
        dict_data = json.loads(data)
        print(dict_data["translateResult"][0][0]["tgt"])


    def run(self):
        """构思爬取思路"""
        # url
        # headers
        # formdata
        # response
        data = self.post_data()
        # print(data)
        # 解析响应
        self.parse_data(data)
if __name__ == '__main__':
    word=input("请输入你要查找的单词:")
    youdao = Youdao(word)
    youdao.run()
