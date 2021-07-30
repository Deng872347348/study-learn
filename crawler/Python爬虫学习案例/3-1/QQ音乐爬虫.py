import requests
import jsonpath
"""
2000多一点

分期 咱们老师承担利息, 免息.
有钱的人 越来越有钱,

先让自己有钱,. 进入一些圈子...

卡密,  2000多块钱.

周期 3个月 你就能赚到3倍以上.

一个半月 可以学完爬虫,   半个月复习,.1个月 赚6K

500    工具人  

自己做 项目. 500

抖音脚本, 500-1000


没有任何技术.. 老板. 


8K账号 4W,   2k  

你有渠道吗? 

给你一万个账号密码. 筛选出正确的.  6-7K之间.

post登录 .

8K 他可能就怀疑 以后就只找你做了.


"""
# cookies的时效性啊????session 保持cookies 维持回话
# 进入首页 得到 cookies  csrf保存在cookies里
def get_csrf():
    url = 'https://kuwo.cn/'
    headers = {
        'Accept': 'textml,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.2.773350284.1614335668; _gid=GA1.2.764530357.1614335668; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614335668; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1614343336; kw_token=9LVH3GVO6NG',
        'Host': 'kuwo.cn',
        'Pragma': 'no-cache',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',


    }
    s.get(url, headers=headers)
    csrf = s.cookies.get_dict()['kw_token']
    return csrf


# 音乐的索引 特征值
def get_rid(csrf):
    url = f'https://kuwo.cn/api/www/search/searchMusicBykeyWord?key={keyword}&pn=1&rn=30&httpsStatus=1'
    headers = {
        # 'Accept': 'application/json, textain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.2.773350284.1614335668; _gid=GA1.2.764530357.1614335668; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614335668; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1614341909; kw_token=3PB45UN366F',
        'csrf': csrf,
        # 'Host': 'kuwo.cn',
        # 'Pragma': 'no-cache',
        'Referer': f'https://kuwo.cn/search/list?key={keyword}',
        # 'Sec-Fetch-Dest': 'empty',
        # 'Sec-Fetch-Mode': 'cors',
        # 'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',


    }
    #  防止跨站点攻击,
    r = s.get(url, headers=headers).json()
    rid = jsonpath.jsonpath(r, '$..rid')[0]
    return rid


# 得到 音乐的下载地址
def get_music_url(rid):
    # 下载一首歌
    url = f'https://kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3&br=128kmp3&from=web&t=1614342354424&httpsStatus=1'
    headers = {
        'Accept': 'application/json, textain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_ga=GA1.2.773350284.1614335668; _gid=GA1.2.764530357.1614335668; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1614335668; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1614342187; kw_token=PEL47GQVIED',
        'Host': 'kuwo.cn',
        'Pragma': 'no-cache',
        'Referer': f'https://kuwo.cn/search/list?key={keyword}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',


    }
    r = s.get(url, headers=headers).json()

    music_url = r.get("url")
    return music_url


# 下载音乐
def get_music(music_url):
    with open(f'{requests.utils.unquote(keyword)}.mp3', 'wb') as f:
        f.write(requests.get(music_url).content)


if __name__ == '__main__':
    keyword = input('请输入你需要下载的音乐名字:')
    keyword = requests.utils.quote(keyword)
    # 保持cookies 维持会话.
    s = requests.session()
    csrf = get_csrf()
    rid = get_rid(csrf)
    music_url = get_music_url(rid)
    get_music(music_url)
