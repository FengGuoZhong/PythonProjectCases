# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibospiderItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field()
    screen_name = scrapy.Field()
    weibo_id = scrapy.Field()
    created_at = scrapy.Field()
    region_name = scrapy.Field()
    source = scrapy.Field()
    text_raw = scrapy.Field()
    text = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()
    attitudes_count = scrapy.Field()
    pic_num = scrapy.Field()
    pic = scrapy.Field()
    mblogid = scrapy.Field()
    isLongText = scrapy.Field()

