# -*- coding: utf-8 -*-
import scrapy


class TiebaspiderSpider(scrapy.Spider):
    name = 'tiebaspider'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/']

    def parse(self, response):
        pass
