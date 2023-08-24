# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeibospiderItem(scrapy.Item):
    # define the fields for your item here like:
    screen_name = scrapy.Field()
    created_at = scrapy.Field()
    text_raw = scrapy.Field()
    text = scrapy.Field()
    reposts_count = scrapy.Field()
    comments_count = scrapy.Field()
    attitudes_count = scrapy.Field()
    isLongText = scrapy.Field()
    mblogid = scrapy.Field()

