from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select  # 导入Select类，在这个案例里这个没有用
driver = webdriver.Chrome()
# 打开豆瓣网页
driver.get('https://www.douban.com/')
time.sleep(1)
# 切换到账号密码登录界面
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(1)
# 切换iframe
login_tag = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(login_tag) # 将driver.switch_to_frame换成driver.switch_to

# 切换到账号密码登陆方式，这个是在切换到iframe页面后的标签路径
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()
time.sleep(1)
# 输入账号，这个是在切换到iframe页面后的标签路径
acount_tag = driver.find_element_by_xpath('//*[@id="username"]')
acount_tag.send_keys('###########')
time.sleep(1)
# 输入密码，这个是在切换到iframe页面后的标签路径
code_tag = driver.find_element_by_xpath('//*[@id="password"]')
code_tag.send_keys('#########')
time.sleep(2)
button_tag = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()
