
#导入python里面的模块
import os
import requests
from colorama import Fore#判断抛出异常的
from fake_useragent import UserAgent  #
from requests import HTTPError

#
def download_page(url, parmas=None):
    """
    根据url地址下载html页面
    :param url:
    :param parmas:
    :return: str
    """
    #抛出异常
    try:
        ua = UserAgent()
        #动态的网站的代理
        headers = {
            'User-Agent': ua.random,
        }
        # 请求https协议的时候， 回遇到报错: SSLError
        # verify=Flase不验证证书
        response = requests.get(url, params=parmas, headers=headers)
    #处理异常
    except  HTTPError as e:
        print(Fore.RED + '[-] 爬取网站%s失败: %s' % (url, str(e)))
        return None
    else:
        #返回网页源代码
        return response
    #这个封装一个解析的函数
def parse_html(html):
    #定义一个文件夹的路径
    path="weibo_pics"
    #获取json数据里面的data
    cards = html.get('data').get('cards')
    # print(cards)
    # 定义一个变量用来计数
    count = 0

    #通过for循环对提取的数据进行依次的提取
    for card in cards:
        try:
            count += 1
            #提取json里面的text文本
            #提取pics里面的照片信息
            text = card['mblog'].get('text')
            pics = card['mblog'].get('pics')
            # 对于博客正文的内容进行处理: 删除标签(正则+re.sub)
            print("第%s篇微博正文内容: %s" % (count, text))
            if pics:
                #使用enumerate函数 ,index是下表，
                for index, pic in enumerate(pics):
                    #获取图片的url
                    pic_url = pic.get('url')
                    #调用获取图片的url，发起进去，并且把他转化成二进制格式
                    pic_content = download_page(pic_url).content
                    #创建一个文件夹用来存储图片
                    if not os.path.exists(path):
                        #自动创建一个文件夹，文件名是我们上面定义的
                        os.mkdir(path)
                    # 图片网址-> 图片名称 https://wx1.sinaimg.cn/orj360/005N3SJDly1fyhlxakcj3j30dc0dcaa4.jpg
                    img_fname = os.path.join('weibo_pics', pic_url.split('/')[-1])
                    #保存图片
                    with open(img_fname, 'wb') as f:
                        f.write(pic_content)
                        print("下载第[%s]张图片成功" % (index + 1))
        except Exception as e:
            print("下载博客失败: %s" % (str(e)))
#定义运行的主函数
if __name__ == '__main__':
    uid = input("请输入你要爬取微博博主的uid:")
    for page in range(10):
        url = 'https://m.weibo.cn/api/container/getIndex?uid=%s&type=uid&containerid=107603%s&page=%s' % (
            uid, uid, page)
        html = download_page(url).json()
        parse_html(html)

