from selenium import  webdriver
import time

driver=webdriver.Chrome()
url='https://mail.163.com/'
driver.get(url)

#先找到登录整体


usename=driver.find_element_by_id('//*[@id="auto-id-1614238822532"]').send_keys('deng872347348')
password=driver.find_element_by_id('//*[@id="auto-id-1614238822535"]').send_keys('15608471682.a')
longin=driver.find_element_by_id('//*[@id="dologin"]').click()


