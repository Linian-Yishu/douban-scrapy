# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class DoubanspiderPipeline(object):
    def __init__(self):
        #获取mongo数据
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        #连接
        client = pymongo.MongoClient(host=host, port=port)
        #指向指定的数据库
        mdb = client[dbname]
        #获取数据库里存放数据的表名
        self.post = mdb[settings['MONGODB_TABLE']]


    def process_item(self, item, spider):
        data = dict(item)
        #添加数据
        self.post.insert(data)
        return item
