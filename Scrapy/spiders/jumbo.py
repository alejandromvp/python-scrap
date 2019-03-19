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
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/3/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/5/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/7/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/8/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/12/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/13/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/17/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/18/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/19/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/1/459/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/21/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/22/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/23/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/24/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/25/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/26/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/418/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/20/425/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/28/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/35/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/42/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/54/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/27/489/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/61/47/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/61/63/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/61/62/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/87/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/88/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/89/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/90/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/86/91/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/75/76/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/75/82/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/107/108/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/107/109/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/125/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/126/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/144/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/142/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/143/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/124/131/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/128/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/129/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/130/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/132/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/133/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/134/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/135/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/127/136/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/158/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/159/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/161/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/162/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/157/573/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/184/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/185/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/186/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/187/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/440/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/473/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/183/540/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/190/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/191/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/192/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/195/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/189/196/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/204/205/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/204/206/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/204/207/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/231/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/232/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/233/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/234/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/235/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/236/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/230/224/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/262/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/263/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/264/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/265/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/266/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/261/267/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/225/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/227/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/228/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/222/580/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/293/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/294/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/295/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/296/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/292/460/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/400/401/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/400/402/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/400/403/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/317/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/318/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/319/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/316/320/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/299/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/300/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/302/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/298/303/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/336/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/337/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/338/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/178/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/335/521/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/355/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/356/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/357/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/358/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/359/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/360/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/354/361/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/394/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/395/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/396/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/397/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/398/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/399/&cat=nada",
        "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0&PageNumber=1&fq=C:/393/461/&cat=nada"
        
        ]
    base_url = "https://nuevo.jumbo.cl/buscapagina?sl=3a356ef2-a2d4-4f1b-865f-c79b6fcf0f2a&PS=50&cc=18&sm=0"

    def parse(self, response):
        o = urlparse(response.url)
        query = o.query.split('&')
        fq = query[5][3:]
        pageNumber = int(query[4][11:])+1
        cat = query[6][4:]

        nextURL = self.base_url+"&PageNumber="+str(pageNumber)+"&fq="+fq+"&cat="+cat
        if response.body:
            for href in response.xpath('//div[@class="product-item__info"]'):
                url = href.css('a::attr(href)').extract_first()
                request = scrapy.Request(url= url+"?cat="+cat, callback=self.parse_item)
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
        o = urlparse(response.url)
        producto['categoria']=o.query[4:]
        yield producto