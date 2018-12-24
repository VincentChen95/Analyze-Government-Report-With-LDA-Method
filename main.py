#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:26:17 2018

@author: chenanyi
"""
from html_utils import html_parse

def main():
    # Report url
    all_reports_url = 'http://www.gov.cn/guowuyuan/baogao.htm'
    x = html_parse(gov_url=all_reports_url,top_n=50)
    x.plot_word_cloud(x.count_list[2])
    
if __name__ == '__main__':
    main()