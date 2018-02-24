# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import *

class TestxxPipeline(object):
    
    def process_item(self, item, spider):
            self.collection.insert(dict(item))
            # print(item)
            return item

        def open_spider(self, spider):
            self.client = MongoClient('113.108.171.5', 27017)
            self.db = self.client['shiyanlou']
            self.collection = self.db['data']

        def close_spider(self, spider):
            pass
