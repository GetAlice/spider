# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebascrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tie_name = scrapy.Field()
    tie_link = scrapy.Field()
    tie_huifu = scrapy.Field()
    tie_create_time = scrapy.Field()
