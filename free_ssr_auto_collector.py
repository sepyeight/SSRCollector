# !/usr/bin/python3
# -*- coding:UTF-8 -*-

import cfscrape
from bs4 import BeautifulSoup


class FreeSSRParse:
    def get_html(self, target):
        scraper = cfscrape.create_scraper()
        response = scraper.get(target)
        if response.status_code == 200:
            return response.text
        else:
            return ''

    def get_ssr(self, html):
        soup = BeautifulSoup(html, 'lxml')
        links = soup.findAll('a')
        ssr_list = []
        for link in links:
            if link.get('href').startswith('ssr://'):
                ssr_list.append(link.get('href'))
        with open('ssr_list.txt', 'r+') as file:
            ssr_already_list = file.read()
            for ssr in ssr_list:
                if ssr not in ssr_already_list:
                    file.write(ssr+'\n')

    def run(self):
        for index in range(1, 4, 1):
            target = 'https://flywind.ml/free-ssr/' + str(index)
            print('curl {}'.format(target))
            html_content = self.get_html(target)
            self.get_ssr(html_content)


if __name__ == "__main__":
    for index in range(1, 4, 1):
        target = 'https://flywind.ml/free-ssr/' + str(index)
        print('curl {}'.format(target))
        html_content = FreeSSRParse().get_html(target)
        FreeSSRParse().get_ssr(html_content)
