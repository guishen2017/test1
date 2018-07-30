# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimenewsnetworkItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    images_urls = scrapy.Field()
    video_urls = scrapy.Field()
    description = scrapy.Field()
    posted_at = scrapy.Field()
    author = scrapy.Field()
    crawl_time = scrapy.Field()
    update_time = scrapy.Field()
    source_url = scrapy.Field()
    type = scrapy.Field()
