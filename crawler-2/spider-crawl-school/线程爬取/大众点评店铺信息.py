import re
import requests
from fontTools.ttLib import TTFont
import pandas as pd

# 获取网页数据
def get_html(url, headers):   
    try:
        rep = requests.get(url ,headers=headers)
    except Exception as e :
        print(e)
    text = rep.text
    html = re.sub('\s', '', text) #去掉非字符数据
    
    return html


# 获取字体映射关系
def get_real_list(html, headers):
    # 图文混排css链接
    text_css = re.findall('<!--图文混排css--><linkrel="stylesheet"type="text\/css"href="(.*?)">', html)[0]  
    # 'http://s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/29de4c2bc5d95d1e147c3c25a5f4aad8.css'
    # css链接
    css_url = 'http:' + text_css
    font_html = get_html(css_url, headers)
    # 字体信息列表
    font_list = re.findall(r'@font-face{(.*?)}', font_html)
    
    # 获取使用到的字体及其链接
    font_dics = {}
    for font in font_list:
        font_name = re.findall(r'font-family:"PingFangSC-Regular-(.*?)"', font)[0]
        font_dics[font_name] = 'http:' + re.findall(r',url\("(.*?)"\);', font)[0]
    
    # 由于我们用到的只有shopNum、tagName和address，这里只下载这三类字体
    font_use_list = ['shopNum','tagName','address']
    for key in font_use_list:
        woff = requests.get(font_dics[key], headers=headers).content
        with open(f'{key}.woff', 'wb')as f:
            f.write(woff)
    
    # 修改三类字体映射关系
    real_list = {}
    for key in font_use_list:
        # 打开本地字体文件
        font_data = TTFont(f'{key}.woff')
        # font_data.saveXML('shopNum.xml')
        # 获取全部编码，前2个非有用字符去掉 
        uni_list = font_data.getGlyphOrder()[2:]
        # 请求数据中是 "&#xecd5" 对应 编码中为"uniecd5",我们进行替换，以请求数据为准
        real_list[key] = ['&#x' + uni[3:] for uni in uni_list]
    
    # 字符串
    words = '1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭人百餐茶务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际路祥青镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡厦府铺内侧元购前幢滨处向座下澩凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常真们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕'
    
    return real_list, words


# 获取单页全部信息
def get_items(html, real_list, words):
    
    # 获取单页全部商铺html整体信息
    shop_list = re.findall(r'<divclass="shop-listJ_shop-listshop-all-list"id="shop-all-list">(.*)<\/div>',html)[0]
    
    # 获取单页全部商铺html信息组成的列表
    shops = re.findall(r'<liclass="">(.*?)<\/li>', shop_list)
    
    items = []
    for shop in shops:
        # 解析单个商铺信息
        # shop = shops[0]
        item = {}
        # 商铺id（唯一性，用于数据清洗阶段去重）
        item['shop_id'] = re.findall(r'<divclass="txt"><divclass="tit">.*data-shopid="(.*?)"', shop)[0]
        # 商铺名称
        item['shop_name'] = re.findall(r'<divclass="txt"><divclass="tit">.*<h4>(.*)<\/h4>', shop)[0]
        # 商铺星级,由于是二位数，需要除以10.0转化为浮点数
        item['shop_star'] = re.findall(r'<divclass="nebula_star"><divclass="star_icon"><spanclass="starstar_(\d+)star_sml"><\/span>', shop)[0]
        item['shop_star'] = int(item['shop_star'])/10.0
        
        # 其实关于商铺地址信息，在class="operate J_operate Hide"中的data-address是有的
        # 因此，我们不需要用到 字体反爬，直接正则获取吧
        # 商铺地址
        item['shop_address'] = re.findall('<divclass="operateJ_operateHide">.*?data-address="(.*?)"', shop)[0]
        
        shop_name = item['shop_name']
        # 评价数和人均价格，用的是shopNum
        try:
            shop_review = re.findall(r'<b>(.*?)<\/b>条评价', shop)[0]
        except:
            print(f'{shop_name} 无评价数据')
            shop_review = ''
            
        try:
            shop_price = re.findall(r'人均<b>￥(.*?)<\/b>', shop)[0]
        except:
            print(f'{shop_name} 无人均消费数据')
            shop_price = ''
            
        for i in range(10):
            shop_review = shop_review.replace(real_list['shopNum'][i], words[i])
            shop_price = shop_price.replace(real_list['shopNum'][i], words[i])
            
        item['shop_review'] = ''.join(re.findall(r'\d',shop_review))
        item['shop_price'] = ''.join(re.findall(r'\d',shop_price))
        
        # 商铺所在地和视频分类用的是tagName
        shop_tag_site = re.findall(r'<spanclass="tag">.*data-click-name="shop_tag_region_click"(.*?)<\/span>', shop)[0]
        # 商铺分类
        shop_tag_type = re.findall('<divclass="tag-addr">.*?<spanclass="tag">(.*?)</span></a>', shop)[0]
        for i in range(len(real_list['tagName'])):
            shop_tag_site = shop_tag_site.replace(real_list['tagName'][i], words[i])
            shop_tag_type = shop_tag_type.replace(real_list['tagName'][i], words[i])
        # 匹配中文字符的正则表达式： [\u4e00-\u9fa5]
        item['shop_tag_site'] = ''.join(re.findall(r'[\u4e00-\u9fa5]',shop_tag_site))
        item['shop_tag_type'] = ''.join(re.findall(r'[\u4e00-\u9fa5]',shop_tag_type))
        items.append(item)
    
    return items


# 获取页数
def get_pages(html):
    try:
        page_html = re.findall(r'<divclass="page">(.*?)</div>', html)[0]
        pages = re.findall(r'<ahref=.*>(\d+)<\/a>', page_html)[0]
    except :
        pages = 1
    
    return pages


if __name__ == '__main__':
    headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Cookie":你的cookie,
            }
    # 搜索关键字
    key = '滑雪'
    # 基础url
    url = f'https://www.dianping.com/search/keyword/2/0_{key}'
    html = get_html(url, headers)
    pages = int(get_pages(html))
    real_list, words = get_real_list(html,headers)
    shop_data = get_items(html, real_list, words)
    for page in range(2,pages+1):
        aim_url = f'{url}/p{page}'
        html = get_html(aim_url, headers)
        items = get_items(html, real_list, words)
        shop_data.extend(items)
        print(f'已爬取{page}页数据')
    # 转化为dataframe类型
    df = pd.DataFrame(shop_data)
    # df.shop_review = df.shop_review.fillna('0')
