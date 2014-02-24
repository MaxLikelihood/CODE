from scrapy.item import Item, Field

class DatasetItem(Item):

    url = Field()
    name = Field()
    frequency = Field()
