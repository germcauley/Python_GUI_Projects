# -*- coding: utf-8 -*-
import scrapy


class BoibotSpider(scrapy.Spider):
    name = 'boibot'
    allowed_domains = ['www.bankofireland.com/']
    start_urls = ['http://www.bankofireland.com//']

    def parse(self, response):
        pass
