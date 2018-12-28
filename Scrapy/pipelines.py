# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class ScrapyPipeline(object):
    def open_spider(self, spider):
        hostname='localhost'
        username='postgres'
        password='226264nicolas'
        database='supermercados'
        self.connection = psycopg2.connect(host=hostname,user=username,password=password,dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO lista_productos(codigo_supermercado,sku_producto, nombre_producto,descripcion_producto) SELECT * FROM (SELECT %s,%s, %s, %s) AS tmp WHERE NOT EXISTS (SELECT sku_producto FROM lista_productos WHERE sku_producto = %s and codigo_supermercado= %s) LIMIT 1",(item['supermercado'],item['sku'],item['nombre'],item['descripcion'],item['sku'],item['supermercado']))
        self.connection.commit()
        self.cur.execute("insert into precios_productos(sku_producto,codigo_supermercado,precio_normal,precio_oferta) values(%s,%s,%s,%s)",(item['sku'],item['supermercado'],item['precio_normal'],item['precio_oferta']))
        self.connection.commit()
        return item
