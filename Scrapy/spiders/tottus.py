# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem;
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse


class TottusSpider(CrawlSpider):
    name = 'tottus'
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'LOG_FILE': 'error_tottus.json',
        'LOG_ENABLED': True,
        'LOG_STDOUT': True,
    }
    allowed_domains=['www.tottus.cl']
    categoria = ''
    
    start_urls = [
        'http://www.tottus.cl/tottus/productListFragment/Conservas/118.8?No=0&Nrpp=70&currentCatId=118.8&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Aceites-y-Vinagres/118.2?No=0&Nrpp=30&currentCatId=118.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Pastas-y-Salsas/118.5?No=0&Nrpp=100&currentCatId=118.5&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Arroz-y-Legumbres/118.3?No=0&Nrpp=40&currentCatId=118.3&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Condimentos-y-Aderezos/118.16?No=0&Nrpp=100&currentCatId=118.16&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Harinas,-Puré-y-Sopas/118.6?No=0&Nrpp=40&currentCatId=118.6&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Alimentos-Saludables/118.13?No=0&Nrpp=30&currentCatId=118.13&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cóctel-y-Snacks/118.1?No=0&Nrpp=100&currentCatId=118.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Leches-Líquidas/118.10?No=0&Nrpp=70&currentCatId=118.10&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Leche-en-Polvo/cat370016?No=0&Nrpp=60&currentCatId=cat370016&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cereales/116.6?No=0&Nrpp=70&currentCatId=116.6&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Café-y-Té/116.1?No=0&Nrpp=80&currentCatId=116.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Azúcar-Endulzantes-y-Mermeladas/116.3?No=0&Nrpp=70&currentCatId=116.3&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Panaderia-y-Pasteleria/cat360019?No=0&Nrpp=40&currentCatId=cat360019&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Galletas-Caramelos-y-Chocolates/117.5?No=0&Nrpp=100&currentCatId=117.5&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Colaciones-y-Galletas/116.7?No=0&Nrpp=60&currentCatId=116.7&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Vacuno/127.1?No=0&Nrpp=30&currentCatId=127.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Pollo/127.4?No=0&Nrpp=10&currentCatId=127.4&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Pavo/127.5?No=0&Nrpp=2&currentCatId=127.5&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cerdo/127.2?No=0&Nrpp=6&currentCatId=127.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Fiambrería/113.2?No=0&Nrpp=100&currentCatId=113.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Quesos/112.2?No=0&Nrpp=70&currentCatId=112.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Yoghurt-y-Postres/112.4?No=0&Nrpp=100&currentCatId=112.4&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Mantequillas-y-Huevos/112.1?No=0&Nrpp=20&currentCatId=112.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Frutas/128.1?No=0&Nrpp=10&currentCatId=128.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Verduras/128.2?No=0&Nrpp=40&currentCatId=128.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Frutos-Secos/cat1420059?No=0&Nrpp=10&currentCatId=cat1420059&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Pescado-y-Mariscos/cat360039?No=0&Nrpp=20&currentCatId=cat360039&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Vegetales/111.3?No=0&Nrpp=40&currentCatId=111.3&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Pizzas-y-Comidas/111.5?No=0&Nrpp=20&currentCatId=111.5&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Helados/111.4?No=0&Nrpp=20&currentCatId=111.4&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Carnes-y-pollo/110.1?No=0&Nrpp=40&currentCatId=110.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Hielo/111.1?No=0&Nrpp=1&currentCatId=111.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Bebidas/114.2?No=0&Nrpp=70&currentCatId=114.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Aguas/114.1?No=0&Nrpp=30&currentCatId=114.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Jugos/114.4?No=0&Nrpp=100&currentCatId=114.4&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cervezas/115.1?No=0&Nrpp=50&currentCatId=115.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Licores/115.2?No=0&Nrpp=70&currentCatId=115.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Vinos-Tintos/115.3?No=0&Nrpp=100&currentCatId=115.3&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Vinos-Blancos/115.4?No=0&Nrpp=20&currentCatId=115.4&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Espumantes/115.5?No=0&Nrpp=10&currentCatId=115.5&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-Mujer/120.4?No=0&Nrpp=60&currentCatId=120.4&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-Capilar/120.1?No=0&Nrpp=70&currentCatId=120.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Higiene-Bucal/120.2?No=0&Nrpp=50&currentCatId=120.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Jabones-y-Accesorios/120.3?No=0&Nrpp=20&currentCatId=120.3&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-Hombre/120.5?No=0&Nrpp=30&currentCatId=120.5&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Salud/120.6?No=0&Nrpp=10&currentCatId=120.6&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Papeles/41.1?No=0&Nrpp=30&currentCatId=41.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Limpieza-Ropa/41.2?No=0&Nrpp=40&currentCatId=41.2&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Limpieza-Casa-y-Baños/41.3?No=0&Nrpp=100&currentCatId=41.3&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cocina/cat230046?No=0&Nrpp=50&currentCatId=cat230046&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Accesorios-de-Limpieza/cat230047?No=0&Nrpp=50&currentCatId=cat230047&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Accesorios-del-Hogar/cat2290034?No=0&Nrpp=4&currentCatId=cat2290034&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-y-Salud/121.1?No=0&Nrpp=40&currentCatId=121.1&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Alimento-Bebé/118.17?No=0&Nrpp=20&currentCatId=118.17&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Pañales/cat2280058?No=0&Nrpp=30&currentCatId=cat2280058&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Juguetería/cat2320040?No=0&Nrpp=2&currentCatId=cat2320040&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Electro-y-Tecnología/cat1350044?No=0&Nrpp=5&currentCatId=cat1350044&cat=nada',
        'http://www.tottus.cl/tottus/productListFragment/Mascotas/cat1270016?No=0&Nrpp=40&currentCatId=cat1270016&cat=nada',
    ]

    rules = (      
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//a[@id="next"]')),follow=True,process_links='parentURI'),
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[@class="title"]/a')),callback='parse_item',process_links='childrenURI'),
    )

    def parentURI(self,value):#sacar nombre categoría en URL padre
        for link in value:
            o = urlparse(link.url)
            self.categoria=''
            self.categoria = o.query.split('&')[2][4:]
            yield link

    def childrenURI(self,value):#concatenar categoría a URL hijo
        for link in value:
            link.url = link.url + '&cat='+self.categoria
            yield link

    def parse_item(self, response):
        producto = ScrapyItem()
        nombre = response.xpath('//div[@class="title"]/h5/text()').extract_first()
        producto['nombre'] = nombre.strip()
        producto['sku'] = response.xpath("//input[@class='btn-add-cart']/@value").extract_first()
        producto['descripcion'] = nombre
        precio_activo =  response.xpath('//span[@class="active-price"]/span[1]/text()').extract_first().strip()
        precio_nulo = response.xpath('//span[@class="nule-price"]/text()').extract_first()
        precio_normal=0
        if precio_nulo is None:
            precio_normal = precio_activo
        else:
            precio_normal = precio_nulo.strip()

        producto['precio_normal'] = int(precio_normal[2:].replace(".",""))
        producto['precio_oferta'] = int(precio_activo[2:].replace(".",""))
        producto['supermercado'] = 3
        o = urlparse(response.url)
        producto['categoria']=o.query.split('&')[2][4:]
        producto['url'] = response.url
        yield producto
