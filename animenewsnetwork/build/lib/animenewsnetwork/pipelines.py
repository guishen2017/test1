# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import time
class AnimenewsnetworkPipeline(object):

    def __init__(self, host, db):
        self.host = host
        self.db = db

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('mongodb://admin:admin123@localhost:27017/')
        self.animenews = self.client[self.db]

    def process_item(self, item, spider):
        self.animenews['content'].insert(dict(item))
        # item = dict(item)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host = crawler.settings.get("MONGO_DB"),
            db = crawler.settings.get("MONGO_DBNAME")
        )

    def close_spider(self, spider):
        self.client.close()

class AnimenewsnetworkDataPipeline(object):

    def process_item(self, item, spider):
        image_url_list = []
        for image_url in item['images_urls']:
            if ".gif" not in image_url:
                image_url_list.append(image_url)
        item['images_urls'] = image_url_list
        return item

