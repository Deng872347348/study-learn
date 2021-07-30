from selenium import webdriver
import time
from selenium.webdriver.common.keys import  Keys
web=webdriver.Chrome()

web.get('https://login.51job.com/login.php')

web.find_element_by_xpath('//*[@id="loginname"]').send_keys('15608471682')#输入密码
web.find_element_by_xpath('//*[@id="password"]').send_keys('15608471682.a')#密码
#点击登录
web.find_element_by_xpath('//*[@id="login_btn"]').click()
#浏览器全屏
web.maximize_window()

web.find_element_by_xpath('//*[@id="topIndex"]/div/p/a[2]').click()
#time.sleep(1)

#找到职位搜索框，输入python
web.find_element_by_xpath('//*[@id="keywordInput"]').send_keys("python")
# web.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/span').click()
# ttags=web.find_elements_by_class_name('ttag')
# time.sleep(1)
# for a in ttags:
#     a.click()
web.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a/span').click()



