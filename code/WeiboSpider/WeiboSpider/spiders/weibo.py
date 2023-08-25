import scrapy
from WeiboSpider.items import WeibospiderItem
from pyquery import PyQuery as pq

from urllib.parse import urlencode
import requests

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    # start_urls = ['http://weibo.com/']

    model_url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover|new_feed&max_id={}&count=10'
    start_urls = [model_url.format(0)]

    longText_url = 'https://weibo.com/ajax/statuses/longtext?id={}'

    headers = {
        "Cookie": "XSRF-TOKEN=Z_ffzq7WE7qZLbk5hfFT7x66; SUB=_2AkMTu-sxf8NxqwJRmf8cz2ngaY11yw7EieKl5xrqJRMxHRl-yT9kqhxYtRB6ODvF3nbjH3GM5x4KAlzWCm39e4cH1ES1; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WhQOx3fU4gdnhT0uzOJQx5V; WBPSESS=xvhb-0KtQV-0lVspmRtycxA4ZzJDTvIQ5yaFPZNCxo7f1JvEU8XycMSJBJnYPE5MSbH3RO-xMEJ2emZOVafj7CY-l6xTdMUZaM44NmjgYINYt6AQRQcdPQmdDfa_2mdw",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }


    def parse(self, response):
        print(response)
        for i in range(1, 2):
            next_url = self.model_url.format(i)
            #print(next_url)

            #构建一个新的请求对象
            request = scrapy.Request(
                url=next_url,
                callback=self.parse #回调交给parse获取响应，传递的解析函数的名字
            )
            yield request

            data = response.json()
            if data['ok'] == 1:
                for statuse in data.get('statuses'):

                    item = WeibospiderItem()

                    #用户信息
                    user_info = statuse.get('user')
                    item['user_id'] = user_info.get('id')  # 发布人id
                    item['screen_name'] = user_info.get('screen_name')  # 发布者昵称

                    #微博信息
                    item['weibo_id'] = statuse.get('id')  # 微博id
                    item['created_at'] = statuse.get('created_at') #发布时间
                    item['region_name'] = statuse.get('region_name') #发布于
                    item['source'] = statuse.get('source') #来源
                    item['text'] = pq(statuse.get('text')).text() #微博内容
                    item['reposts_count'] = statuse.get('reposts_count') #转发数
                    item['comments_count']  = statuse.get('comments_count') #评论数
                    item['attitudes_count']  = statuse.get('attitudes_count') #点赞数

                    item['pic_num'] = statuse.get('pic_num')  #该条微博包含的图片数
                    item['pic'] = []  # 用于保存该条微博图片的 url
                    if item['pic_num'] > 0:
                        pic_dict = statuse.get('pic_infos')
                        print('pic_dict:',pic_dict)
                        for i in pic_dict:
                            pic_url = pic_dict[i]['original']['url']
                            item['pic'].append(pic_url)
                    else:
                        pass

                    isLongText = statuse.get('isLongText')  #是否长文本，True时可展开
                    mblogid = statuse.get('mblogid') #长文本id

                    item['mblogid']  = statuse.get('mblogid') #评论数
                    item['isLongText']  = statuse.get('isLongText') #点赞数

                    url = self.longText_url.format(mblogid)
                    if isLongText == True:
                        print(url, isLongText)
                        #json_longtext = self.get_response_json(_longText_url)
                        #item['text'] = json_longtext.get('data').get('longTextContent')

                        yield scrapy.Request(
                            url=url,
                            callback=self.longTextParse,
                            meta={'item': item}
                        )
                    else:
                        yield item

    #长文本接口
    def longTextParse(self,response):
        print(response)
        #print(response.text)
        item = response.meta.get('item')
        data = response.json()
        #print(data)
        if data['http_code'] == 200 and data['ok'] == 1 and data['data']:
            item['text'] = data['data']['longTextContent']
            yield item

    def get_response_json(self,url):
        response = requests.get(url, headers=self.headers)
        print(response.text)
        # json = response.json()
        # return json

