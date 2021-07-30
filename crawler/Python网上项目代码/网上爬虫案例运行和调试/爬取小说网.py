import requests
import parsel
from tqdm import tqdm


def get_response(html_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=headers)
    response.encoding = response.apparent_encoding
    return response


def save(novel_name, title, content):
    """
    保存小说
    :param title: 小说章节标题
    :param content: 小说内容
    :return:
    """
    filename = f'{novel_name}' + '.txt'
    # 一定要记得加后缀 .txt  mode 保存方式 a 是追加保存  encoding 保存编码
    with open(filename, mode='a', encoding='utf-8') as f:
        # 写入标题
        f.write(title)
        # 换行
        f.write('\n')
        # 写入小说内容
        f.write(content)


def get_one_novel(name, novel_url):
    # 调用请求网页数据函数
    response = get_response(novel_url)
    # 转行成selector解析对象
    selector = parsel.Selector(response.text)
    # 获取小说标题
    title = selector.css('.bookname h1::text').get()
    # 获取小说内容 返回的是list
    content_list = selector.css('#content::text').getall()
    # ''.join(列表) 把列表转换成字符串
    content_str = ''.join(content_list)
    save(name, title, content_str)


def get_all_url(html_url):
    # 调用请求网页数据函数
    response = get_response(html_url)
    # 转行成selector解析对象
    selector = parsel.Selector(response.text)
    # 所有的url地址都在 a 标签里面的 href 属性中
    dds = selector.css('#list dd a::attr(href)').getall()
    # 小说名字
    novel_name = selector.css('#info h1::text').get()
    for dd in tqdm(dds):
        novel_url = 'http://www.biquges.com' + dd
        get_one_novel(novel_name, novel_url)


if __name__ == '__main__':
    novel_id = input('输入书名ID：')
    url = f'http://www.biquges.com/{novel_id}/index.html'
    get_all_url(url)
