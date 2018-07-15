# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class TiebascrapyPipeline(object):
    #def process_item(self, item, spider):
    #   return item
    def __init__(self):
        self.filename = open('tieba.json','wb+')

    def process_item(self,item,spider):
        json_test = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.filename.write(json_test.encode('utf-8'))

    def close_spider(self,spider):
        self.filename.close()