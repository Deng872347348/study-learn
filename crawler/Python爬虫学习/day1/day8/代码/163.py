from selenium import  webdriver
import time

driver = webdriver.Chrome()
driver.get('https://mail.163.com/')
driver.maximize_window() # 窗口最大化
time.sleep(1)


iframe = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)

driver.find_element_by_name('email').send_keys("J18692872087")
driver.find_element_by_name('password').send_keys('jiuge@123')
driver.find_element_by_id('dologin').click()

time.sleep(6)

driver.quit()