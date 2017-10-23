# -*- coding: utf-8 -*-
import scrapy


class LjHouseSpider(scrapy.Spider):
    name = 'lj_house'
    allowed_domains = ['nj.lianjia.com/ershoufang/']
    start_urls = ['http://nj.lianjia.com/ershoufang//']

    def parse(self, response):
        pass
