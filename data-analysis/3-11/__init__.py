import requests
from bs4 import BeautifulSoup
import os


def getHtml(url):
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r
    except:
        return "爬取失败"


def getLink(demo, pagelist):
    try:
        soup = BeautifulSoup(demo.text, "html.parser")
        for link in soup.find_all('img'):
            pagelist.append(link.get('src'))
        print(pagelist)
    except:
        return "获取失败"


def getPic(pagelist, root):
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        print(len(pagelist))  # 这里还能正常输出pagelist列表的长度的
        for i in pagelist:
            print('为什么不行呢')  # 程序到这里就不能打印这行字符了，不知道哪里出错了
            path = root + pagelist[i]
            if not os.path.exists(path):
                r = getHtml(pagelist[i])
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()0.
                    print('文件已保存成功')
            else:
                print('文件已存在')
    except:
        return '下载失败'


if __name__ == "__main__":
    pagelist = []
    root = 'E:\python社区版\python项目\学校上课数据分析代码\3-11\煎蛋网'
    url = 'http://jandan.net/ooxx/MjAyMTAzMDktMTEw#comments'
    demo = getHtml(url)
    getLink(demo, pagelist)
    getPic(pagelist, root)
