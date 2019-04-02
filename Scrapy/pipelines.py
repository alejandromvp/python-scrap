# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import psycopg2
import pymongo
from datetime import datetime
import uuid
from bson.objectid import ObjectId

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
        self.lider = self.db.lista_supermercados.find_one({"id_supermercado":1})
        self.jumbo = self.db.lista_supermercados.find_one({"id_supermercado":2})
        self.tottus = self.db.lista_supermercados.find_one({"id_supermercado":3})

      
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        #algunos productos no tienen sku, le genero uno
        if item['sku'] is None:
            unique_id = uuid.uuid1()
            item['sku'] = 'SS-'+str(unique_id)

        if item['supermercado'] == 1:
            supermercado = self.lider['_id']
        elif item['supermercado'] == 2:
            supermercado = self.jumbo['_id']
        else:
            supermercado = self.tottus['_id']

        #busco si el sku escaneado está en la BD
        producto = self.db.lista_productos.find_one({"sku_producto":item['sku'],"codigo_supermercado":supermercado})
        categoria = self.db.categorias.find_one({"nombre_categoria":item['categoria']})

        if producto is None:#si no está, lo inserto
            id_producto = self.db.lista_productos.insert_one({"codigo_supermercado":supermercado,"sku_producto":item['sku'],"nombre_producto":item['nombre'],"descripcion_producto":item['descripcion'],"categoria_producto":categoria['_id'],"fecha_registro":str(datetime.now()),"estado_producto":True,"url_producto":item['url']}).inserted_id

            self.db.precio_productos.insert_one({"id_producto":id_producto,"precio_normal":item['precio_normal'],"precio_oferta":item['precio_oferta'],"fecha_registro":str(datetime.now())})
        else:
            #sacar cuando todos los productos tengan categoría
            self.db.lista_productos.update_one({"_id":ObjectId(producto['_id'])},{"$set":{"categoria_producto":categoria['_id'],"estado_producto":True,"url_producto":item['url']}})

            self.db.precio_productos.insert_one({"id_producto":producto['_id'],"precio_normal":item['precio_normal'],"precio_oferta":item['precio_oferta'],"fecha_registro":str(datetime.now())})
        return item
