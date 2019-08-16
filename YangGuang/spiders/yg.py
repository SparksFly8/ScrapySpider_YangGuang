# -*- coding: utf-8 -*-
import scrapy
import random
from YangGuang.items import YangguangItem

class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        '''首页解析函数'''
        tr_list = response.xpath('//div[@class="greyframe"]/table[2]//tr')
        headers = {'User-Agent': self.get_ua()}
        for tr in tr_list:
            item = YangguangItem()
            item['title'] = tr.xpath('.//a/@title').extract_first()
            item['department'] = tr.xpath('.//a[@class="t12h"]/text()').extract_first()
            item['status'] = tr.xpath('.//td[3]/span/text()').extract_first()
            item['publish_date'] = tr.xpath('.//td[last()]/text()').extract_first()
            item['href'] = tr.xpath('.//a[@class="news14"]/@href').extract_first()

            yield scrapy.Request(
                url=item['href'],
                callback=self.parse_detail,  # 指定传入的URL由parse_detail解析函数处理
                meta={'item':item},          # 向parse_detail传递的元数据
                headers=headers,             # 传入包含随机UA的headers
            )

        next_url = response.xpath('//div[@class="pagination"]/a[text()=">"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(
                url=next_url,
                callback=self.parse,
            )

    def parse_detail(self, response):
        '''详情页面解析函数'''
        item = response.meta['item']  # 取出从parse传来的元数据
        img = response.xpath('//div[@class="textpic"]/img/@src').extract_first()  # 获取详情页面的图片地址(不含域名)
        if img is None: # 若获取图片地址失败，则1.该页面仅有文本内容;2.该页面不存在-404
            item['img'] = None
            item['contentext'] = response.xpath('//div[@class="wzy1"]//tr[1]/td[@class="txt16_3"]/text()').extract()
        else:   # 若成功获取图片地址，加上域名前缀，且文本内容xpath如下
            item['img'] = 'http://wz.sun0769.com'+img
            item['contentext'] = response.xpath('//div[@class="contentext"]/text()').extract()

        yield item

    def get_ua(self):
        '''随机生成User-Agent用户代理'''
        first_num = random.randint(55, 76)
        third_num = random.randint(0, 3800)
        fourth_num = random.randint(0, 140)
        os_type = [
            '(Windows NT 6.1; WOW64)', '(Windows NT 10.0; WOW64)', '(X11; Linux x86_64)',
            '(Macintosh; Intel Mac OS X 10_14_5)'
        ]
        chrome_version = 'Chrome/{}.0.{}.{}'.format(first_num, third_num, fourth_num)

        ua = ' '.join(['Mozilla/5.0', random.choice(os_type), 'AppleWebKit/537.36',
                       '(KHTML, like Gecko)', chrome_version, 'Safari/537.36']
                      )
        return ua


