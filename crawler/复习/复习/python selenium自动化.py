import time
from selenium.webdriver import  Chrome#导入浏览器的包
#自动敲回车的导入库
from  selenium.webdriver.common.keys import  Keys
#打开浏览器
web=Chrome()
#打开浏览器，请求网站
web.get('https://www.baidu.com')

web.find_element_by_xpath().click()#找到浏览器你要找的路径的xoath
#来一个延池
#导入时间模块
time.sleep()
#找到文本框，输入python，输入回车
web.find_element_by_xpath("").send_keys('',Keys.INSERT)
#web.find_elements_by_xpath()
alist=web.find_element_by_class_name("")

for a in alist:
    a.find
    #窗口转化
    web.switch_to.window()
    text=web.find_element_by_xpath().text#拿文本
#把拿到的文本保存在文件中


#关闭窗口
web.close()

#调整窗口到最开始那个页面
web.switch_to.window()
time.sleep()