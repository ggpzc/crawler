import scrapy
from bs4 import BeautifulSoup
import tools


class baiduSpider(scrapy.spiders.Spider):
    name = "baidu"                              # name for crawler
    allowed_domains = ["baidu.com"]             # crawl domain


    start_urls = [
        "https://www.baidu.com"                 # the page to begin with
    ]




    def parse(self, response):
        R=BeautifulSoup(response.text,'lxml')

        input=R.find('input')
        input.string=tools.keyword()