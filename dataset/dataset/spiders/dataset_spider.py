from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from .. import items
import re

class DatasetSpider(CrawlSpider):

    pages = 9466
    name = 'dataset'
    allowed_domains = ['data.gc.ca']
    start_urls = []

    for i in range(1, pages + 1):
        start_urls.append('http://data.gc.ca/data/en/dataset?page=' + str(i))

    rules = [Rule(SgmlLinkExtractor(allow=['/dataset/[0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12}']),
                  'parse_dataset')]

    def parse_dataset(self, response):
        p = re.compile('(((((\\(?[A-Za-z]{1}[-A-Za-z]+,?\\)?)|[-0-9]+)|-)|\\(?[A-Za-z0-9]+\\)?) *)+')

        sel = Selector(response)
        dataset = items.DatasetItem()
        dataset['url'] = response.url
        dataset['name'] = p.search(sel.xpath("//div[@class='span-6']/article/div[@class='module'][1]/section[@class='module-content indent-large'][1]/h1/text()").extract()[0].encode('ascii', 'ignore')).group()

        p = re.compile('([A-Z]{1}[a-z]+ *)+')
        dataset['frequency'] = p.search(sel.xpath("//div[@class='span-2']/aside[@class='secondary']/div[@class='module-related'][2]/ul[1]/li[@class='margin-bottom-medium']/text()").extract()[0].encode('ascii','ignore')).group()

        return dataset
