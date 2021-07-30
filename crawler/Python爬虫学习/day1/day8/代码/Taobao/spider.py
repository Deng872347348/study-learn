from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 判断元素条件
import re
from pyquery import PyQuery as pq
from config import *
import pymongo

client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

#chromedriver执行路径
driver = webdriver.Chrome()
#selenium官方文档
wait = WebDriverWait(driver, 10)
def search():
    try:
        driver.get("https://world.taobao.com/")
        input = wait.until(
            #等待页面加载完成，css选择器
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mq'))
        )
        submit = wait.until(
            #等待按钮可点击
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_PopSearch > div.sb-search > '
                                                         'div > form > input[type="submit"]'
                                                         ':nth-child(2)'))
        )
        #input框输入搜索关键字
        input.send_keys("美食")
        #按钮点击
        submit.click()
        total_page_num = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager > div > div > div > div.total'))
        )
        #获取第一页商品信息
        get_products()
        #返回总页数
        return total_page_num.text
    except TimeoutException:
        return search()

def next_page(page_num):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > '
                                                             'div > div.form > input'))
        )
        #清空input框
        input.clear()
        #输入跳转到的页码
        input.send_keys(page_num)
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > '
                                                         'div > div > div.form > span.btn.J_Submit'))
        )
        #点击确定按钮跳转
        submit.click()
        #确定是跳转到了所要跳转的页码
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager>div>'
                                                                     'div>div>ul>li.item.active>'
                                                                     'span'),str(page_num)))
        #获取从第二页开始的所有商品信息
        get_products()
    except TimeoutException:
        #如果超时重新调用此函数
        next_page(page_num)

def get_products():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item'))
    )
    #获取完整html
    html = driver.page_source
    #用pyquery解析
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            '商品名称':item.find('.title').text(),
            '图片地址':item.find('.pic .img').attr('src'),
            '商品价格':item.find('.price').text().strip().replace("\n",""),
            '付款人数':item.find('.deal-cnt').text()[:-3],
            '商品地址':item.find('.pic .pic-link').attr('href'),
            '发货地':item.find('.location').text()
        }
        #保存
        save2mongo(product)

def save2mongo(result):
    """保存到MongoDB"""
    try:
        if db[MONGO_TABLE].insert(result):
            print("保存成功",result)
    except Exception:
        print("出错",result)

def main():
    total_page_num = search()
    #获取的信息为“共 ？？ 页”，只留数字
    total_page_num = int(re.compile('(\d+)').search(total_page_num).group(1))
    #从第二页到最后一页获取
    for i in range(2,total_page_num+1):
        next_page(i)

if __name__ == "__main__":
    main()

