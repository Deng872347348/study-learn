# 导入seleinum的webdriver接口
from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')
# 5秒钟后关闭浏览器
time.sleep(5)
driver.quit()