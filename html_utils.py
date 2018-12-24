#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 18:44:36 2018

@author: chenanyi
"""

import requests
from bs4 import BeautifulSoup as bs
import jieba 
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

# Html exception
class HtmlParseError(Exception):
    def __init__(self,value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

class html_parse():
    # Get html text
    def __init__(self,gov_url,top_n):
        self.all_url = self.get_report_urls(gov_url)
        self.count_list, self.top_n_words = self.article_top_n_words(self.all_url,top_n)
#        self.save_report(self.count_list)
        
    def save_report(self,count_list):
        df=pd.DataFrame(data=count_list)
        df.to_csv("reports.csv",encoding="gb2312")
        print('Saved file!')
    
    def plot_word_cloud(self,count_list):
        combined_text = " ".join([word for word in count_list])
        font = 'SimHei.ttf'
        # Initialize wordcloud object
        wc = WordCloud(background_color='white',font_path=font, max_words=50)
        # Generate and plot wordcloud
        plt.imshow(wc.generate(combined_text))
        plt.axis('off')
        plt.show()
        
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
    def get_top_n_words(self,text,n):
        cut_list = jieba.cut(text,cut_all=False)
        cut_list = [word for word in cut_list if len(word)>=2]
        counter = Counter(cut_list)
        return cut_list, counter.most_common(n)
    
    def article_top_n_words(self,all_url,n):
        cut_list, top_n = [],[]
        count = 0
        for url in all_url:
            html = self.get_html(url)
            article = self.parse_report_article(html)
            temp_cut_list, temp_top_n = self.get_top_n_words(article,n)
            cut_list.append(temp_cut_list)
            top_n.append(temp_top_n)
            count+=1
            print('Finish % files' %count)
            if count > 5:
                break
        return cut_list, top_n
       