from selenium import  webdriver
import time
# 1.创建浏览器对象
driver = webdriver.Chrome()

# 2.操作浏览器对象
driver.get("https://www.baidu.com")
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
driver.find_element_by_xpath('//*[@id="su"]').click()

time.sleep(2)

#driver.quit()