# Scrapy settings for WeiboSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'WeiboSpider'

SPIDER_MODULES = ['WeiboSpider.spiders']
NEWSPIDER_MODULE = 'WeiboSpider.spiders'

LOG_LEVEL = 'WARNING'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WeiboSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'Referer':'https://weibo.com/newlogin?tabtype=weibo&gid=102803&openLoginLayer=0&url=https%3A%2F%2Fweibo.com%2F',
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
   #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
   'Cookie': 'SINAGLOBAL=4762606171177.985.1692773258306; un=15010046492; ULV=1693290767002:3:3:1:1149081069544.251.1693290766999:1692837930006; WBPSESS=Dt2hbAUaXfkVprjyrAZT_FIivS-p7Sv3G4yuvSnulja73PCxWkqPBXxKLDufEZHNHgxWfHWgYqxVLsaGkID_c-2jbQW2jO0h7AdoXCwx_Yt0kViUOiczrMqS3ozfFuClK56MQnBeAAIXcLW4Xlx_an9uwQ80Fs9_VTaBuSBKHuktCOhDeAIZYiDJrPEbHQYK7d21iJV5DcfBttwwwuxmxg==; XSRF-TOKEN=JZCLv30CKfxOu9onbBeFQV3u; SSOLoginState=1693356715; SCF=AnO8qNvlaAiHidL4B8fB4F0oCWjzpgNDNgUQukbawRjJB08B05FZ1Hu7uuPeONDIzhY7Z4axc7SSXsB-7FCspFc.; SUB=_2A25J6uL7DeRhGeNN41IW-S7Myz2IHXVqnlMzrDV8PUNbmtANLULxkW9NSYb7hkqwKNOnApN_yX7YNa-dABvQPODm; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W57gP.kESaXpCF-Mjad2-9l5JpX5KzhUgL.Fo-01h5N1K57eh22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMfe0n7S0.7eh5p; ALF=1724892715',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'WeiboSpider.middlewares.WeibospiderSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'WeiboSpider.middlewares.WeibospiderDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'WeiboSpider.pipelines.WeibospiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
MYSQL_DB_CONFIG = {
   'HOST':'localhost',
   'PORT':3306,
   'USER':'root',
   'PASSWORD':'123456',
   'DATABASE':'weibo_db',
   'charset':'utf8mb4'
}
