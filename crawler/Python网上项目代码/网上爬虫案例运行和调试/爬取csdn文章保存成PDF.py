import pdfkit
import requests
import parsel

html_str = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
{article}
</body>
</html>
"""


def save(article, title):
    pdf_path = 'pdf\\' + title + '.pdf'
    html_path = 'html\\' + title + '.html'
    html = html_str.format(article=article)
    with open(html_path, mode='w', encoding='utf-8') as f:
        f.write(html)
        print('{}已下载完成'.format(title))
    # exe 文件存放的路径
    config = pdfkit.configuration(wkhtmltopdf='E:\python社区版\python项目\新建文件夹\Python网上项目代码\网上爬虫案例运行和调试\wkhtmltox-0.12.5-1.msvc2015-win64(1).exe')
    # 把 html 通过 pdfkit 变成 pdf 文件
    pdfkit.from_file(html_path, pdf_path, configuration=config)


def main(html_url):
    # 请求头
    headers = {
        "Host": "blog.csdn.net",
        "Referer": "https://blog.csdn.net/Deng872347348/article/details/102570971",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    }
    # 用户信息
    cookie = {
        'Cookie': 'uuid_tt_dd=10_18637768680-1608011006080-338161; UserName=Deng872347348; UserInfo=d29098d245c341fb9dee38afc80a17d1; UserToken=d29098d245c341fb9dee38afc80a17d1; UserNick=Deng872347348; AU=F88; UN=Deng872347348; BT=1608011062847; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22Deng872347348%22%2C%22scope%22%3A1%7D%7D; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_18637768680-1608011006080-338161!5744*1*Deng872347348; UM_distinctid=1784f8b5bb3990-08b091dc9724da-5771031-144000-1784f8b5bb4a67; __gads=ID=13dd565e10255905-2293ccaed3c6007b:T=1616724508:RT=1616724508:S=ALNI_MbpQHDzimK_1ebK6qedsce6ZyAgAw; Hm_lvt_e5ef47b9f471504959267fd614d579cd=1617002767,1617711701; dc_sid=bd78594fe1b929334707d5b8bbccb9b2; c_segment=1; firstDie=1; referrer_search=1618034642761; dc_session_id=10_1618039399853.778396; announcement-new=%7B%22isLogin%22%3Atrue%2C%22announcementUrl%22%3A%22https%3A%2F%2Fblog.csdn.net%2Fblogdevteam%2Farticle%2Fdetails%2F112280974%3Futm_source%3Dgonggao_0107%22%2C%22announcementCount%22%3A0%2C%22announcementExpire%22%3A3600000%7D; aliyun_webUmidToken=T2gAFvaVpa4hViFI8g6b5j6DtQfWXa0zyEOwxZg2P5zTYzNk1TVmGW6Tc4mnQlZfa6s=; c_first_ref=www.baidu.com; c_first_page=https%3A//blog.csdn.net/blwinner/article/details/79161907; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1618031122,1618031974,1618041043,1618041080; c_utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-0; log_Id_click=2948; c_pref=https%3A//blog.csdn.net/fei347795790/category_8746749.html; c_ref=https%3A//blog.csdn.net/Deng872347348%3Fspm%3D1001.2014.3001.5343; c_page_id=default; dc_tos=qrc8xu; log_Id_pv=3595; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1618041666; log_Id_view=7138'
    }
    response = requests.get(url=html_url, headers=headers, cookies=cookie)
    selector = parsel.Selector(response.text)
    urls = selector.css('.article-list h4 a::attr(href)').getall()
    for html_url in urls:
        response = requests.get(url=html_url, headers=headers, cookies=cookie)
        # text 文本（字符串）
        # 遭遇了反扒
        # print(response.text)
        """如何把 HTML 变成 PDF 格式"""
        # 提取文章部分
        sel = parsel.Selector(response.text)
        # css 选择器
        article = sel.css('article').get()
        title = sel.css('h1::text').get()
        save(article, title)


if __name__ == '__main__':
    url = 'https://blog.csdn.net/Deng872347348/article/list/1'
    main(url)
