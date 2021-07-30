# -*- coding: UTF-8 -*-
"""
@File    ：spider.py
@Author  ：叶庭云
@CSDN    ：https://yetingyun.blog.csdn.net/
"""
from selenium import webdriver
from time import sleep
import logging
import openpyxl


wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['段子内容', '好笑数', '评论数'])
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

chrome_driver = r'E:\python社区版\python项目\Python爬虫学习\chromedriver.exe'

options = webdriver.ChromeOptions()
# 可以设置无头模式 不弹出浏览器
# options.add_argument("--headless")
# 关闭左上方 Chrome 正受到自动测试软件的控制的提示
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("excludeSwitches", ['enable-automation'])
browser = webdriver.Chrome(options=options, executable_path=chrome_driver)
# 可以设置绕过Webdriver的检测
browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
"source": """
Object.defineProperty(navigator, 'webdriver', {
get: () => undefined
})
"""
})


def get_data(page):     # 爬取数据函数
    url = f'https://www.qiushibaike.com/text/page/{page}/'
    browser.get(url)    # 访问目标url
    browser.maximize_window()   # 最大化窗口
    sleep(1)    # 短暂休眠
    # Xpath定位到所有包含段子信息的div标签
    items = browser.find_elements_by_xpath('//*[@id="content"]/div/div[2]/div')
    # print(len(items))  一页25条段子
    # 遍历  获取每一条段子信息
    for item in items:
        con = item.find_element_by_xpath('.//a/div/span').text                   # 段子内容
        funny_num = item.find_element_by_xpath('.//div[2]/span[1]/i').text      # 好笑数
        comment_num = item.find_element_by_xpath('.//div[2]/span[2]/a/i').text   # 评论数
        sheet.append([con, funny_num, comment_num])
        logging.info([con, funny_num, comment_num])


if __name__ == '__main__':
    for i in range(1, 14):    # 翻页爬取
        get_data(i)
    browser.quit()     # 关闭浏览器
    wb.save(filename='datas.xlsx')   # 保存数据

