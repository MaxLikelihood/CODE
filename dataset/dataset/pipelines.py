import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DatasetPipeline(object):

    title_regex = re.compile('(((((\\(?[A-Za-z]{1}[-A-Za-z]+,?\\)?)|[-0-9]+)|-)|\\(?[A-Za-z0-9]+\\)?) *)+')
    frequency_regex = re.compile('([A-Z]{1}[a-z]+ *)+')

    def process_item(self, item, spider):

        if item['name']:
            item['name'] = self.title_regex.search(item['name'][0].encode('ascii', 'ignore')).group()
        else:
            item['name'] = 'Dataset Title Regex Matching Unsuccessful'

        if item['frequency']:
             item['frequency'] = self.frequency_regex.search(item['frequency'][0].encode('ascii','ignore')).group()
        else:
            item['frequency'] = 'Dataset Frequency Attribute Regex Matching Unsuccessful'

        return item
