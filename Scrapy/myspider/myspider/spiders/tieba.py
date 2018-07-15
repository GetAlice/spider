# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Scrapy.myspider.myspider.items import MyspiderItem


class TiebaSpider(CrawlSpider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%A2%A7%E8%93%9D%E8%88%AA%E7%BA%BF&ie=utf-8&pn=0']
    page_link = LinkExtractor(allow=('pn=\d+'))

    rules = (
        #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(page_link,callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        i = {}
        item = MyspiderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        for each in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            #print(each)
            tie_name = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a')
            print(tie_name)
        #return i
