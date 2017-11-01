# -*- coding: utf-8 -*-
import scrapy


class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']

    def parse(self, response):
        print(response.body.decode('utf-8', 'ignore'))
        
