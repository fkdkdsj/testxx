# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from pyquery import PyQuery

class XxSpider(scrapy.Spider):
    # name = "xx"
    # allowed_domains = ["kingname.info"]
    # start_urls = ['http://exercise.kingname.info/ajax_1_postbackend']
    # data = {'name': 'xx', 'age': 24}
    
    # import json
    # data = json.dumps(data)
    # ua = {
    #     'Content-Type': 'application/json; charset=UTF-8', #重点在这条信息
    #     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    # }

    # def start_requests(self):
    #     print('请求中……')
    #     yield scrapy.http.Request('http://exercise.kingname.info/ajax_1_postbackend', method='POST', headers=self.ua, body=self.data)

    # def parse(self, response):
    #     print(response.body.decode())
    # name = 'xx'
    # allowed_domains = ['yunpanjingling.com']
    # start_urls = ['https://www.yunpanjingling.com/user/login']
    # # handle_httpstatus_list = [403, 400]

    # def start_requests(self):
        
    #     headers = {
    #         # 'Accept':'application/json, text/javascript, */*; q=0.01',
    #         # 'Accept-Encoding':'gzip, deflate, br',
    #         # 'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    #         # 'Connection':'keep-alive',
    #         # 'Content-Length':'55',
    #         # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #         # 'DNT':'1',
    #         # 'Host':'www.yunpanjingling.com',
    #         # 'Origin':'https://www.yunpanjingling.com',
    #         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    #         # 'X-CSRF-TOKEN':csrf,
    #         # 'refer': 'https://www.yunpanjingling.com/',
    #         # 'X-Requested-With':'XMLHttpRequest'
    #     }
                
    #     yield scrapy.Request(self.start_urls[0], headers=headers, meta={'cookiejar': 1}, callback=self.parse, dont_filter=False)

    # def parse(self, response):
    #     data = {'email':'fkdkdsj@gmail.com','password':'ldmoko','remember':'true'}
    #     import json
    #     data = json.dumps(data)
    #     # print(data)
    #     import re
    #     csrf = re.findall('name="csrf-token" content="(.*?)" />', response.body.decode())[0]
    #     print(csrf)
    #     headers = {
    #         'Accept':'application/json, text/javascript, */*; q=0.01',
    #         'Accept-Encoding':'gzip, deflate, br',
    #         'Accept-Language':'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    #         'Connection':'keep-alive',
    #         'Content-Length':'55',
    #         'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    #         'DNT':'1',
    #         'Host':'www.yunpanjingling.com',
    #         'Origin':'https://www.yunpanjingling.com',
    #         'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
    #         'X-CSRF-TOKEN':csrf,
    #         # 'refer': 'https://www.yunpanjingling.com/',
    #         'X-Requested-With':'XMLHttpRequest'
    #     }
    #     yield scrapy.http.Request(self.start_urls[0], method='POST', meta={'cookiejar':1}, headers=headers, body=data, callback=self.after_login)
    #     # return scrapy.FormRequest(url=self.start_urls[0], headers=headers, formdata=data, meta={'cookiejar':1}, callback=self.after_login, dont_filter=False)

    # def after_login(self, response):
    #     print(response.body.decode())


 


    name = 'xx'
    allowed_domains = ["163.com"]
    start_urls = ['http://money.163.com']

    def parse(self, response):
        from testxx.items import TestxxItem
        item = TestxxItem()
        print(item.fields)
        for i in response.xpath('//*[@id="index2016_wrap"]/div/div[3]/div[3]/div[2]/div[1]/ul[1]/li/h3'):
            
            item['url'] = i.xpath('a/@href').extract()[0]
            item['name'] = i.xpath('a/text()').extract()[0]
            #item['rooturl'] = response.url
            #print(item)
            yield item


    # def parse(self, response):
    #     from testxx.items import TestxxItem
    #     from scrapy.loader import ItemLoader

    #     # 通过item loader加载item       
    #     all = response.xpath('//*[@id="index2016_wrap"]/div/div[3]/div[3]/div[2]/div[1]/ul[1]/li/h3')
         
    #     for i in all:    
    #         loader = ItemLoader(item=TestxxItem(), response=response)

    #         loader.add_xpath('url', 'a/@href')
    #         loader.add_xpath('name', 'a/text()')
    #         loader.add_value('rooturl', response.url)

    #         # item = item_loader.load_item()
    #         print(loader.load_item())
