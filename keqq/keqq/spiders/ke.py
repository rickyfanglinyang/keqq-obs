# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.http import Request
from lxml import etree




class KeSpider(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['ke.qq.com']
    start_urls = ['http://ke.qq.com/']
    print("before parse###")

    def parse(self, response):
        print("This is the end of code --------------------------")
        # result = response.body.decode('utf-8', 'ignore')
        print(response.xpath("//title/text()").extract())
        # print('what is the result: ',result)
        # logging.log(logging.WARNING, "----" * 200)
        # logging.log(logging.WARNING, "###: " + result)
        # logging.log(logging.WARNING, "----" * 200)

        key = "python"
        for i in range(1,2):
            url = "https://ke.qq.com/course/list/"+str(key)+"?page="+str(i)
        
        yield Request(url=url, callback=self.page)


    def page(self, response):
        # response.xpath("//h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract()
        course_name  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/h4[@class='item-tt']/a[@class='item-tt-link']/text()").extract()
        sold_count  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()").extract()
        price  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()").extract()
        sold_by  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()").extract()

        list_courses = []
        
        # #Get count for selectors 
        # record_num = len(response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']"))
        # s_record_num = len(response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='line-cell item-user']"))
        # p_record_num = len(response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']"))


        # print("Number of selectors ##", record_num)

        # for i  in range(1,record_num + 1):
        #     course_name  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/h4[@class='item-tt']/a[@class='item-tt-link']/text()")[i].extract()
        #     if s_record_num > 0:
        #         sold_count  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='line-cell item-user']/text()")[i].extract()
        #     else:
        #         sold_count = 0
            
        #     if p_record_num > 0:
        #         price  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--bottom']/span[@class='line-cell item-price']/text()")[i].extract()
        #     else:
        #         price = 0

        #     sold_by  = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']/div[@class='item-line item-line--middle']/span[@class='item-source']/a[@class='item-source-link']/text()")[i].extract()
            
        #     a_course = []
        #     a_course.append(course_name)
        #     a_course.append(sold_count)
        #     a_course.append(price)
        #     a_course.append(sold_by)

        #     logging.log(logging.WARNING, "####" * 200)
        #     logging.log(logging.WARNING, a_course)
        #     logging.log(logging.WARNING, "----" * 200)

        #     list_courses.append(a_course)



        # logging.log(logging.WARNING, "###All Courses###")
        # logging.log(WARNING,list_courses)      






            # logging.log(logging.WARNING, "####" * 200)
            # logging.log(logging.WARNING, course_name)
            # logging.log(logging.WARNING, sold_count)
            # logging.log(logging.WARNING, price)
            # logging.log(logging.WARNING, sold_by)
            # logging.log(logging.WARNING, "----" * 200)

            # print(course_name)
            # print(sold_count)
            # print(price)
            # print(sold_by)


        # print(list_courses)
        result = response.xpath("//ul[@class='course-card-list']/li[@class='course-card-item']")
        doc = etree.fromstring(str(result))        





# atags = doc.xpath('//a')
# for a in atags:
#     btags = a.xpath('b')
#     for b in btags:
#             print b

