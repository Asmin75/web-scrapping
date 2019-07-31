# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

#scrapped_data -> item_containers -> json/csv_files

import scrapy


class QoutetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()

