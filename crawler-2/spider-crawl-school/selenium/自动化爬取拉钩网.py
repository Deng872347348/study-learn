# !/usr/bin/env python
# -*-coding:utf-8-*-
# date :2021/2/14 13:12
# author:Sabo
from selenium import webdriver
from time import sleep
if __name__ == '__main__':
    # 目的网址
    url = "https://www.lagou.com/"
    driver = webdriver.Chrome()
    # 获取网页
    driver.get(url)
    driver.maximize_window()
    # 关闭首页广告
    driver.find_element_by_xpath("//*[@id=\"cboxClose\"]").click()
    # 关闭城市定位
    # driver.find_element_by_id("cboxClose").click()
    sleep(1)
    # 搜索python
    driver.find_element_by_xpath('//*[@id="search_input"]').send_keys('python')
    driver.find_element_by_xpath('//*[@id="search_button"]').click()
    sleep(1)
    driver.find_element_by_xpath('/html/body/div[8]/div/div[2]').click()
    # 获取职位网址列表bn
    aList = driver.find_elements_by_class_name('position_link')
    # 单个列表点击
    n = 1
    for a in aList:
        # 点击单个网址
        a.find_element_by_tag_name('h3').click()
        # 跳转到单个网址中去
        sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        sleep(2)
        text = driver.find_element_by_xpath('//*[@id="job_detail"]/dd[2]').text  # 文本
        # 写入文件
        f = open("Info_%s.txt" % n, mode = 'w')
        f.write(text)
        # 关闭文件
        f.close()
        driver.close()
        # 跳转回第一个窗口
        driver.switch_to.window(driver.window_handles[0])
        # 文件数目加1
        sleep(1)
        n += 1
