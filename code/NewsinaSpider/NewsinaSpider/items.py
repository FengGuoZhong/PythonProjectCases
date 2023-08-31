# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsinaspiderItem(scrapy.Item):
    # define the fields for your item here like:
    oid = scrapy.Field()
    title = scrapy.Field()
    intro = scrapy.Field()
    media_name = scrapy.Field()
    keywords = scrapy.Field()
    ctime = scrapy.Field()
    url = scrapy.Field()
    wapurls = scrapy.Field()
    content = scrapy.Field()
