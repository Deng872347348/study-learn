# scrapy的框架：
# 什么是scrapy:
# 爬虫中封装好的一个明星框架，功能：高性能的持久化存储，异步数据的下载
#
# windows安装：
# mac or linux:pip install scrapy
# windows:
# pip install wheel
# 下载twisted:下载地址：http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
#
# 安装twisted:pip install  Twisted-20.3.0-cp37-cp37m-win_amd64.wh
# pip install pywin32
# pip install scrapy
# 在终端中输入scrapy，没有报错，成功
#
# 创建一个工程：scrapy startproject xxxPrb
# cd xxxPro
# 在spiders子目录中创建一个爬虫文件
#  -scrapy genspider spiderName www.xxx.com
# 执行工程：
#  scrapy crawl spiderName

#输出日志文件
#scrapy crawl spiderName --nolog
# scrapy 持久化存储：
# 基于终端指令：
# 要求：只可以将parse方法的返回值存储到本地的文本文件中
# 注意：持久化存储对应的文本文件的类型只可以为：'json','jsonlines','jl','csv','xml',
# 指令：scrapy crawl xxx -o filePath
# 好处：简单高效便捷
# 缺点：局限性比较强（数据只可以存储到指定后缀的文本文件中）
# 基于管道：
#      编码流程：
# 数据解析
# 在item类
# 将解析的数据封装存储item类型的对象

