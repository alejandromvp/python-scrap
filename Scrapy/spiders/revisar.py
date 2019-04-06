# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem
from scrapy.http import FormRequest
from urllib.parse import urlparse
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

""" se harán 3 archivos para revisar, uno por cada supermercado
esto será para saber si hay algún producto que ya no esté disponible, o alguno que no 
estaba disponible y volvió a estarlo. Para eso hay que buscar la forma de ver como funcionan
las páginas cuando no se encuentra una URL en específico, que esta URL sería la que no está disponible.
El archivo revisa-categorias.py que está en el servidor era solamente para revisar los productos que se 
habían agregado antes y no tenían categorías o url, se le dejó una url por defecto. Así que no hay que revisar esas URL, ese archivo ya no se usará ya que desde ahora todos los productos vienen con una url, una categoría y su estado en verdadero, ese estado sólo se cambiará desde los archivos de revisar si es que no se encuentra la URL"""

class RevisarSpider(scrapy.Spider):
    name = 'revisar'
    client = MongoClient('mongodb://localhost:27017')
    db = client['supermercados']
    cursor = db.lista_productos.find({})
    start_urls = []
    for prod in cursor:
        start_urls.append(prod['url_producto'])
            
    #print(productos)    

    def parse(self, response):
        print(response)
        #pass