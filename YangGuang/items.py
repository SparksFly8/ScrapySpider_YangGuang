# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    title = scrapy.Field()        # 标题
    department = scrapy.Field()   # 负责部门
    status = scrapy.Field()       # 处理状态
    publish_date = scrapy.Field() # 发布时间
    href = scrapy.Field()         # 详情页面超链接

    contentext = scrapy.Field()   # 详情页面投诉文本内容
    img = scrapy.Field()          # 详情页面投诉图片内容
