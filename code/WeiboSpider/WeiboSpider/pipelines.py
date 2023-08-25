# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class WeibospiderPipeline:

    def open_spider(self,spider):
        print('爬虫开始')
        # self.file_obj = open('db.txt',mode='a',encoding='utf-8',newline='')

    def process_item(self, item, spider):
        # print('打印:')
        # print(item)
        #存文件
        # self.file_obj.write(json.dumps(dict(item),ensure_ascii=False)+'\n')
        return item

    def close_spider(self,spider):
        print('爬虫结束')
        # self.file_obj.close()


