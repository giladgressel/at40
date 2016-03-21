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
    url.extend(['http://www.at40.com/top-40/most-recent'])

    print url

    start_urls = url
    # start_urls = ['http://www.at40.com/top-40/2012/01']

    def parse(self, response):
        items = []
        year = response.xpath("//*[@id='categories']/h2/text()").extract()
        table = response.xpath('//*[@id="chartintlist"]')

        # //*[@id="chartintlist"]/tbody/tr[1]/td[2]/time/


        for things in table:
            artists_titles_1 = things.xpath("tr[2]/td[1]/text()").extract()
            artists_titles_2 = things.xpath('tr[2]/td[2]/text()').extract()
            week = things.xpath('tr[1]/td[2]/time/a/text()').extract()
            for a_t in artists_titles_1:
                item = At40Item()
                item["artist_title"] = a_t
                item['year'] = year
                item['week'] = week
                items.append(item)
            for a_t in artists_titles_2:
                item = At40Item()
                item['artist_title'] = a_t
                item['year'] = year
                item['week'] = week
                items.append(item)



        # for a_i in artists_titles:
        #     item = At40Item()
        #     item["artist_title"] = a_i
        #     item['year'] = year
        #     item['week'] = week
        #     items.append(item)


        return items













