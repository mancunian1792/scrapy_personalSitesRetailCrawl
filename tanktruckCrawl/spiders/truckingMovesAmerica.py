# -*- coding: utf-8 -*-
import scrapy


class TruckingmovesamericaSpider(scrapy.Spider):
    name = 'truckingMovesAmerica'
    allowed_domains = ['http://truckingmovesamerica.com/']
    start_urls = ['http://truckingmovesamerica.com/']

    def parse(self, response):
        companies = response.xpath('//*[@class="mtphr-dnt-tick mtphr-dnt-default-tick mtphr-dnt-clearfix "]')
        for company in companies:
            url = company.xpath('./a/@href').extract_first()
            company_name = company.xpath('./a/text()').extract_first()
            yield {
                   "companyName": company_name,
                   "url": url
                   }
            