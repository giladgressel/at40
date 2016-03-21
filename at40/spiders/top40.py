# -*- coding: utf-8 -*-
import scrapy
from  at40.items import At40Item

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

    # start_urls = url
    start_urls = ['http://www.at40.com/top-40/2012/01']

    def parse(self, response):
        items = []

        # get the artist_title expath and extract
        artists_titles = response.xpath("//*[@id='chartintlist']/tr[2]/td[1]/text()").extract()
        for a_i in artists_titles:
            item = At40Item()
            item["artist_title"] = a_i
            items.append(item)

        return items













