# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Paiza_2.items import Paiza2Item


class Paiza2SpiderSpider(CrawlSpider):
    name = 'paiza_2_spider'
    allowed_domains = ['paiza.jp']
    start_urls = ['https://paiza.jp/career/job_offers/dev_language/Python3?page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+Python3\?page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'.+job_offers/\d{4}'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
       name = response.xpath("//h2[@id='corpname']/text()").get()
       content = response.xpath("//div[@class='rBox font13 lineHeight17']//p/text()").getall()
       content = "".join(content).strip()
       item=Paiza2Item(name=name, content=content)
       yield item

