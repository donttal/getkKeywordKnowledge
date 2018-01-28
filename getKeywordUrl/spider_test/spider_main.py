#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spider_test import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()  # Url管理器
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)  # 添加根页面

        while self.urls.has_new_url():
            try:  # 由于有些url已经失效，进行下载会异常，故而进行异常捕获
                new_url = self.urls.get_new_url()
                print("crawing {0}:{1}".format(count, new_url))
                # 调用html下载器，下载new_url对应的html内容
                html_doc = self.downloader.download(new_url)
                # print(html_doc)
                # 调用html解析器， 解析html内容，获取到网页内容中新的url和需要的信息
                new_urls, new_data = self.parser.parse(html_doc)
                # 将新的url存储到url管理器中
                self.urls.add_new_urls(new_urls)
                # 由outputer手机本次爬取，解析得到网页的信息
                self.outputer.collect_data(new_data)

                if count == 50:
                    break

                count += 1
            except:
                print('--craw falled!---')

        print('crae finished!')
        # 爬取完毕，调用outputer显示爬取的结果
        self.outputer.output_html()
        print('写入已经完成')


def read_keyword_url():
    pass


# 编写模块的主入口
#  爬虫开始爬取的根url，为百度百科中关于Python解析的网页链接
if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()  # 实例化一个爬虫对象
    obj_spider.craw(root_url)  # 启动爬取信息

