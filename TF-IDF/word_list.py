# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:11:15 2018

@author: Herbert
"""
import jieba

class WordSeg():
    """word segmentation algorithm"""
    def __init__(self):
        super(WordSeg, self).__init__()
        
    def segment(self, filePath):
        print("word segmentation:")
        original_text = open(filePath, 'r', encoding='UTF-8').read()
        
        seg_list = jieba.cut_for_search(original_text, HMM=False)  # 搜索引擎模式
        text = " ".join(seg_list)
        
        print("word segmentation finish")
        return text

#seg_list = jieba.cut(text, cut_all=False)
#print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
#
#for key in analyse.extract_tags(text,topK=20, withWeight=True):
## 使用jieba.analyse.extract_tags()参数提取关键字,默认参数为50
## 当withWeight=True时,将会返回number类型的一个权重值(TF-IDF)
#    print(key)