# -*- coding: utf-8 -*-
import sys
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
sys.path.append(os.path.dirname(__file__))
import word_list

# 得到文件夹下面的文件名
def get_file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.txt':
                L.append(os.path.splitext(file)[0])
    return L


def cal_tfidf():
    current_path = os.path.dirname(__file__) #返回当前文件目录
    text_path = '/CorpusCollection/' #设置要分析的文本路径
    filePath = current_path + text_path

    total_text = []
    wordSeg = word_list.WordSeg() #分词模块

    file_list = get_file_name(filePath)
    for file_name in file_list:
        text_path = '/CorpusCollection/' + file_name + '.txt' #设置要分析的文本路径
        filePath = current_path + text_path
        text = wordSeg.segment(filePath)
        total_text.append(text) #得到分词结果

    vectorizer=CountVectorizer(stop_words = None)#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
    tfidf=transformer.fit_transform(vectorizer.fit_transform(total_text))
    #第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

    weight_pd = pd.DataFrame(weight)
    weight_pd.columns=word

    return weight_pd, word, file_list
