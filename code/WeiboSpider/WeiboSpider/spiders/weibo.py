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
        "Cookie": "SINAGLOBAL=4762606171177.985.1692773258306; ULV=1692837930006:2:2:2:5391596155029.152.1692837929986:1692773258359; wb_view_log=1366*7681; un=15010046492; WBPSESS=Dt2hbAUaXfkVprjyrAZT_H2W169NZ9goB0dG_NoS6qox_9-zpr3ehwWnEYU4mmgKD89pBfgW8tOG44FHW5bBRe6IeD6EZm0SDK08T0U-PA--nxYI3ZkJ2DHvJ3QRwFNaGSvve-XiK5VJnVn-HsUDdrLc-dghtv5troELV5oNHQuVO3czUtPvJ2hdw8D3OtIkrmj6e2zjUHc_nKhddNAICQ==; XSRF-TOKEN=rpwdNNajpbs9LsvvDMb51xzE; SSOLoginState=1692867003; SCF=AnO8qNvlaAiHidL4B8fB4F0oCWjzpgNDNgUQukbawRjJJREmrtrtDgm7n2WBZu6_BolBa2hIwS-e6GsfXUAioV0.; SUB=_2A25J42m8DeRhGeNN41IW-S7Myz2IHXVqmdx0rDV8PUNbmtANLU7mkW9NSYb7hheoeV5tWbSQXm5XtZwLWmyiVy2E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W57gP.kESaXpCF-Mjad2-9l5JpX5KzhUgL.Fo-01h5N1K57eh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMfe0n7S0.7eh5p; ALF=1724403051",
        "X-Requested-With": "XMLHttpRequest",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Ch-Ua-Dest": "document",
        "Sec-Ch-Ua-Site": "none",
        "Sec-Ch-Ua-User": "?1",
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
                for statuse in data['statuses']:
                    screen_name = statuse['user']['screen_name'] #发布人
                    created_at = statuse['created_at'] #发布时间
                    text_raw = statuse['text_raw'] #内容
                    text = statuse['text']
                    reposts_count = statuse['reposts_count'] #转发数
                    comments_count = statuse['comments_count'] #评论数
                    attitudes_count = statuse['attitudes_count'] #点赞数
                    isLongText = statuse['isLongText'] #长文本
                    mblogid = statuse['mblogid']

                    item = WeibospiderItem()
                    item['screen_name'] = screen_name
                    item['created_at'] = created_at
                    item['text_raw'] = text_raw
                    item['text'] = pq(text).text()
                    item['reposts_count'] = reposts_count
                    item['comments_count'] = comments_count
                    item['attitudes_count'] = attitudes_count
                    item['isLongText'] = isLongText
                    item['mblogid'] = mblogid
                    #print(item)

                    #yield item


                    _longText_url = self.longText_url.format(mblogid)


                    if isLongText == True:
                        print(_longText_url, isLongText)
                        json_longtext = self.get_response_json(_longText_url)
                        #item['text'] = json_longtext.get('data').get('longTextContent')

                        # yield scrapy.Request(
                        #     url='https://weibo.com/ajax/statuses/longtext?id=Ng2C2ts5s',
                        #     callback=self.longTextParse,
                        #     meta={'item': item},
                        #     headers = self.headers
                        #
                        # )
                    else:
                        yield item


    def longTextParse(self,response):
        print(response)
        print(response.text)
        # item = response.meta.get('item')
        # print(item)
        # data = response.json()
        # if data['http_code'] == 200 and data['ok'] == 1:
        #     item['longTextContent'] = data['data']['longTextContent']
        #     yield item

    def get_response_json(self,url):
        response = requests.get(url, headers=self.headers)
        print(response.text)
        # json = response.json()
        # return json

