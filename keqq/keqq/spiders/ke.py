# -*- coding: utf-8 -*-
import scrapy
import logging



class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']

    def parse(self, response):
        result = response.body.decode('utf-8', 'ignore')
        # print(result)
        logging.log(logging.WARNING, "----" * 200)
        logging.log(logging.WARNING, "###: " + result)
        logging.log(logging.WARNING, "----" * 200)
        # result = response.xpath("//h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract()
        # print('#####', result)
