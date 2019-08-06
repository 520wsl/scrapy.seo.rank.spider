# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baiud.com']
    start_urls = ['http://baiud.com/']

    def parse(self, response):
        print(response)
        pass
