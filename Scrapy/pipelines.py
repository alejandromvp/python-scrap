# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import psycopg2
import pymongo
from datetime import datetime

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
        """hostname='localhost'
        username='postgres'
        password='226264nicolas'
        database='supermercados'
        self.connection = psycopg2.connect(host=hostname,user=username,password=password,dbname=database)
        self.cur = self.connection.cursor()"""

    def close_spider(self, spider):
        """self.cur.close()
        self.connection.close()"""
        self.client.close()

    def process_item(self, item, spider):
        """self.cur.execute("INSERT INTO lista_productos(codigo_supermercado,sku_producto, nombre_producto,descripcion_producto) SELECT * FROM (SELECT %s,%s, %s, %s) AS tmp WHERE NOT EXISTS (SELECT sku_producto FROM lista_productos WHERE sku_producto = %s and codigo_supermercado= %s) LIMIT 1",(item['supermercado'],item['sku'],item['nombre'],item['descripcion'],item['sku'],item['supermercado']))
        self.connection.commit()
        self.cur.execute("insert into precios_productos(sku_producto,codigo_supermercado,precio_normal,precio_oferta) values(%s,%s,%s,%s)",(item['sku'],item['supermercado'],item['precio_normal'],item['precio_oferta']))
        self.connection.commit()"""
        if item['sku'] is None:
            self.db.lista_productos.insert_one({"codigo_supermercado":item['supermercado'],"sku_producto":"SIN SKU","nombre_producto":item['nombre'],"descripcion_producto":item['descripcion']})
        else:
            key = {"codigo_supermercado":item['supermercado'],"sku_producto":item['sku']}
            data = {"codigo_supermercado":item['supermercado'],"sku_producto":item['sku'],"nombre_producto":item['nombre'],"descripcion_producto":item['descripcion']}
            self.db.lista_productos.replace_one(key,data,upsert=True)

        self.db.precio_productos.insert_one({"sku_producto":item['sku'],"codigo_supermercado":item['supermercado'],"precio_normal":item['precio_normal'],"precio_oferta":item['precio_oferta'],"fecha_registro":str(datetime.now())})
        return item
