# 爬取百度贴吧
import requests


class BdTieba():
    def __init__(self, name, pn):
        # 保存贴吧名
        self.name = name
        # 初始url
        self.base_url = "http://tieba.baidu.com/f?kw={}&pn=".format(name)
        # 构造请求头
        self.headers = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/69.0.3497.100Safari/537.36"
        }

        # 2. 批量生成url
        # 使用列表推导式生成了url列表
        self.url_list = [self.base_url + str(i*50) for i in range(pn)]
        # 打印测试
        # print(self.url_list)

    # 3. 批量发送请求，封装发送请求
    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def save_data(self, data, index):
        filename = self.name + "_{}.html".format(index)
        with open(filename, "wb") as f:
            f.write(data)

    def run(self):
        # 1.请求初始url，测试使用
        # response = requests.get(url=self.base_url, headers=self.headers)
        # 打印测试,测试成功返回结果
        # print(response.text)

        # 2.批量生成url
        for url in self.url_list:
            data = self.get_data(url)

        # 3.批量发送请求
            # 4.保存网页，为了保存的网页名字不重复，且有顺序，这里使用index进行区分
            # 获取当前url的index
            index = self.url_list.index(url)
            # 保存
            self.save_data(data, index)



if __name__ == '__main__':
    bdspider = BdTieba("python", 10)
    bdspider.run()