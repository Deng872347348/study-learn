from  selenium import  webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.58.com')

print(driver.current_url)
# 记录所有的窗口句柄,新打开的窗口句柄会添加到列表尾部
print(driver.window_handles)


# 点击合租
driver.find_element_by_xpath('//*[@id="fcNav"]/em/a[1]').click()

# 切换窗口
driver.switch_to.window(driver.window_handles[-1])


print(driver.current_url)
# 记录所有的窗口句柄,新打开的窗口句柄会添加到列表尾部
print(driver.window_handles)


el_list = driver.find_elements_by_xpath('/html/body/div[7]/div[2]/ul/li/div[2]/h2/a')
print(el_list)


for el in el_list:
    print(el.text,el.get_attribute('href'))


# driver.quit()