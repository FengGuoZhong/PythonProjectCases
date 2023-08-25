# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
from twisted.enterprise import adbapi


class WeibospiderPipeline:

    ##初始化连接
    def __init__(self, mysql_config):
        self.host = mysql_config['HOST']
        self.port = mysql_config['PORT']
        self.user = mysql_config['USER']
        self.password = mysql_config['PASSWORD']
        self.database = mysql_config['DATABASE']
        self.charset = mysql_config['charset']
        self.conn = None
        self.cursor = None

    #编写类方法，调用setting配置的mysql，用于连接sql数据库
    @classmethod
    def from_crawler(cls, crawler):
        mysql_config = crawler.settings['MYSQL_DB_CONFIG']
        return cls(mysql_config)

    def open_spider(self, spider):
        print('爬虫开始')
        self.conn = pymysql.Connect(
            host=self.host,
            port=3306,
            user=self.user,
            password=self.password,
            db=self.database,
            charset=self.charset
        )
        print(self.conn)

    def process_item(self, item, spider):
        # 执行sql语句
        self.cursor = self.conn.cursor()
        sql = 'insert into t_weibo (weibo_id,user_id,screen_name,created_at,region_name,source,text,reposts_count,comments_count,attitudes_count,pic_num,pic) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        args = (item['weibo_id'], item['user_id'], item['screen_name'], item['created_at'],item['region_name'], item['source'],item['text'], item['reposts_count'], item['comments_count'], item['attitudes_count'], item['pic_num'],item['pic'])

        #print(sql)
        print(args)
        # 事务处理
        try:
            self.cursor.execute(sql, list(args))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        print('爬虫结束')
        self.cursor.close()
        self.conn.close()
