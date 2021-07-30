# Scrapy settings for ajax project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ajax'

SPIDER_MODULES = ['ajax.spiders']
NEWSPIDER_MODULE = 'ajax.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ajax (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ajax.middlewares.AjaxSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ajax.middlewares.AjaxDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ajax.pipelines.AjaxPipeline': 300,
#}

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
#修改的地方

#MY_USER_AGENT
MY_USER_AGENT = [
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
]
#DOWNLOADER_MIDDLEWARES
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddleware.useragent.UserAgentMiddleware': None,#这里要设置系统的useragent为None，否者会被覆盖掉
    'ajax.middlewares.AjaxDownloaderMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.cookies.CookiesMiddleware': 700,
}

ITEM_PIPELINES = {
   'ajax.pipelines.AjaxPipeline': 300,
}
#DOWNLOAD_DELAY
DOWNLOAD_DELAY = 1.5
#COOKIE
COOKIE = {
    "user_trace_token": "20171109093921 - c87e4dd6 - 6116 - 4060 - a976 - 38df4f6dfc1c",
    "_ga = GA1": ".2.1308939382.1510191563",
    "LGUID": "20171109093922 - cff5ddb7 - c4ee - 11e7 - 985f - 5254005c3644",
    "JSESSIONID": "ABAAABAAAGGABCBAE8E3FCEFC061F7CF2860681B1BF3D98",
    "X_HTTP_TOKEN": "0f2396abe975f6a09df1c0b8a0a3a258",
    "showExpriedIndex": "1",
    "showExpriedCompanyHome": "1",
    "showExpriedMyPublish": "1",
    "hasDeliver": "12",
    "index_location_city": "% E6 % B7 % B1 % E5 % 9C % B3",
    "TG - TRACK - CODE": "index_user",
    "login": "false",
    "unick": "",
    "_putrc": "",
    "LG_LOGIN_USER_ID": "",
    "_gat": "1",
    "LGSID": "20180720141029 - 99fde5eb - 8be3 - 11e8 - 9e4d - 5254005c3644",
    "PRE_UTM": "",
    "PRE_HOST": "",
    "PRE_SITE": "",
    "PRE_LAND": "https % 3A % 2F % 2Fwww.lagou.com % 2Fzhaopin % 2F",
    "SEARCH_ID": "5ddd3d52f1d94b45820534b397ef21e6",
    "LGRID": "20180720141849 - c455d124 - 8be4 - 11e8 - 9e4d - 5254005c3644",
}
