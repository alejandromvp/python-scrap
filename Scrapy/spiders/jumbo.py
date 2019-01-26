# -*- coding: utf-8 -*-
import scrapy
from Scrapy.items import ScrapyItem
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
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/7/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/8/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/12/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/13/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/17/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/18/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/19/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/459/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/21/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/22/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/23/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/24/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/25/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/26/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/418/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/425/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/28/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/35/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/42/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/54/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/489/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/61/47/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/61/63/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/61/62/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/87/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/88/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/89/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/90/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/91/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/75/76/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/75/82/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/107/108/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/107/109/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/125/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/126/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/144/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/142/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/143/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/131/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/128/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/129/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/130/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/132/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/133/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/134/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/135/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/136/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/158/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/159/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/161/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/162/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/573/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/184/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/185/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/186/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/187/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/440/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/473/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/540/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/190/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/191/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/192/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/195/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/196/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/204/205/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/204/206/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/204/207/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/231/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/232/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/233/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/234/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/235/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/236/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/224/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/262/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/263/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/264/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/265/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/266/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/267/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/225/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/227/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/228/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/580/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/293/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/294/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/295/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/296/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/460/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/400/401/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/400/402/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/400/403/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/317/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/318/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/319/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/320/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/299/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/300/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/302/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/303/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/336/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/337/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/338/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/178/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/519/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/521/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/355/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/356/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/357/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/358/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/359/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/360/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/361/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/394/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/395/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/396/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/397/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/398/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/399/",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/461/"
        
        ]
        
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

        yield producto