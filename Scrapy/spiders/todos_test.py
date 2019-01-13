from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

process = CrawlerProcess(get_project_settings())

process.crawl('jumbo')
process.crawl('tottus')
process.crawl('lider')
process.start(stop_after_crawl=True)