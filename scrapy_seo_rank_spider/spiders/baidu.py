# -*- coding: utf-8 -*-
from urllib import parse
from urllib.parse import urlparse, parse_qs

import scrapy
import re


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?ie=UTF-8&wd=花键磨齿']
    page_num = 1

    def parse(self, response):
        cards = response.xpath('//div[@id="content_left"]//div[@tpl="se_com_default"]')
        page_index = 1
        page_url = response.url
        urldict = urlparse(response.url)
        query = parse.unquote(urldict.query)
        res = dict([(k, v[0]) for k, v in parse_qs(query).items()])
        keyword = res['wd']
        for card in cards:
            title = card.xpath('./h3[@class="t"]//text()').getall()
            title = ''.join(title)
            baidu_index = card.xpath('./@id').get()
            text = card.xpath('.//a[@class="c-showurl"]//text()').getall()
            text = ''.join(text)
            text = re.sub(r"\s*\.[^{]+\{[^}]*\}", '', text)
            path = card.xpath('.//a[@class="c-showurl"]/@href').get()
            print(title)
            page_index += 1
        self.page_num += 1

        next_page_url = response.xpath('//div[@id="page"]/a[@class="n"][last()]/@href').get()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url,callback=self.parse)
