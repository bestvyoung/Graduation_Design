# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst
from scrapy.loader import ItemLoader                #导入ItemLoader类也就加载items容器类填充数据
from .elasticsearch_orm import movieType

class MovieItemLoader(ItemLoader):                  #自定义Loader继承ItemLoader类，在爬虫页面调用这个类填充数据到Item类
    default_output_processor = TakeFirst()



def tianjia(value):                                 #自定义数据预处理函数
    return value

class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field(  # 接收爬虫获取到的title信息
        input_processor=MapCompose(tianjia),  # 将数据预处理函数名称传入MapCompose方法里处理，数据预处理函数的形式参数value会自动接收字段title
    )

    title = scrapy.Field()
    another_name = scrapy.Field()
    actors = scrapy.Field()
    category = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    director = scrapy.Field()
    up_time = scrapy.Field()
    movie_time = scrapy.Field()
    description = scrapy.Field()
    #keywords = scrapy.Field()
    url = scrapy.Field()
    riqi = scrapy.Field()

    def save_to_es(self):
        lagou = movieType()  # 实例化elasticsearch(搜索引擎对象)
        lagou.title = self['title']  # 字段名称=值
        lagou.description = self['description']
        lagou.another_name = self['another_name']
        lagou.actors = self['actors']
        lagou.category = self['category']
        lagou.area = self['area']
        lagou.language = self['language']
        lagou.director = self['director']
        lagou.up_time = self['up_time']
        lagou.movie_time = self['movie_time']
        lagou.description = self['description']
        lagou.url = self['url']
        lagou.riqi = self['riqi']
        lagou.save()  # 将数据写入elasticsearch(搜索引擎对象)
        return