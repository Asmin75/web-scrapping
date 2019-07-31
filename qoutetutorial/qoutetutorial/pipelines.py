# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

#scrapped_data -> item_containers -> json/csv_files
#scrapped_data -> item_containers -> pipeline -> SQL/Mongo db

import psycopg2
# from twisted.internet import defer, reactor

class QoutetutorialPipeline(object):

    def open_spider(self, Spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'mypass'
        database = 'postgres'
        self.connection = psycopg2.connect(host=hostname,
                                           user=username,
                                           password=password,
                                           dbname=database)
        self.cur = self.connection.cursor()


    def process_item(self, item, Spider):
        # self.cur.execute("DROP TABLE IF EXISTS quotes_tb")
        # self.cur.execute("""Create table quotes_tb(
        #                 title text,
        #                 author text,
        #                 tag text
        #                 )""")
        self.cur.execute("insert into quotes_tb(title,author,tag) values (%s,%s,%s)",
                         (item['title'], item['author'], item['tag']))
        self.connection.commit()
        return item
        # dfd = defer.Deferred()
        # dfd.addCallback(self.write_item)
        # reactor.callLater(0, dfd.callback, item)
        # return dfd

    # def write_item(self, item):
    #     self.cur.execute("insert into quotes_tb(title,author,tag) values (%s,%s,%s)",
    #                      (item.get('title'), item.get('author'), item.get('tag')))
    #     # self.connection.commit()
    #     return item

    def close_spider(self, Spider):
        self.cur.close()
        self.connection.close()
