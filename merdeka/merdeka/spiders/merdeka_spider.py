import scrapy
import time
from scrapy.selector import Selector
from merdeka.items import MerdekaItem


class TirtoSpider(scrapy.Spider):
    name = "merdeka"
    allowed_domains = ["merdeka.com"]
    start_urls = [
        "https://www.merdeka.com/berita-hari-ini/",
    ]

    def parse(self, response):
        """ This function parses a property page.

        @url https://www.merdeka.com/berita-hari-ini/
        @returns items
        """

        indeks = Selector(response).xpath('//div[@class="mdk-tag-contln"]')

        for indek in indeks:
            item = MerdekaItem()
            item['title'] = indek.xpath('div[@class="mdk-tag-contln-r2"]/div[@class="mdk-tag-contln-titlebar"]/a/text()').extract()[0]
            item['link'] = "https://www.merdeka.com" + indek.xpath('div[@class="mdk-tag-contln-r2"]/div[@class="mdk-tag-contln-titlebar"]/a/@href').extract()[0]
            item['images'] = indek.xpath('div[@class="mdk-tag-contln-l"]/a/img/@src').extract()[0]
            item['category'] = indek.xpath('div[@class="mdk-tag-contln-r2"]/div[@class="mdk-tag-contln-date"]/span/text()').extract()[0]
            item['date'] = time.strftime("%d/%m/%Y")
            item['desc'] = ""

            yield item
