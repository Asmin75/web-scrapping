import scrapy
from ..items import QoutetutorialItem


class QouteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        "http://quotes.toscrape.com/"
    ]


    def parse(self, response):
        for quotes in response.css('div.quote'):
            item_title = quotes.css('span.text::text').extract()
            item_author = quotes.css('.author::text').extract()
            item_tag = quotes.css('.tag::text').extract()
            quoteItem = QoutetutorialItem(title=item_title, author=item_author, tag=item_tag)
            yield quoteItem
