# -*- coding: utf-8 -*-
import scrapy
import random
import time
from utils.get_date import get_date_list
from utils.filter_html import filte
from crunchyroll.items import CrunchyrollItem

class CrunSpiderSpider(scrapy.Spider):
    name = 'crun_spider'
    allowed_domains = ['crunchyroll.com']
    start_urls = "http://www.crunchyroll.com/newsfeed/archive/feature/{time}+{hour}%3A{minute}%3A{second}"

    def start_requests(self):
        date_list = get_date_list()
        for date in date_list:
            h = random.randint(1,11)
            m = random.randint(1,59)
            s = random.randint(1,59)
            date = str(date).split()[0]
            url = self.start_urls.format(time=date,hour = h,minute=m, second = s)
            yield scrapy.Request(url=url)

    def parse(self, response):
        detail_urls = response.xpath("//ul[@class='newsfeed']//li/h2/a/@href").getall()
        for url in detail_urls:
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        title = response.xpath('//div[@class="related"]/h2/a/text()').get("")
        content = "".join(response.xpath('//div[@class="contents"][1]//text()').getall())
        content = filte(content)
        images = response.xpath('//div[@class="contents"][1]//img/@src').getall()
        videos = ""
        description = response.xpath('//div[@class="showcrunchynews_article white-wrapper"]/h2/text()').get("")
        author = response.xpath('//div[@class="byline"]/a[@class="text-link"]/text()').get()
        posted_on = response.xpath('//span[@class="post-date"]/text()').get()
        crawl_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        source_url = response.url
        item = CrunchyrollItem()
        item['title'] = title
        item['content'] = content
        item['images'] = images
        item['videos'] = videos
        item['description'] = description
        item['author'] = author
        item['posted_on'] = posted_on
        item['crawl_time'] = crawl_time
        item['source_url'] = source_url
        yield item