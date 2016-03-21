# -*- coding: utf-8 -*-
import scrapy

def url_creator(year):
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    stock_url = 'http://www.at40.com/top-40/{}/{}'
    return [stock_url.format(year,month) for month in months]

class Top40Spider(scrapy.Spider):
    name = "top40"
    allowed_domains = ["at40.com"]

    url = url_creator(2012)
    url.extend(url_creator(2013))
    url.extend(url_creator(2014))
    url.extend(url_creator(2015))

    start_urls = url

    def parse(self, response):
        pass



