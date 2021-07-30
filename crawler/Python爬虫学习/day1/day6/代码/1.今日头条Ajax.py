import requests, re, os
from hashlib import md5  # 去重
from selenium import webdriver

def get_cookies(url):
    # 自动化浏览器窗口
    str = ''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options=options)
    browser.get(url)
    for i in browser.get_cookies():
        try:
            name = i.get("name")
            value = i.get("value")
            str = str + name + '=' + value + ';'
        except ValueError as e:
            print(e)
    return str

    # headers

def get_page(offset):
    # params
    params = {
        "aid": "24",
        "app_name": "web_search",
        "offset": "60",
        "format": offset,
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "en_qc": "1",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis",

    }
    # url
    url = "https://www.toutiao.com/api/search/content/"
    # reponse
    try:
        r = requests.get(url, params=params, headers=headers)
        if r.status_code == 200:
            return r.json()
        else:
            print("requests get_page error!")
    except requests.ConnectionError:
        return None


def get_images(json):
    data = json.get("data")
    if data:
        for i in data:
            if i.get('title'):
                title = re.sub('[\t]', ',', i.get('title'))  # re.sub() 正则高级替换 复杂替换
                url = i.get('article_url')
                if url:
                    r = requests.get(url, headers=headers)
                    if r.status_code == 200:
                        imgags_pattern = re.compile('JSON.parse\("(.*?)"\),\n', re.S)  # .*？
                        result = re.search(imgags_pattern, r.text)
                        if result:
                            b_url = 'https://p3.pstatp.com/origin/pgc-image/'
                            up = re.compile('url(.*?)"width', re.S)  # re.S 整体进行匹配
                            results = re.findall(up, result.group(1))
                            if results:
                                for result in results:
                                    yield {
                                        'title': title,
                                        'image': b_url + re.search('F([^F]*)\\\\",', result).group(1)
                                    }

                        else:
                            images = i.get('image_list')
                            for image in images:
                                origin_image = re.sub("list.*?pgc-image", "large/pgc-image",
                                                      image.get('url'))  # 改成origin/pgc-image是原图
                                yield {
                                    'image': origin_image,
                                    'title': title
                                }


def save_image(item):
    title = re.sub(r"[./\\,，！!?？|]","",item.get('title'))
    img_path = "img" + os.path.sep + title
    if not os.path.exists(img_path):
        os.makedirs(img_path)  # 生成目录文件夹
    try:
        resp = requests.get(item.get('image'))
        if requests.codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')  # 单一文件的路径
            if not os.path.exists(file_path):
                with open(file_path, 'wb')as f:
                    f.write(resp.content)
                print("Downloaded image path is %s" % file_path)
            else:
                print('Already Downloade', file_path)

    except Exception as e:
        print(e, 'noe123')


cookies = get_cookies('https://www.toutiao.com/')
headers = {
    'cookie': cookies,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D'
}

# 解析网页
# 保存文件
def main(offset):
    a = get_page(offset)
    for i in get_images(a):
        save_image(i)

if __name__ == '__main__':
    # pool多进程不能实现跨进程共享cookies
    for i in [x * 20 for x in range(3)]:
        main(i)
