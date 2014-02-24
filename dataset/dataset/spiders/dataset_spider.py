from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from dataset import DatasetItem

class DatasetSpider(CrawlSpider):

    name = 'dataset'
    allowed_domains = ['data.gc.ca/data/en']
    start_urls = ['http://data.gc.ca/data/en/dataset?page=1']
    rules = [Rule(SgmlLinkExtractor(allow=['/dataset/[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}']),
                  'parse_dataset')]

    def parse_dataset(self, response):
        sel = Selector(response)
        dataset = DatasetItem()
        dataset['url'] = response.url
        dataset['name'] = sel.xpath("//div[@class='span-6']/article/div[@class='module'][1]/section[@class='module-content indent-large'][1]/h1").extract()
        dataset['frequency'] = sel.xpath("//div[@class='span-2']/aside[@class='secondary']/div[@class='module-related'][2]/ul[1]/li[@class='margin-bottom-medium']").extract()

        return dataset
