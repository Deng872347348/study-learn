from  selenium import  webdriver

url = 'https://qzone.qq.com/'

driver = webdriver.Chrome()

driver.get(url)

el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
print(el_frame)
# driver.switch_to.frame(el_frame)
#
# driver.find_element_by_id("switcher_plogin").click()
# driver.find_element_by_id('u').send_keys('872347348')
# driver.find_element_by_id('p').send_keys('06021511.')
# driver.find_element_by_id('login_button').click()