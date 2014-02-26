Canadian Open Data Experience (CODE)
====

For [Canadian Open Data Experience][1], [Open Data][2] dataset web scraper via [scrapy][3] in [Python][4].

Dependency
====
[scrapy][3]

scrapy Item Model
====
`url` Dataset URL

`name` Dataset Name

`frequency` Dataset Maintain and Update Frequency

scrapy Spider Task
====
Visit all available datasets, starting from [page 1][5] to [page 9466][6], and scrape `Dataset Title`, `Dataset URL`, and `Dataset Maintain and Update Frequency` into Item attribute `name`, `url`, and `frequency` respectively. 

Store scraped data
====
In scrapy project directory, execute

`scrapy crawl dataset -o dataset_items.json -t json`

will dump the data into `dataset_items.json` JSON file.

View
====
For quick in-console display, run `print.py`. Default and the only existing filter is `frequency`, more can be added as needed.

Sample JSON Output
====
`{"url": "http://data.gc.ca/data/en/dataset/004c6558-af03-5414-aaa4-2d654428ab4f", "frequency": "As Needed", "name": "Ground Control Database, Canada - N72d50mW098d23m"}`

[1]: https://canadianopendataexperience.com/ "Canadian Open Data Experience"
[2]: http://data.gc.ca/eng/showcase "Canada Open Data"
[3]: http://scrapy.org/ "scrapy"
[4]: http://python.org/ "Python"
[5]: http://data.gc.ca/data/en/dataset?page=1 "Dataset Page 1"
[6]: http://data.gc.ca/data/en/dataset?page=9446 "Dataset Page 9446"
