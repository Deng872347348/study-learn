"""
selenium抓取民政部最新行政区划代码
"""
from selenium import webdriver
import time


class MzbSpider:
    def __init__(self):
        # 打开浏览器,输入URL地址
        self.driver = webdriver.Chrome()
        self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/2020/')

    def parse_html(self):
        self.driver.find_element_by_xpath('//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a').click()
        # 谨记:只要click(),必须休眠
        time.sleep(1)
        # 切换句柄
        li = self.driver.window_handles
        self.driver.switch_to.window(li[1])
        # 提取数据
        tr_list = self.driver.find_elements_by_xpath('//tr[@height="19"]')
        for tr in tr_list:
            item = {}
            li = tr.text.split()
            item['code'] = li[0]
            item['name'] = li[1]
            print(item)

    def run(self):
        self.parse_html()


if __name__ == '__main__':
    spider = MzbSpider()
    spider.run()

