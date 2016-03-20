# -*- coding: utf-8 -*-
import scrapy


class Top40Spider(scrapy.Spider):
    name = "top40"
    allowed_domains = ["at40.com"]
    start_urls = (
        'http://www.at40.com/',
    )

    def parse(self, response):
        pass
