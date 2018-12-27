#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:26:17 2018

@author: chenanyi
"""
from html_utils import html_parse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from utils import plot_word_cloud,print_top_words
def main():
    # Report url
    all_reports_url = 'http://www.gov.cn/guowuyuan/baogao.htm'
    x = html_parse(gov_url=all_reports_url)
#    plot_word_cloud(x.corpus[2],max_words = 30)
    
    # LDA
    n_features = 1000
    # Delete stop word
    stop_word_txt ="中文停用词表.txt"
    with open(stop_word_txt, 'rb') as fp:
        stopword = fp.read().decode('utf-8')  
    stopword_list = stopword.splitlines() 
    
    tf_vectorizer = CountVectorizer(stop_words= stopword_list,max_features=n_features)
    tf = tf_vectorizer.fit_transform(x.corpus)
    n_topics = 5
    lda = LatentDirichletAllocation(n_components=n_topics, max_iter=500,learning_method='batch')
    lda.fit(tf) 
    
    # Get feature name
    tf_feature_names = tf_vectorizer.get_feature_names()
    print_top_words(lda, tf_feature_names, n_top_words= 20)

if __name__ == '__main__':
    main()