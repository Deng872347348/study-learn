# 分析豆瓣你好李焕英的影评，生成词云
# https://movie.douban.com/subject/34841067/comments?start=20&limit=20&status=P&sort=new_score
# url = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&sort=new_score&status=P '\
# % (movie_id, (i - 1) * 20)

import requests
from stylecloud import gen_stylecloud
import jieba
import re
from bs4 import BeautifulSoup
from wordcloud import STOPWORDS

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
}


def jieba_cloud(file_name, icon):
    with open(file_name, 'r', encoding='utf8') as f:
        word_list = jieba.cut(f.read())

        result = " ".join(word_list)    # 分词用  隔开
        # 制作中文词云
        icon_name = " "
        if icon == "1":
            icon_name = ''
        elif icon == "2":
            icon_name = "fas fa-space-shuttle"
        elif icon == "3":
            icon_name = "fas fa-heartbeat"
        elif icon == "4":
            icon_name = "fas fa-bug"
        elif icon == "5":
            icon_name = "fas fa-thumbs-up"
        elif icon == "6":
            icon_name = "fab fa-qq"
        pic = str(icon) + '.png'
        if icon_name is not None and len(icon_name) > 0:
            gen_stylecloud(text=result,
                           size=1024,  # stylecloud 的大小（长度和宽度）
                           icon_name=icon_name,
                           font_path='simsun.ttc',
                           max_font_size=200,  # stylecloud 中的最大字号
                           max_words=2000,  # stylecloud 可包含的最大单词数
                           stopwords=True,  # 布尔值，用于筛除常见禁用词
                           custom_stopwords=STOPWORDS,
                           output_name=pic)
        else:
            gen_stylecloud(text=result, font_path='simsun.ttc', output_name=pic)
        return pic


def spider_comment(movie_id, page):
    comment_list = []
    with open("douban.txt", "a+", encoding='utf-8') as f:
        for i in range(1,page+1):

            url = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&sort=new_score&status=P' \
                  % (movie_id, (i - 1) * 20)

            req = requests.get(url, headers=headers)
            req.encoding = 'utf-8'
            comments = re.findall('<span class="short">(.*)</span>', req.text)


            f.writelines('\n'.join(comments))
    print(comments)

# 主函数
if __name__ == '__main__':
    movie_id = '34841067'
    page = 10
    spider_comment(movie_id, page)
    jieba_cloud("douban.txt", "1")
    jieba_cloud("douban.txt", "2")
    jieba_cloud("douban.txt", "3")
    jieba_cloud("douban.txt", "4")
    jieba_cloud("douban.txt", "5")

    jieba_cloud("douban.txt", "6")
