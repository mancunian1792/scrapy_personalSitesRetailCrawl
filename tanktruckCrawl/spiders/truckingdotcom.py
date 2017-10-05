#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 01:28:15 2017

@author: ubuntu
"""

# -*- coding: utf-8 -*-
# This spider uses selenium to scrape of a page.
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class TruckingSpider(Spider):
    name = 'truckingDotOrg'
    header = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1"
    allowed_domains = ['http://trucking.org/MemberDirectory.aspx']
    
    def start_requests(self):
        self.driver = webdriver.Chrome('/home/ubuntu/Documents/chromedriver')
        self.driver.get('http://trucking.org/MemberDirectory.aspx')
        sel = Selector(text=self.driver.page_source)
        truckCompanies = sel.xpath('//*[@class="span9 col"]/article')
        
        for comp in truckCompanies:
            url = comp.xpath('./div[2]/span/a/@href').extract_first()
            name = comp.xpath('./div[2]/span/a/text()').extract_first()
            phoneNum = comp.xpath('./div[2]/span/text()').extract_first()
            yield {
                   "url": url,
                   "companyName": name,
                   "phoneNum": phoneNum
                       } 
                       
        while True:
            try:
                next_page = self.driver.find_element_by_xpath('//*[@class="span9 col"]/div[contains(@class,"row-fluid")]/span/div[3]/input[1]')
                sleep(3)
                self.logger.info('Sleeping for 3 seconds')
                next_page.click()
                sel = Selector(text=self.driver.page_source)
                truckCompanies = sel.xpath('//*[@class="span9 col"]/article')
        
                for comp in truckCompanies:
                    url = comp.xpath('./div[2]/span/a/@href').extract_first()
                    name = comp.xpath('./div[2]/span/a/text()').extract_first()
                    phoneNum = comp.xpath('./div[2]/span/text()').extract_first()
                    yield {
                           "url": url,
                           "companyName": name,
                           "phoneNum": phoneNum
                           } 
        
            except NoSuchElementException:
                self.logger.info('No more pages to log')
                self.driver.quit()
                break