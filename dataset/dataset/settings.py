# Scrapy settings for dataset project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'dataset'

SPIDER_MODULES = ['dataset.spiders']
NEWSPIDER_MODULE = 'dataset.spiders'

ITEM_PIPELINES = {
    'dataset.pipelines.DatasetPipeline': 100,
}

FEED_URI = 'file'
FEED_FORMAT = 'jsonlines'

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_MAX_DELAY = 2.0

CONCURRENT_REQUESTS_PER_DOMAIN = 10

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'dataset (+http://www.yourdomain.com)'
