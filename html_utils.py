#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:44:36 2018

@author: chenanyi
"""

import requests
from bs4 import BeautifulSoup as bs
import jieba 

# Html exception
class HtmlParseError(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class html_parse():
    # Get html text
    def __init__(self,gov_url):
        self.all_url = self.get_report_urls(gov_url)
        self.corpus= self.get_corpus(self.all_url)
        assert len(self.corpus) == 50, 'There are 50 years reports'
        
    def get_report_urls(self, gov_url):
        html = self.get_html(gov_url)
        soup = bs(html,'html.parser')
        tag = soup.find_all('a',href=True)
        result = []
        for a in tag:
            # We need to remove the /r and /n
            result.append(a['href'].strip())
        all_reports_url = [url for url in result if url[:4] == 'http']
        return  all_reports_url       
    
    def get_html(self,url):
        header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98'}
        resp = requests.get(url,headers = header)
        resp.encoding = 'utf-8'
        if resp:
            return resp.text
        return None

    def parse_report_article(self,html):
        soup = bs(html,'html.parser')
        # Solution 1
        article = soup.select('#UCAP-CONTENT')
        # If article is None
        if len(article) == 0:
            article = soup.select('.p1')
            # It still None
            if len(article) == 0:
                raise HtmlParseError('parse report error!')    
        return article[0].text
    
    # Counter the most frequence of word
    def cut_txt(self,text):
        cut_list = ' '.join(jieba.cut(text,cut_all=False))
        return cut_list
    
    def get_corpus(self,all_url):
        corpus = []
        count = 0
        for url in all_url:
            html = self.get_html(url)
            article = self.parse_report_article(html)
            temp_cut_list = self.cut_txt(article)
            corpus.append(temp_cut_list)
            count+=1
            if count % 10 ==0:
                print('Finish %d files' %count)
        return corpus
       