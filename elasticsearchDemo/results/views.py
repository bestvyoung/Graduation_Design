#_*_ coding:utf-8 _*_
from django.shortcuts import render
from elasticsearch import  Elasticsearch
from results.models import lagouType
from datetime import datetime
# Create your views here.
client = Elasticsearch()
def index(request):
    return render(request,"index.html")
def search(request):
    key_words = request.GET['key']
    print(key_words+'__________________________________________________________________________________')
    start_time = datetime.now()
    response = client.search(index="luyin", doc_type="biao", body={
        "query": {
            "multi_match": {
                "query": key_words,
                "fields":["title","description"]
            }
        },
        "size":10,
        "highlight":{
            "pre_tags":['<span class="keyWord">'],
            "post_tags":['</span>'],
            "fields":{
                "title":{},
                "description":{}
            }
        }
    })
    for item in response["hits"]["hits"]:
        print(item["_source"])
    end_time = datetime.now()
    last_time = (end_time-start_time).total_seconds()
    total_nums = response["hits"]["total"]
    hit_list = []
    for hit in response["hits"]["hits"]:  # 循环查询到的结果
        hit_dict = {}  # 设置一个字典来储存循环结果
        if "title" in hit["highlight"]:  # 判断title字段，如果高亮字段有类容
            hit_dict["title"] = "".join(hit["highlight"]["title"])  # 获取高亮里的title
        else:
            hit_dict["title"] = hit["_source"]["title"]  # 否则获取不是高亮里的title

        if "description" in hit["highlight"]:  # 判断description字段，如果高亮字段有类容
            hit_dict["description"] = "".join(hit["highlight"]["description"])[:500]  # 获取高亮里的description
        else:
            hit_dict["description"] = hit["_source"]["description"]  # 否则获取不是高亮里的description

        hit_dict["url"] = hit["_source"]["url"]  # 获取返回url

        hit_list.append(hit_dict)  # 将获取到内容的字典，添加到列表
      # 显示页面和将列表和搜索词返回到html

    return render(request, "result.html",{     # 当前页码
                                           "total_nums": total_nums,  # 数据总条数
                                           "all_hits": hit_list,  # 数据列表
                                           "key_words": key_words,  # 搜索词
                                          "last_time": last_time  # 搜索时间
                                          })