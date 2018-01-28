#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import traceback


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return
        headers = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        try:
            r = requests.get(url, headers=headers, timeout=30, allow_redirects=False)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return


# if __name__ == '__main__':
#     a = HtmlDownloader()
#     h = a.download('https://baike.baidu.com/item/Python/407313')
#     print(h)
