#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:46:16 2017

@author: ubuntu
"""


import scrapy


class TanktruckFleetSpider(scrapy.Spider):
    name = 'tankTruckFleet'
    allowed_domains = ['www.tanktruck.org/about/membership/fleet-member-directory']
    start_urls = ['http://www.tanktruck.org/about/membership/fleet-member-directory']

    def parse(self, response):
        allRows = response.xpath('//tr')
        allRows = allRows[1:]
        for row in allRows:
            companyUrl= row.xpath('./td/a/@href').extract_first()
            companyName = row.xpath('./td/a/text()').extract_first()
            restOftheCols = row.xpath('./td/text()').extract()
            city = restOftheCols[0] if restOftheCols[0] else ''
            state = restOftheCols[1] if restOftheCols[1] else ''
            yield {
                   "url": companyUrl,
                   "companyName": companyName,
                   "city": city,
                   "state": state
                   }

