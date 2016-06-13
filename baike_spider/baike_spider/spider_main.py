# coding:utf8
'''
Created on 2016年6月13日

@author: Quan
'''
from baike_spider import url_manager, html_parser, html_outputer, html_download


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_download.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    
    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)    #把url添加到set集合中
        while self.urls.has_new_url():     #如果有新的url一直循环
            try:
                new_url = self.urls.get_new_url()      #获取新的url
                print 'craw %d : %s' %(count, new_url)
                html_cont = self.downloader.download(new_url)      #下载页面
                new_urls, new_data = self.parser.parse(new_url, html_cont)    #下载页面信息(url,感兴趣的数据)
                self.urls.add_new_urls(new_urls)      #把url添加到set集合中
                self.outputer.collect_data(new_data)      #保存收集到的数据
                
                if count == 100:   #爬取网页的数量
                    break
                
                count = count + 1
            except:
                print 'craw failed'
                
        self.outputer.output_html()   #把数据写如到html中



if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/2181064.htm" #百度百科词条入口
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
