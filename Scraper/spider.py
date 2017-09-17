import scrapy
import time
from scrapy import selector
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
    name = 'FinanceCrawl'
    def __init__(self):
        self.urls = [
            'https://www.bloomberg.com/markets',
            'https://www.bloomberg.com/technology',
            'https://www.bloomberg.com/pursuits',
            'https://www.bloomberg.com/politics'
        ]
        self.base_url = 'https://www.bloomberg.com'
        self.baseArticle = []
        self.outfile = 'results.txt'
        super(QuotesSpider, self).__init__(self)

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        time.sleep(1)
        links = response.selector.xpath('//a/@href').extract() # Selector uses xpath

        fixedLinks = []
        [fixedLinks.append(link) for link in links if (link.startswith('/news/articles/') and link not in fixedLinks)]

        # Follow links
        for link in fixedLinks:
            print(link)
            yield scrapy.Request(url=self.base_url + link, callback=self.parseArticle)

    def parseArticle(self, response):
        time.sleep(1)
        data = response.selector.xpath('//p/text()').extract()
        content = []
        if len(self.baseArticle) == 0:
            self.baseArticle = data
            content = data
        else:
            [content.append(p) for p in data if p not in self.baseArticle]
        print(response.url + ":  " + str(content))

        with open(self.outfile, 'a') as f:
            f.write(response.url + '\n' + str(content) + '\n\n')


process = CrawlerProcess({'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}) # Overridden anyways

process.crawl(QuotesSpider)
process.start()
