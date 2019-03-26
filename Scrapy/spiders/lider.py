# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem;
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse

class LiderSpider(CrawlSpider):
	name = 'lider'
	custom_settings = {
        'LOG_LEVEL': 'ERROR',
        'LOG_FILE': 'error_lider.json',
        'LOG_ENABLED': True,
        'LOG_STDOUT': True,
    }
	allowed_domains = ['www.lider.cl']
	categoria = ''

	start_urls = [
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Vacuno/_/N-1gleruj/cat=nada?Nrpp=70',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Pollo/_/N-8fisy4/cat=nada?Nrpp=40',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Cerdo/_/N-smtdkg/cat=nada?Nrpp=20',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Pavo/_/N-k2c2mu/cat=nada?Nrpp=20',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Cordero/_/N-1iidz0s/cat=nada?Nrpp=3',
		'https://www.lider.cl/supermercado/category/Carnes-y-Pescados/Pescados-y-Mariscos/_/N-xij3cz/cat=nada?Nrpp=60',
		'https://www.lider.cl/supermercado/category/Frutas-y-Verduras/Frutas/_/N-2l8cxe/cat=nada?Nrpp=20',
		'https://www.lider.cl/supermercado/category/Frutas-y-Verduras/Verduras/_/N-1ps6iab/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Frutas-y-Verduras/Frutos-Secos/_/N-1h7jpzp/cat=nada?Nrpp=15',
		'https://www.lider.cl/supermercado/category/Frutas-y-Verduras/Disney/_/N-16ohr3b/cat=nada?Nrpp=4',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Fiambres-y-Embutidos/_/N-gqb8d6/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Quesos/_/N-3j7e1l/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Leches/_/N-1syzw6g/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Cremas/_/N-1ozxmgv/cat=nada?Nrpp=7',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Bebidas-Vegetales/_/N-xj3z08/cat=nada?Nrpp=10',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Yoghurt/_/N-1ywlmf4/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Postres-Refrigerados/_/N-19rajm2/cat=nada?Nrpp=40',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Huevos-y-Mantequillas/_/N-squyhq/cat=nada?Nrpp=70',
		'https://www.lider.cl/supermercado/category/Frescos-Lácteos/Comidas-Preparadas/_/N-4an7fd/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Congelados/Verduras-y-Frutas-Congeladas/_/N-19z05nb/cat=nada?Nrpp=70',
		'https://www.lider.cl/supermercado/category/Congelados/Hamburguesas-y-Churrascos/_/N-4k9ene?Nrpp=30',#hamburguesas
		'https://www.lider.cl/supermercado/category/Congelados/Hamburguesas-y-Churrascos/_/N-1908zjv?Nrpp=3',#churrascos y lomitos
		'https://www.lider.cl/supermercado/category/Congelados/Hamburguesas-y-Churrascos/_/N-1u7kk77?Nrpp=10',#apanados
		'https://www.lider.cl/supermercado/category/Congelados/Hamburguesas-y-Churrascos/_/N-9pmy5q?Nrpp=6',#vegetarianos
		'https://www.lider.cl/supermercado/category/Congelados/Comidas-Congeladas/_/N-g52l8f/cat=nada?Nrpp=40',
		'https://www.lider.cl/supermercado/category/Congelados/Helados/_/N-ovueji/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Alimentación-Libre/_/N-1oou206/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Pastas-y-Salsas/_/N-pgxorj/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Harinas-y-Polvos/_/N-1w5ocqy/cat=nada?Nrpp=20',
		'https://www.lider.cl/supermercado/category/Despensa/Arroz-y-Legumbres/_/N-13kg7b2/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Salsas/_/N-1188opy/cat=nada?Nrpp=80',
		'https://www.lider.cl/supermercado/category/Despensa/Aceites-y-Aderezos/_/N-qskffs/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Cóctel-y-Snack/_/N-1o5ibif/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Conservas/_/N-98vkeb/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Repostería/_/N-1e3xmac/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Despensa/Alimentos-Instantáneos/_/N-gm6h78/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Alimentacion/_/N-1we5k8g/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Perfumeria/_/N-1yt9ipw/cat=nada?Nrpp=80',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Pañales/_/N-m0dwac/cat=nada?Nrpp=50',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Accesorios-de-Higiene/_/N-1jkijoc/cat=nada?Nrpp=10',
		'https://www.lider.cl/supermercado/category/Mundo-Bebe/Entretencion/_/N-1pkr8qg/cat=nada?Nrpp=30',
		'https://www.lider.cl/supermercado/category/Mascotas/Perro/_/N-12dc08k/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Mascotas/Gato/_/N-14sisva/cat=nada?Nrpp=80',
		'https://www.lider.cl/supermercado/category/Otras-Mascotas/_/N-1gc6ake/cat=nada?Nrpp=3',
		'https://www.lider.cl/supermercado/category/Pan-Frutas-y-Verduras/Panadería/_/N-5fhq6y/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Cereales/_/N-1le2ate/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Café-Té-y-Hierbas/_/N-wauza0/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Dulces-Mermeladas-y-Manjar/_/N-1j5bt7c/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Galletas-y-Colaciones-Dulces/_/N-pbmgle/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Chocolates-y-Candy/_/N-1juh1iq/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Postres-para-Preparar/_/N-6vmfx7/cat=nada?Nrpp=30',
		'https://www.lider.cl/supermercado/category/Desayunos-y-Panadería/Pastelería/_/N-qg627/cat=nada?Nrpp=60',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Vinos-y-Espumantes/_/N-she0ig/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Cervezas/_/N-1mi8n3m/cat=nada?Nrpp=70',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Destilados/_/N-7n2dag/cat=nada?Nrpp=40',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Coctel-y-Licores/_/N-8rxdu7/cat=nada?Nrpp=40',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Bebidas/_/N-o65v3z/cat=nada?Nrpp=80',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Jugos/_/N-oz9aq9/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Aguas/_/N-1227rw1/cat=nada?Nrpp=20',
		'https://www.lider.cl/supermercado/category/Bebidas-Licores/Hielo/_/N-1pzg9o4/cat=nada?Nrpp=1',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Detergentes/_/N-f3yzpu/cat=nada?Nrpp=80',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Baño-y-Cocina/_/N-mfbfi0/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Pisos-y-Muebles/_/N-fotifz/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Papeles/_/N-ncfsxl/cat=nada?Nrpp=80',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Aerosoles-y-Desinfectantes/_/N-qr95di/cat=nada?Nrpp=90',
		'https://www.lider.cl/supermercado/category/Limpieza-Aseo/Accesorios-Aseo/_/N-g6eqjj/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Facial-Corporal/_/N-1c23u66/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Capilar/_/N-u3y2c4/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Personal/_/N-1nln3mi/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Bucal/_/N-hux3cg/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Hombre/_/N-1o9q315/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Mujer/_/N-1atuxia/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Cuidado-Adulto-Mayor/_/N-kl3eff/cat=nada?Nrpp=10',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Belleza/_/N-u9xnwa/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Perfumería-Salud/Salud/_/N-7nnagl/cat=nada?Nrpp=50',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Librería/_/N-1tyynyq/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Ferretería-y-Automóvil/_/N-vzvlz0/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Celebraciones/_/N-19id83g/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Aire-Libre/_/N-1rlyyc8/cat=nada?Nrpp=10',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Cocina-y-Hogar/_/N-77oobg/cat=nada?Nrpp=100',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Juguetería/_/N-1g5rpc5/cat=nada?Nrpp=70',
		'https://www.lider.cl/supermercado/category/Hogar-y-Bazar/Electrohogar/_/N-1nat8m4/cat=nada?Nrpp=20'
	]

	rules = (
		Rule(LinkExtractor(allow=(),restrict_xpaths=('//i[@class="fa fa-angle-right"]/../../a')),follow=True,process_links='parentURI'),
		Rule(LinkExtractor(allow=(),restrict_xpaths=('//div[contains(@class,"product-details")]/a')),callback='parse_item',process_links='childrenURI'),
	)

	def parentURI(self,value):#sacar nombre categoría en URL padre

		for link in value:
			o = urlparse(link.url)
			self.categoria=''
			self.categoria = o.path.split('/')[7][4:]
			yield link


	def childrenURI(self,value):#concatenar categoría a URL hijo
		for link in value:
			link.url = link.url + '?cat='+self.categoria
			self.aux = 1
			yield link

	def parse_item(self, response):
		producto = ScrapyItem()
		
		titulo = response.xpath('//title/text()').extract_first()
		titulo = titulo.split('|')
		producto['nombre'] = titulo[0].strip()
		producto['sku'] = response.xpath('//span[@itemprop="productID"]/text()').extract_first()
		producto['descripcion'] = response.xpath('//span[@itemprop="name"]/text()').extract_first()

		precio_activo = int(float(response.xpath('//p[@itemprop="lowPrice"]/@content').extract_first()))

		precio_nulo = response.xpath('//p[@itemprop="highPrice"]/@content').extract_first()
		precio_normal = 0

		if precio_nulo is None:
			precio_normal = precio_activo
		else:
			precio_normal = int(float(precio_nulo))

		producto['precio_normal'] = precio_normal
		producto['precio_oferta'] = precio_activo
		producto['supermercado'] = 1
		o = urlparse(response.url)
		producto['categoria']=o.query[4:]
		yield producto
