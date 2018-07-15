# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tiebascrapy.items import TiebascrapyItem

class TiebaSpider(CrawlSpider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%A2%A7%E8%93%9D%E8%88%AA%E7%BA%BF&ie=utf-8&pn=0']
    page_link = LinkExtractor(allow=('pn=\d+'))

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(page_link, callback='parse_item', follow=False),#True
    )

    def parse_item(self, response):
        i = {}
        item = TiebascrapyItem()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        for each in response.xpath('//li[@class=" j_thread_list clearfix"]'):
            # print(each)
            name = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            if name:
                tie_name = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()[0]
            else:
                tie_name = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a/@title').extract()
            #print(tie_name)


            l = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract()
            if l:
                link = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract()[0]

            else:
                link = each.xpath('.//div[@class="threadlist_title pull_left j_th_tit "]/a/@href').extract()
            if len(link)>0:
                tie_link = 'http://tieba.baidu.com' + link
            else:
                tie_link = ''
            #print(tie_link)



            tie_huifu = each.xpath('.//span[@class="threadlist_rep_num center_text"]/text()').extract()[0]
            #print(tie_huifu)



            tie_create_time = each.xpath('.//span[@class="pull-right is_show_create_time"]/text()').extract()[0]
            #print(tie_create_time)

            item['tie_name']= tie_name
            item['tie_link']= tie_link
            item['tie_huifu']= tie_huifu
            item['tie_create_time']= tie_create_time

            yield item
        # return i
