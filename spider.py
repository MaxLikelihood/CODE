from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class DatasetSpider(CrawlSpider):

    name = 'dataset'
    allowed_domains = ['data.gc.ca/data/en']
    start_urls = ['http://data.gc.ca/data/en/dataset?page=1']
    rules = [Rule(SgmlLinkExtractor(allow=['/dataset/[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}']),
                  'parse_dataset')]
