# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrunchyrollItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    images = scrapy.Field()
    videos = scrapy.Field()
    description = scrapy.Field()

    author = scrapy.Field()
    posted_on = scrapy.Field()
    crawl_time = scrapy.Field()
    source_url = scrapy.Field()
