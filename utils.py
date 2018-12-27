#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 11:39:50 2018

@author: chenanyi
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import pandas as pd

def plot_word_cloud(combined_text,max_words):
    font = 'SimHei.ttf'
    # Initialize wordcloud object
    wc = WordCloud(background_color='white',font_path=font, max_words=max_words)
    # Generate and plot wordcloud
    plt.imshow(wc.generate(combined_text))
    plt.axis('off')
    plt.show()
            
def save_report(corpus):
    df=pd.DataFrame(data=corpus)
    df.to_csv("reports.csv",encoding="gb2312")
    print('Saved file!')
        
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        print("Topic #%d:" % topic_idx)
        print(" ".join([feature_names[i] for i in topic.argsort()[:-n_top_words - 1:-1]]))
        print()