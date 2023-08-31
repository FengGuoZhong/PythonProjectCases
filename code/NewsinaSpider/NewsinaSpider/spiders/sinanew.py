import scrapy
import random
from datetime import datetime
from NewsinaSpider.items import NewsinaspiderItem
import re

import warnings
warnings.filterwarnings("ignore") #去除不影响程序运行的警告
# 参考https://zhuanlan.zhihu.com/p/71925619

class SinanewSpider(scrapy.Spider):
    name = 'sinanew'
    allowed_domains = ['news.sina.com.cn']
    start_urls = ['http://news.sina.com.cn/']

    #model_url = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.6546448152284963&callback=jQuery111209472105093440668_1693383075840&_=1693383075841'
    model_url =  'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid={}&k=&num=50&page={}&r={}'


    # "2509": "全部",
    # "2510": "国内",
    # "2511": "国际",
    # "2669": "社会",
    # "2512": "体育",
    # "2513": "娱乐",
    # "2514": "军事",
    # "2515": "科技",
    # "2516": "财经",
    # "2517": "股市",
    # "2518": "美股",
    # "2968": "国内_国际",
    # "2970": "国内_社会",
    # "2972": "国际_社会",
    # "2974": "国内国际社会"

    def start_requests(self):

        for page in range(1,10):
            lid = '2509' #全部新闻
            r = random.random()
            # 构建一个新的请求对象
            request = scrapy.Request(
                url=self.model_url.format(lid,page,r),
                callback=self.parse  # 回调交给parse获取响应，传递的解析函数的名字
            )
            yield request

    def parse(self, response,**kwargs):
        #print(response.json())

        result  = response.json()
        data_list = result.get('result').get('data')
        for data in data_list:
            item = NewsinaspiderItem()

            ctime = datetime.fromtimestamp(int(data.get('ctime'))) #发布时间
            ctime = datetime.strftime(ctime, '%Y-%m-%d %H:%M')
            item['ctime'] = str(ctime)
            item['url'] = data.get('url')
            item['wapurls'] = data.get('wapurls')
            item['title'] = data.get('title') #新闻标题
            item['intro'] = (data.get('intro')).strip()
            item['media_name'] = data.get('media_name') #发布的媒体
            item['keywords'] = data.get('keywords')
            item['oid'] = data.get('oid') #ID
            #yield item
            yield scrapy.Request(
                url=item['url'],
                callback=self.parse_content,
                meta={'item': item}
            )


    #新闻内容
    def parse_content(self,response):
        #print(response)
        item = response.meta.get('item')
        #print(item)

        content_list = response.xpath('//*[@id="article"]//p/text()')
        #print(content)
        content = ''.join(content_list.extract())
        content = re.sub(r'\u3000', '', content)
        # print(new_content)

        item['content'] = content
        yield item

