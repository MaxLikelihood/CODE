from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

class DatasetSpider(CrawlSpider):

    name = 'dataset'
    allowed_domains = ['data.gc.ca']
    start_urls = ['http://data.gc.ca/data/en/dataset?page=1']

