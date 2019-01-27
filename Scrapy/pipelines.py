# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import psycopg2
import pymongo
from datetime import datetime
import uuid

class ScrapyPipeline(object):

    def __init__(self, mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
      
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        #algunos productos no tienen sku, le genero uno
        if item['sku'] is None:
            unique_id = uuid.uuid1()
            item['sku'] = 'SS-'+str(unique_id)

        #busco si el sku escaneado está en la BD
        producto = self.db.lista_productos.find_one({"sku_producto":item['sku']})

        if producto is None:#si no está, lo inserto
            id_producto = self.db.lista_productos.insert_one({"codigo_supermercado":item['supermercado'],"sku_producto":item['sku'],"nombre_producto":item['nombre'],"descripcion_producto":item['descripcion'],"fecha_registro":str(datetime.now())}).inserted_id
            self.db.precio_productos.insert_one({"id_producto":id_producto,"precio_normal":item['precio_normal'],"precio_oferta":item['precio_oferta'],"fecha_registro":str(datetime.now())})
        else:
            self.db.precio_productos.insert_one({"id_producto":producto['_id'],"precio_normal":item['precio_normal'],"precio_oferta":item['precio_oferta'],"fecha_registro":str(datetime.now())})


        return item
