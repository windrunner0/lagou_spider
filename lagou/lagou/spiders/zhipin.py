# -*- coding: utf-8 -*-
import scrapy


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['http://www.zhipin.com/']

    def parse(self, response):
        detail_urls = response.css('div.info-primary a::attr(href),tr.odd a::attr(href)').extract()
         for url in detail_urls:
            #fullurl = 'http://hr.tencent.com/' + url
            #构建绝对的url地址，效果同上（域名加相对地址）
            fullurl = response.urljoin(url)
            print(fullurl)
