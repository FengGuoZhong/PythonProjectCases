import scrapy
from WeiboSpider.items import WeibospiderItem
from pyquery import PyQuery as pq
import json

from urllib.parse import urlencode
import requests

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    allowed_domains = ['weibo.com']
    # start_urls = ['http://weibo.com/']

    #model_url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover|new_feed&max_id={}&count=10'
    model_url = 'https://weibo.com/ajax/feed/hottimeline?since_id=0&refresh=0&group_id=102803&containerid=102803&extparam=discover|new_feed&max_id={}&count=10'
    #model_url = 'https://weibo.com/ajax/feed/hottimeline?refresh=2&group_id=102803&containerid=102803&extparam=discover|new_feed&max_id={}&count=10'
    next_model_url = 'https://weibo.com/ajax/feed/hottimeline?refresh=2&group_id=102803&containerid=102803&extparam=discover|new_feed&max_id={}&count=10'
    start_urls = [model_url.format(0)]

    longText_url = 'https://weibo.com/ajax/statuses/longtext?id={}'

    total_count = 0


    def parse(self, response,**kwargs):
        print(response)
        data = response.json()
        if data['ok'] == 1:
            for statuse in data.get('statuses'):

                item = WeibospiderItem()
                self.total_count += 1
                print(self.total_count,statuse.get('id'))
                print('*'*50)
                # 用户信息
                user_info = statuse.get('user')
                item['user_id'] = user_info.get('id')  # 发布人id
                item['screen_name'] = user_info.get('screen_name')  # 发布者昵称

                # 微博信息
                item['weibo_id'] = statuse.get('id')  # 微博id
                item['created_at'] = statuse.get('created_at')  # 发布时间
                item['region_name'] = statuse.get('region_name')  # 发布于
                item['source'] = statuse.get('source')  # 来源
                try:
                    item['text'] = pq(statuse.get('text')).text()  # 微博内容
                except:
                    item['text_raw'] = pq(statuse.get('text_raw')).text()  # 微博内容

                item['reposts_count'] = statuse.get('reposts_count')  # 转发数
                item['comments_count'] = statuse.get('comments_count')  # 评论数
                item['attitudes_count'] = statuse.get('attitudes_count')  # 点赞数

                # 图片
                item['pic_num'] = statuse.get('pic_num')  # 该条微博包含的图片数
                item['pic'] = []  # 用于保存该条微博图片的 url
                if item['pic_num'] > 0:
                    pic_dict = statuse.get('pic_infos')
                    try:
                        for i in pic_dict:
                            pic_url = pic_dict[i]['original']['url']
                            item['pic'].append(pic_url)
                    except:
                        pass

                item['pic_num'] = len(item['pic'])  # 根据实际图片数量来赋值

                # 图片列表转json,列表为空处理
                if item['pic'] == []:
                    item['pic'] = None
                else:
                    item['pic'] = json.dumps(item['pic'])

                isLongText = statuse.get('isLongText')  # 是否长文本，True时可展开
                mblogid = statuse.get('mblogid')  # 长文本id

                # 视频
                item['media_video'] = None
                try:
                    if statuse['page_info']['object_type'] == 'video':
                        item['media_video'] = statuse['page_info']['media_info']['stream_url']
                except:
                    pass

                item['mblogid'] = statuse.get('mblogid')  # 长文本内容id
                item['isLongText'] = statuse.get('isLongText')  # 是否长文本

                url = self.longText_url.format(mblogid)
                if isLongText == True:
                    print(url, isLongText)
                    # json_longtext = self.get_response_json(_longText_url)
                    # item['text'] = json_longtext.get('data').get('longTextContent')

                    yield scrapy.Request(
                        url=url,
                        callback=self.longTextParse,
                        meta={'item': item}
                    )
                else:
                    yield item

        for i in range(1, 100):
            next_url = self.next_model_url.format(i)
            #print(next_url)

            #构建一个新的请求对象
            request = scrapy.Request(
                url=next_url,
                callback=self.parse #回调交给parse获取响应，传递的解析函数的名字
            )
            yield request

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

