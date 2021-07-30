from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json



class ZufangSpider(object):

    def __init__(self):
        # 创建浏览器驱动对象
        self.driver = webdriver.Chrome()
        # 准备URL
        self.url = 'http://sz.58.com/chuzu/'

    def get_data_list(self):
        """提取数据, 返回数据列表"""
        # 使用XPATH提取, 就要先分组:
        # 获取包租房信息的li标签
        lis = self.driver.find_elements_by_xpath('//ul[@class="listUl"]/li')[:-2]
        # 遍历lis, 提取需要的数据

        data_list = []

        for li in lis:
            # 广告li的, class="apartments-pkg apartments"
            # 如果不是广告, 才提取数据
            if li.get_attribute('class') != 'apartments-pkg apartments':
                data = {}
                data['title'] = li.find_element_by_xpath('./div[2]/h2/a').text
                data['url'] = li.find_element_by_xpath('./div[2]/h2/a').get_attribute('href')
                data['price'] = li.find_element_by_xpath('./div[3]/div[2]/b').text
                print(data)
                data_list.append(data)

        # 找下一页的a标签
        # 由于最后一页没有下一页的a标签, 如果使用find_element就会报错
        next_page = self.driver.find_elements_by_class_name('next')
        if len(next_page) != 0:
            next_page = next_page[0]
        else:
            next_page = None
        return data_list, next_page

    def save_data(self, data_list):
        """保存数据"""
        with open('58zufang.json', 'a' , encoding='utf8') as f:
            for data in data_list:
                json.dump(data, f, ensure_ascii=False)
                f.write('\n')

    def run(self):
        # 2. 加载租房页面
        self.driver.get(self.url)

        while True:
            # 3. 获取数据
            data_list, next_page = self.get_data_list()
            # 4. 保存数据
            self.save_data(data_list)

            # 如果有下一页, 就点击它
            if next_page:
                next_page.click()
            else:
                break

        # 退出浏览器
        self.driver.quit()

if __name__ == '__main__':
    zfs = ZufangSpider()
    zfs.run()
