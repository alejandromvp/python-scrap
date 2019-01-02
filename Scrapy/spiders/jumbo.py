# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem;
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from urllib.parse import urlparse



class JumboSpider(scrapy.Spider):
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'LOG_FILE': 'error_jumbo.json',
        'LOG_ENABLED': True,
        'LOG_STDOUT': True,
    }
    name = 'jumbo'
    allowed_domains = ['jumbo.cl']
    start_urls = [
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/3/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/5/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/225/"
        ]
    item_count = 0
    base_url = "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0"

    def parse(self, response):
        o = urlparse(response.url)
        fq = o.query.split('&')[5][3:]
        pageNumber = int(o.query.split('&')[4][11:])+1

        nextURL = self.base_url+"&PageNumber="+str(pageNumber)+"&fq="+fq
        if response.body:
            for href in response.xpath('//div[@class="product-item__info"]'):
                url = href.css('a::attr(href)').extract_first()
                request = scrapy.Request(url= url, callback=self.parse_item)
                yield request
            yield scrapy.Request(url = nextURL, callback=self.parse)


    def parse_item(self, response):
        producto = ScrapyItem()
        titulo = response.xpath('//title/text()').extract_first()
        nombre = titulo.split('|')[0].strip()
        producto['nombre'] = nombre
        producto['sku'] = response.xpath('//div[@class="skuReference"]/text()').extract_first()
        producto['descripcion'] = nombre

        precio_activo = response.xpath('//strong[@class="skuBestPrice"]/text()').extract_first()
        if precio_activo:
            producto['precio_normal'] = int(precio_activo.split('$')[1].strip().split(',')[0].replace('.',''))
            producto['precio_oferta'] = int(precio_activo.split('$')[1].strip().split(',')[0].replace('.',''))
        else:
            producto['precio_normal'] = 0
            producto['precio_oferta'] = 0
 
        producto['supermercado'] = 2

        self.item_count += 1
        print(self.item_count)
        yield producto