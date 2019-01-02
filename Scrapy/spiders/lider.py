# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem;
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class LiderSpider(CrawlSpider):
	name = 'lider'
	custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'LOG_FILE': 'error_lider.json',
        'LOG_ENABLED': True,
        'LOG_STDOUT': True,
    }
	allowed_domains = ['www.lider.cl']
	item_count=0
	
	start_urls = [
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Vacuno/_/N-1gleruj',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Vacuno/_/N-1gleruj',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Pollo/_/N-8fisy4',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Cerdo/_/N-smtdkg',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Pavo/_/N-k2c2mu',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Cordero/_/N-1iidz0s',
		'https://www.lider.cl/supermercado/category/Congelados-/Pescados-y-Mariscos/_/N-qnjyef',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Frutas-y-verduras/_/N-1rh1dk8',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Fiambres-y-Embutidos/_/N-gqb8d6',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Leches/_/N-1syzw6g',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Yoghurt/_/N-1ywlmf4',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Quesos/_/N-3j7e1l',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Huevos-y-Mantequillas/_/N-squyhq',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Bebidas-Vegetales/_/N-xj3z08',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Cremas/_/N-1ozxmgv',
		'https://www.lider.cl/supermercado/category/Congelados-/Comidas-Congeladas/Comida-Congelada/_/N-qihlyk',
		'https://www.lider.cl/supermercado/category/Congelados-/Helados/_/N-ovueji',
		'https://www.lider.cl/supermercado/category/Congelados/Postres/Postres-Congelados/_/N-124opyy',
		'https://www.lider.cl/supermercado/category/Congelados/Postres/Postres-Refrigerados/_/N-seh8t7',
		'https://www.lider.cl/supermercado/category/Despensa/Pastas-y-Salsas/_/N-pgxorj',
		'https://www.lider.cl/supermercado/category/Despensa/Harinas-y-Polvos/_/N-1w5ocqy',
		'https://www.lider.cl/supermercado/category/Despensa/Arroz-y-Legumbres/_/N-13kg7b2',
		'https://www.lider.cl/supermercado/category/Despensa/Salsas/_/N-1188opy',
		'https://www.lider.cl/supermercado/category/Despensa/Alimentos-Instantáneos/_/N-gm6h78',
		'https://www.lider.cl/supermercado/category/Despensa/Aceites-y-Aderezos/_/N-qskffs',
		'https://www.lider.cl/supermercado/category/Despensa/Cóctel-y-Snack/_/N-1o5ibif',
		'https://www.lider.cl/supermercado/category/Despensa/Conservas/_/N-98vkeb',
		'https://www.lider.cl/supermercado/category/Despensa/Repostería/_/N-1e3xmac',
		'https://www.lider.cl/supermercado/category/Despensa/Alimentos-Especiales/_/N-1i0ni5w',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Alimentacion/_/N-1we5k8g',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Perfumeria/_/N-1yt9ipw',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Pañales/_/N-m0dwac',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Accesorios-de-Higiene/_/N-1jkijoc',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Entretencion/_/N-1pkr8qg',
		'https://www.lider.cl/supermercado/category/Mascotas/Perro/_/N-12dc08k',
		'https://www.lider.cl/supermercado/category/Mascotas/Gato/_/N-14sisva',
		'https://www.lider.cl/supermercado/category/Otras-Mascotas/_/N-1gc6ake',
		'https://www.lider.cl/supermercado/category/Pan-Frutas-y-Verduras/Panadería/_/N-5fhq6y',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Cereales/Cereales/_/N-e00l8z',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Café-Té-y-Hierbas/_/N-wauza0',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Dulces-Mermeladas-y-Manjar/_/N-1j5bt7c',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Galletas-y-Colaciones-Dulces/_/N-pbmgle',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Chocolates-y-Candy/_/N-1juh1iq',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Postres-para-Preparar/_/N-6vmfx7',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Pastelería/_/N-qg627',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Aguas/_/N-1227rw1',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Jugos/_/N-oz9aq9',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Bebidas/_/N-o65v3z',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Cervezas/_/N-1mi8n3m',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Destilados/_/N-7n2dag',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Coctel-y-Licores/_/N-8rxdu7',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Vinos-y-Espumantes/_/N-she0ig',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Detergentes/_/N-f3yzpu',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Baño-y-Cocina/_/N-mfbfi0',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Pisos-y-Muebles/_/N-fotifz',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Papeles/_/N-ncfsxl',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Aerosoles-y-Desinfectantes/_/N-qr95di',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Accesorios-Aseo/_/N-g6eqjj',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Facial-Corporal/_/N-1c23u66',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Capilar/_/N-u3y2c4',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Personal/_/N-1nln3mi',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Bucal/_/N-hux3cg',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Hombre/_/N-1o9q315',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Mujer/_/N-1atuxia',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Adulto-Mayor/_/N-kl3eff',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Belleza/_/N-u9xnwa',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Salud/_/N-7nnagl',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Librería/_/N-1tyynyq',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Ferretería-y-Automóvil/_/N-vzvlz0',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Celebraciones/_/N-19id83g',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Aire-Libre/_/N-1rlyyc8',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Cocina-y-Hogar/_/N-77oobg',
		'https://www.lider.cl/supermercado/category/Especiales/Precios-Especiales/_/N-koawk5',
		'https://www.lider.cl/supermercado/category/Especiales/Marcas-Propias/_/N-tkgbm8'
		]
	rules = (
		Rule(LinkExtractor(allow=(),restrict_xpaths=('//i[@class="fa fa-angle-right"]/../../a')),follow=True),
		Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[contains(@class,"product-details")]/a')),callback='parse_item'),
	)

	def parse_item(self, response):
		producto = ScrapyItem()
		
		titulo = response.xpath('//title/text()').extract_first()
		titulo = titulo.split('|')
		producto['nombre'] = titulo[0].strip()
		producto['sku'] = response.xpath('//p[@itemprop="sku"]/text()').extract_first()
		producto['descripcion'] = response.xpath('//span[@itemprop="name"]/text()').extract_first()

		precio_activo = int(float(response.xpath('//p[@itemprop="lowPrice"]/@content').extract_first()))

		precio_nulo = response.xpath('//p[@itemprop="highPrice"]/@content').extract_first()
		precio_normal = 0

		if precio_nulo is None:
			precio_normal = precio_activo
		else:
			precio_normal =int(precio_nulo)

		producto['precio_normal'] = precio_normal
		producto['precio_oferta'] = precio_activo
		producto['supermercado'] = 1
		self.item_count += 1
		print(self.item_count)
		yield producto
