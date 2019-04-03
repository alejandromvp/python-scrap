# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem
from scrapy.http import FormRequest
from urllib.parse import urlparse
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId



class RevisarSpider(scrapy.Spider):
    name = 'revisar'
    client = MongoClient('mongodb://localhost:27017')
    db = client['supermercados']
    cursor = db.lista_productos.find({})
    start_urls = []
    for prod in cursor:
        if prod['url_producto'] is not None:
            start_urls.append(prod['url_producto'])
        else:
            start_urls.append("http://ayndemos.com")
            
    #print(productos)    

    def parse(self, response):
        print(response)
        #pass