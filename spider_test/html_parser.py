#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from bs4 import BeautifulSoup


class HtmlParser(object):

    def parse(self, html_doc):
        if html_doc is None:
            return

        page_url = r'https://baike.baidu.com'
        soup = BeautifulSoup(html_doc, 'html.parser')

        # 获取本网页中新的URL
        new_urls = self._get_new_urls(page_url, soup)
        # 获取本网页中需要爬去得到的信息
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()

        # 要匹配的节点<a target="_blank" href="/item/
        # %E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80">计算机程序设计语言</a>
        pat = re.compile(r'/item/.+')
        links = soup.find_all('a', href=pat)

        for link in links:
            new_url = link['href']  # 获得节点的href属性值 /item/
            # %E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E8%AF%AD%E8%A8%80
            new_full_url = page_url + new_url
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        new_data = {}
        new_data['url'] = page_url

        # 匹配<dd class='lemmaWgt-lemmaTitle-title'><h1>Phthon<h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find("h1")
        new_data['title']=title_node.get_text(strip=True) # 获得title_node的文字消息

        # 匹配<div class='lemma-summary' label-module="lemmaSummary">节点，获得summary
        summary_node = soup.find('div', class_='lemma-summary')
        new_data['summary']=summary_node.get_text()  # 获得summary_node的文字信息

        return new_data
