from scrapy.item import Item, Field

class DatasetItem(Item):

    name = Field()
    frequency = Field()
    