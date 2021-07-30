from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.keys import  Keys
#创建浏览器
web=Chrome()
#打开浏览器，请求到拉钩

web.get('https://www.lagou.com')

#找到那个叉子，取消他
web.find_element_by_xpath('//button[@id="cboxClose"]').click()

#来一个延池
time.sleep(1)
#输入Python回车找到文本框
web.find_element_by_xpath('//*[@id="search_input"]').send_keys('python',Keys.ENTER)

# 这个找xpath是错的
# web.find_elements_by_xpath()
n=1
alist=web.find_elements_by_class_name('position_link')
for a in alist:
    a.find_element_by_tag_name("h3").click()
    #窗口转化
    # web.switch_to.window(web.window_handles[-1])#跳转到第一个窗口
    # text=web.find_element_by_xpath('//*[@id="container"]/div[1]').text#拿文本
    # #招聘信息保存到文本
    # f=open('abc/需求_%s.txt'%n,mode='w')
    # f.write(text)
    # f.close()#关闭文本
    # web.close()#关闭窗口
    # #调整窗口到最开始的那个页面
    # web.switch_to.window(web.window_handles[0])
    # time.sleep(1)
    # n+=1