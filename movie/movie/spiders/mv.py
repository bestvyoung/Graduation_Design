# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from movie.items import MovieItem
from movie.items import MovieItemLoader
import movie.items
from datetime import datetime
import time
class MvSpider(CrawlSpider):
    name = 'mv'
    allowed_domains = ['www.80s.tw']
    start_urls = ['https://www.80s.tw/movie/list']

    rules = (
        Rule(LinkExtractor(allow=r'/movie/list/-----p\d+$'), callback= 'parse_item',follow=True),
        Rule(LinkExtractor(allow=r'//www.80s.tw/movie/\d+$'),callback='parse_job',follow=False)
    )

    def parse_item(self, response):
        print(response.url)
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()


    def parse_job(self, response):  # 回调函数，注意：因为CrawlS模板的源码创建了parse回调函数，所以切记我们不能创建parse名称的函数
        atime = time.localtime(time.time())  # 获取系统当前时间
        dqatime = "{0}-{1}-{2} {3}:{4}:{5}".format(
            atime.tm_year,
            atime.tm_mon,
            atime.tm_mday,
            atime.tm_hour,
            atime.tm_min,
            atime.tm_sec
        )  # 将格式化时间日期，单独取出来拼接成一个完整日期
        url = response.url
        item_loader = MovieItemLoader(MovieItem(), response=response)
        item_loader.add_xpath('title','//div[@id="minfo"]/div[@class="info"]/h1/text()')
        item_loader.add_xpath('another_name','//*[@id="minfo"]/div[2]/span[2]/text()')
        item_loader.add_xpath('actors','//*[@id="minfo"]/div[2]/span[3]/a/text()')
        item_loader.add_xpath('category','//*[@id="minfo"]/div[2]/div[1]/span[1]/a/text()')
        item_loader.add_xpath('area','//*[@id="minfo"]/div[2]/div[1]/span[2]/a/text()')
        item_loader.add_xpath('language','//*[@id="minfo"]/div[2]/div[1]/span[3]/a/text()')
        item_loader.add_xpath('director','//*[@id="minfo"]/div[2]/div[1]/span[4]/a/text()')
        item_loader.add_xpath('up_time','//*[@id="minfo"]/div[2]/div[1]/span[5]/text()')
        item_loader.add_xpath('movie_time','//*[@id="minfo"]/div[2]/div[1]/span[6]/text()')
        item_loader.add_xpath('description','//*[@id="movie_content"]/text()[2]')
        item_loader.add_value('url',url)
        item_loader.add_value('riqi',dqatime)
        movie_item = item_loader.load_item()
        yield movie_item

