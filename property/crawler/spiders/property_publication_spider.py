# -*- coding: utf-8 -*-
import re
import subprocess
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from cy.items import PropertyItem


class Spider(BaseSpider):
    name = "property"
    allowed_domains = ["sunshine.cy.gov.tw"]
    start_urls = ['http://sunshine.cy.gov.tw/GipOpenWeb/wSite/lp?ctNode=442&mp=2&nowPage=1&pagesize=300']

    def parse(self, response):
        sel = Selector(response)
        items = []
        trs = sel.xpath('//table[@class="lptb3"]/tr')
        for tr in trs:
            tds = tr.xpath('td')
            if tds:
                item = PropertyItem()
                item['journal'] = tds[1].xpath('text()').re(u'\s*(\S+)\s*')[0]
                item['date'] = re.sub('/', '-', tds[2].xpath('text()').extract()[0])
                item['download_url'] = ['http://sunshine.cy.gov.tw/GipOpenWeb/wSite/%s' % link for link in tds[3].xpath('div/a/@href').extract()]
                for link in item['download_url']:
                    cmd = 'wget -c -O data/pdf/journal/%s.pdf %s' % (item['journal'], link)
                    retcode = subprocess.call(cmd, shell=True)
                items.append(item)
        return items
