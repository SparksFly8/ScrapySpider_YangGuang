# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
from YangGuang.settings import MONGO_HOST, MONGO_PORT
from pymongo import MongoClient


class YangguangPipeline(object):
    def open_spider(self, spider):
        '''爬虫开始执行时执行的函数(仅run一次)，可放入数据库连接代码'''
        client = MongoClient(MONGO_HOST, MONGO_PORT)  # 新建MongoDB客户端实例
        self.col = client['YangGuang']['content']     # 新建数据库为YangGuang，集合为content的实例

    def process_item(self, item, spider):
        item['contentext'] = self.process_content(item['contentext']) # 清洗item中content数据
        self.col.insert_many([dict(item)])     # 向MongoDB中插入数据
        # print(item['href'])
        return item

    def process_content(self, content):
        '''对content数据进行清洗，去除空白字符等不必要的数据'''
        if content == []:  # 如果content是空列表，说明详细页面响应404
            return None
        # 使用列表切片和sub替换，逐个清洗数据中的空格、\t、\n和\xa0等任意空白字符
        content = [re.sub('\s', '', item) for item in content]
        # 将含有多个字段的列表连接成只有一个字段的列表
        content = ''.join(content)
        return content
