# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem;
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TottusSpider(CrawlSpider):
    name = 'tottus'
    custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'LOG_FILE': 'error_tottus.json',
        'LOG_ENABLED': True,
        'LOG_STDOUT': True,
    }
    allowed_domains=['www.tottus.cl']
    item_count=0

    start_urls = [
        'http://www.tottus.cl/tottus/productListFragment/Conservas/118.8?No=0&Nrpp=&currentCatId=118.8',
        'http://www.tottus.cl/tottus/productListFragment/Aceites-y-Vinagres/118.2?No=0&Nrpp=&currentCatId=118.2',
        'http://www.tottus.cl/tottus/productListFragment/Pastas-y-Salsas/118.5?No=0&Nrpp=&currentCatId=118.5',
        'http://www.tottus.cl/tottus/productListFragment/Arroz-y-Legumbres/118.3?No=0&Nrpp=&currentCatId=118.3',
        'http://www.tottus.cl/tottus/productListFragment/Condimentos-y-Aderezos/118.16?No=0&Nrpp=&currentCatId=118.16',
        'http://www.tottus.cl/tottus/productListFragment/Harinas,-Puré-y-Sopas/118.6?No=0&Nrpp=&currentCatId=118.6',
        'http://www.tottus.cl/tottus/productListFragment/Alimentos-Saludables/118.13?No=0&Nrpp=&currentCatId=118.13',
        'http://www.tottus.cl/tottus/productListFragment/Cóctel-y-Snacks/118.1?No=0&Nrpp=&currentCatId=118.1',
        'http://www.tottus.cl/tottus/productListFragment/Leches-Líquidas/118.10?No=0&Nrpp=&currentCatId=118.10',
        'http://www.tottus.cl/tottus/productListFragment/Leche-en-Polvo/cat370016?No=0&Nrpp=&currentCatId=cat370016',
        'http://www.tottus.cl/tottus/productListFragment/Cereales/116.6?No=0&Nrpp=&currentCatId=116.6',
        'http://www.tottus.cl/tottus/productListFragment/Café-y-Té/116.1?No=0&Nrpp=&currentCatId=116.1',
        'http://www.tottus.cl/tottus/productListFragment/Azúcar-Endulzantes-y-Mermeladas/116.3?No=0&Nrpp=&currentCatId=116.3',
        'http://www.tottus.cl/tottus/productListFragment/Panaderia-y-Pasteleria/cat360019?No=0&Nrpp=&currentCatId=cat360019',
        'http://www.tottus.cl/tottus/productListFragment/Galletas-Caramelos-y-Chocolates/117.5?No=0&Nrpp=&currentCatId=117.5',
        'http://www.tottus.cl/tottus/productListFragment/Colaciones-y-Galletas/116.7?No=0&Nrpp=&currentCatId=116.7',
        'http://www.tottus.cl/tottus/productListFragment/Vacuno/127.1?No=0&Nrpp=&currentCatId=127.1',
        'http://www.tottus.cl/tottus/productListFragment/Pollo/127.4?No=0&Nrpp=&currentCatId=127.4',
        'http://www.tottus.cl/tottus/productListFragment/Pavo/127.5?No=0&Nrpp=&currentCatId=127.5',
        'http://www.tottus.cl/tottus/productListFragment/Cerdo/127.2?No=0&Nrpp=&currentCatId=127.2',
        'http://www.tottus.cl/tottus/productListFragment/Cordero/127.3?No=0&Nrpp=&currentCatId=127.3',
        'http://www.tottus.cl/tottus/productListFragment/Asados/10.3?No=0&Nrpp=&currentCatId=10.3',
        'http://www.tottus.cl/tottus/productListFragment/Fiambrería/113.2?No=0&Nrpp=&currentCatId=113.2',
        'http://www.tottus.cl/tottus/productListFragment/Quesos/112.2?No=0&Nrpp=&currentCatId=112.2',
        'http://www.tottus.cl/tottus/productListFragment/Yoghurt-y-Postres/112.4?No=0&Nrpp=&currentCatId=112.4',
        'http://www.tottus.cl/tottus/productListFragment/Mantequillas-y-Huevos/112.1?No=0&Nrpp=&currentCatId=112.1',
        'http://www.tottus.cl/tottus/productListFragment/Frutas/128.1?No=0&Nrpp=&currentCatId=128.1',
        'http://www.tottus.cl/tottus/productListFragment/Verduras/128.2?No=0&Nrpp=&currentCatId=128.2',
        'http://www.tottus.cl/tottus/productListFragment/Frutos-Secos/cat1420059?No=0&Nrpp=&currentCatId=cat1420059',
        'http://www.tottus.cl/tottus/productListFragment/Pescado-y-Mariscos/cat360039?No=0&Nrpp=&currentCatId=cat360039',
        'http://www.tottus.cl/tottus/productListFragment/Vegetales/111.3?No=0&Nrpp=&currentCatId=111.3',
        'http://www.tottus.cl/tottus/productListFragment/Pizzas-y-Comidas/111.5?No=0&Nrpp=&currentCatId=111.5',
        'http://www.tottus.cl/tottus/productListFragment/Carnes-y-pollo/110.1?No=0&Nrpp=&currentCatId=110.1',
        'http://www.tottus.cl/tottus/productListFragment/Hielo/111.1?No=0&Nrpp=&currentCatId=111.1',
        'http://www.tottus.cl/tottus/productListFragment/Bebidas/114.2?No=0&Nrpp=&currentCatId=114.2',
        'http://www.tottus.cl/tottus/productListFragment/Aguas/114.1?No=0&Nrpp=&currentCatId=114.1',
        'http://www.tottus.cl/tottus/productListFragment/Jugos/114.4?No=0&Nrpp=&currentCatId=114.4',
        'http://www.tottus.cl/tottus/productListFragment/Cervezas/115.1?No=0&Nrpp=&currentCatId=115.1',
        'http://www.tottus.cl/tottus/productListFragment/Licores/115.2?No=0&Nrpp=&currentCatId=115.2',
        'http://www.tottus.cl/tottus/productListFragment/Vinos-Tintos/115.3?No=0&Nrpp=&currentCatId=115.3',
        'http://www.tottus.cl/tottus/productListFragment/Vinos-Blancos/115.4?No=0&Nrpp=&currentCatId=115.4',
        'http://www.tottus.cl/tottus/productListFragment/Espumantes/115.5?No=0&Nrpp=&currentCatId=115.5',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-Mujer/120.4?No=0&Nrpp=&currentCatId=120.4',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-Capilar/120.1?No=0&Nrpp=&currentCatId=120.1',
        'http://www.tottus.cl/tottus/productListFragment/Higiene-Bucal/120.2?No=0&Nrpp=&currentCatId=120.2',
        'http://www.tottus.cl/tottus/productListFragment/Jabones-y-Accesorios/120.3?No=0&Nrpp=&currentCatId=120.3',
        'http://www.tottus.cl/tottus/productListFragment/Cuidado-Hombre/120.5?No=0&Nrpp=&currentCatId=120.5',
        'http://www.tottus.cl/tottus/productListFragment/Salud/120.6?No=0&Nrpp=&currentCatId=120.6',
        'http://www.tottus.cl/tottus/productListFragment/Papeles/41.1?No=0&Nrpp=&currentCatId=41.1',
        'http://www.tottus.cl/tottus/productListFragment/Limpieza-Ropa/41.2?No=0&Nrpp=&currentCatId=41.2',
        'http://www.tottus.cl/tottus/productListFragment/Limpieza-Casa-y-Baños/41.3?No=0&Nrpp=&currentCatId=41.3',
        'http://www.tottus.cl/tottus/productListFragment/Cocina/cat230046?No=0&Nrpp=&currentCatId=cat230046',
        'http://www.tottus.cl/tottus/productListFragment/Accesorios-de-Limpieza/cat230047?No=0&Nrpp=&currentCatId=cat230047',
        'http://www.tottus.cl/tottus/productListFragment/Bebés-y-Niños/121.1?No=0&Nrpp=&currentCatId=121.1',
        'http://www.tottus.cl/tottus/productListFragment/Alimento-Bebé/118.17?No=0&Nrpp=&currentCatId=118.17',
        'http://www.tottus.cl/tottus/productListFragment/Juguetería/124.6?No=0&Nrpp=&currentCatId=124.6',
        'http://www.tottus.cl/tottus/productListFragment/Electro/34.2?No=0&Nrpp=&currentCatId=34.2',
        'http://www.tottus.cl/tottus/productListFragment/Electrodomésticos/126.2?No=0&Nrpp=&currentCatId=126.2',
        'http://www.tottus.cl/tottus/productListFragment/Libreria/cat660015?No=0&Nrpp=&currentCatId=cat660015',
        'http://www.tottus.cl/tottus/productListFragment/Hogar-y-Aire-Libre/10.1?No=0&Nrpp=&currentCatId=10.1',
        'http://www.tottus.cl/tottus/productListFragment/Accesorios-Perro/119.2?No=0&Nrpp=&currentCatId=119.2',
        'http://www.tottus.cl/tottus/productListFragment/Accesorios-Gato/9.3?No=0&Nrpp=&currentCatId=9.3',
        'http://www.tottus.cl/tottus/productListFragment/Otras-Mascotas/cat320049?No=0&Nrpp=&currentCatId=cat320049',
        'http://www.tottus.cl/tottus/productListFragment/Alimento-Perro/119.1?No=0&Nrpp=&currentCatId=119.1',
        'http://www.tottus.cl/tottus/productListFragment/Alimento-Gato/9.2?No=0&Nrpp=&currentCatId=9.2',
    ]

    rules = (      
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//a[@id="next"]')),follow=True),
        Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[@class="title"]/a')),callback='parse_item'),
    )

    def parse_item(self, response):
        producto = ScrapyItem()
        nombre = response.xpath('//div[@class="title"]/h5').extract_first()
        nombre = nombre.replace("<h5>", "").replace("<span>","").replace("</span>","").replace("</h5>","").replace("\xa0","")
        producto['nombre'] = nombre
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
        self.item_count += 1
        print(self.item_count)
        yield producto
