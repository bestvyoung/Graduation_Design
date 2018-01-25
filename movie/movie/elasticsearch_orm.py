  #!/usr/bin/env python
# -*- coding:utf8 -*-
from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, Completion, Keyword, Text, Integer

# 更多字段类型见第三百六十四节elasticsearch(搜索引擎)的mapping映射管理

from elasticsearch_dsl.connections import connections       # 导入连接elasticsearch(搜索引擎)服务器方法
connections.create_connection(hosts=['127.0.0.1'])


class movieType(DocType):                                                   # 自定义一个类来继承DocType类
    # Text类型需要分词，所以需要知道中文分词器，ik_max_wordwei为中文分词器
    title = Text(analyzer="ik_max_word")      # 设置，字段名称=字段类型，Text为字符串类型并且可以分词建立倒排索引
    another_name = Text(analyzer="ik_max_word")
    actors = Text(analyzer="ik_max_word")
    category = Text(analyzer="ik_max_word")
    area = Text(analyzer="ik_max_word")
    language = Text(analyzer="ik_max_word")
    director = Text(analyzer="ik_max_word")
    up_time = Text(analyzer="ik_max_word")
    movie_time = Text(analyzer="ik_max_word")
    description = Text(analyzer="ik_max_word")
    keywords = Text(analyzer="ik_max_word")
    url = Keyword()                                                         # 设置，字段名称=字段类型，Keyword为普通字符串类型，不分词
    riqi = Date()                                                           # 设置，字段名称=字段类型，Date日期类型

    class Meta:                                                             # Meta是固定写法
        index = "movie"                                                     # 设置索引名称(相当于数据库名称)
        doc_type = 'name'                                                   # 设置表名称

if __name__ == "__main__":          # 判断在本代码文件执行才执行里面的方法，其他页面调用的则不执行里面的方法
    movieType.init()                # 生成elasticsearch(搜索引擎)的索引，表，字段等信息


# 使用方法说明：
# 在要要操作elasticsearch(搜索引擎)的页面，导入此模块
# lagou = lagouType()           #实例化类
# lagou.title = '值'            #要写入字段=值
# lagou.description = '值'
# lagou.keywords = '值'
# lagou.url = '值'
# lagou.riqi = '值'
# lagou.save()                  #将数据写入elasticsearch(搜索引擎)