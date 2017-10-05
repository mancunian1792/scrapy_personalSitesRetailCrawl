# -*- coding: utf-8 -*-
import scrapy


class TanktruckSpider(scrapy.Spider):
    name = 'tankTruck'
    allowed_domains = ['www.tanktruck.org/about/membership/carriers-member-directory']
    start_urls = ['http://www.tanktruck.org/about/membership/carriers-member-directory/']

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