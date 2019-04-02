# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyItem(scrapy.Item):
    nombre = scrapy.Field()
    sku = scrapy.Field()
    descripcion = scrapy.Field()
    precio_normal = scrapy.Field()
    precio_oferta = scrapy.Field()
    supermercado = scrapy.Field()
    categoria = scrapy.Field()
    url = scrapy.Field()