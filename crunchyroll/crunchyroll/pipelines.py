# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class CrunchyrollPipeline(object):
    def __init__(self, host, db):
        self.host = host
        self.db = db

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.host)
        self.crunchyroll = self.client[self.db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.crunchyroll['content'].insert(dict(item))
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get("MONGO_DB"),
            db=crawler.settings.get("MONGO_DBNAME")
        )