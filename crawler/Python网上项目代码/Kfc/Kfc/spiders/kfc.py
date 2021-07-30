import scrapy
import json
from  ..items import KfcItem
class KfcSpider(scrapy.Spider):
    name = 'kfc'
    allowed_domains = ['www.kfc.com.cn']
    post_url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    city_name=input("请输入城市名称 : ")
    def start_requests(self):
        # 重写start_request方法(),生成所有抓取的url地址，交给调度器入队列
        formdata = {
            'cname': self.city_name,
            'pid': '',
            'pageIndex': '1',
            'pageSize': '10',
        }
        yield scrapy.FormRequest(url=self.post_url,formdata=formdata,callback=self.get_total)
    def get_total(self,response):
        # 获取总页数，交给调度器
        html=json.loads(response.text)
        count=html['Table'][0]['rowcount']
        total_page=count // 10 if count%10==0 else count // 10 +1
        #将所有页面的url交给调度器
        for page in range(1,total_page+1):
            formdata={
                'cname':self.city_name,
                'pid':'',
                'pageIndex': str(page),
                'pageSize': '10',
            }
            yield scrapy.FormRequest(url=self.post_url,formdata=formdata,callback=self.parse)
    def parse(self, response):
        #解析提取具体1的门店1数据
        html=json.loads(response.text)
        for one_shop_dict in html['Table1']:
            item=KfcItem()
            item['rownum'] = one_shop_dict['rownum']
            item['storeName'] = one_shop_dict['storeName']
            item['addressDetail'] = one_shop_dict['addressDetail']
            item['cityName'] = one_shop_dict['cityName']
            item['provinceName'] = one_shop_dict['provinceName']

            #一个完整的门店数据提取完成，交给项目管道文件处理
            yield item