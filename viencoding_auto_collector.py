# !/usr/bin/python3
# -*- coding:UTF-8 -*-

import requests
from bs4 import BeautifulSoup


class ViencodingParse:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7,zh;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }
        self.target = 'https://viencoding.com/ss-ssr-share'
        self.proxies = {'socket5': 'socket5://127.0.0.1:1086', 'http': 'http://127.0.0.1:1087'}

    def get_html(self):
        response = requests.request('GET', self.target, headers=self.headers)
        if response.status_code == 200:
            return response.text
        else:
            return ''

    def get_ssr(self, html, reg):
        soup = BeautifulSoup(html, 'lxml')
        ssr_list = soup.find_all(reg)
        with open('ssr_list.txt', 'r+') as file:
            ssr_already_list = file.read()
            for ssr in ssr_list:
                ssr = ssr.string
                if ssr not in ssr_already_list:
                    file.write(ssr+'\n')

    def run(self):
        html_content = self.get_html()
        self.get_ssr(html_content, 'code')

if __name__ == "__main__":
    html = ViencodingParse().get_html()
    ViencodingParse().get_ssr(html, 'code')
