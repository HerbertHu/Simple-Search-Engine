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
        # print("word segmentation:")
        # 读取文件
        original_text = open(filePath, 'r', encoding='UTF-8').read()

        # 得到分词结果
        seg_list = jieba.cut_for_search(original_text, HMM=False)  # 搜索引擎模式
        text = " ".join(seg_list)
        # print("word segmentation finish")
        return text
