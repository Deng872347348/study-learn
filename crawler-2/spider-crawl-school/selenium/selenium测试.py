# from selenium import webdriver
# import time
# driver = webdriver.Chrome() # 记得这里Chrome首字母是大写，否则会报错。
# # 打开百度网页
# driver.get('https://baidu.com/')
# time.sleep(3)
# driver.find_element_by_id('kw').send_keys('python')
# button_tag = driver.find_element_by_id('su')
# time.sleep(2)
# button_tag.click()
# time.sleep(5)
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By #这个是我们在find_element()可以选择和find_element_by_id一样的效果
import time
driver=webdriver.Chrome()

#打开百度网页
driver.get('https://baidu.com/')
time.sleep(3)
# driver.find_element_by_id('kw').send_keys('python')
driver.find_element(By.ID,'kw').send_keys('miantaoge') # .find_element(By.)后面会提示很多中定位方法，
# 然后自由选择，这里我们仍然选择id定位，后面就逗号，然后输入id值。效果是跟刚才一样的。
button_tag = driver.find_element_by_id('su')
time.sleep(2)
button_tag.click()
time.sleep(5)
driver.quit()
