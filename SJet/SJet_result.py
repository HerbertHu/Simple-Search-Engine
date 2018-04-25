# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.dirname(__file__))
import corpusTfIdf
import jieba
import pandas as pd
import numpy as np

def text_sort(query):
#    query = "一届中国第一所现代化大学中的现代化大学"
    weight_pd, word_set, file_list = corpusTfIdf.cal_tfidf()

    # 计算query每个词的tfidf
    seg_list = jieba.cut_for_search(query, HMM=False)
    words_in_query = list(seg_list)

    # 对query中每个词，计算在query中出现的次数
    tfidf_in_query = {}
    for word in words_in_query:
        word = word.strip()
        if len(word) > 0:
            tfidf_in_query[word] = tfidf_in_query.get(word, 0.0) + 1.0

    query_vector = []
    # 分析语料库是否有出现了query中的这个词，得到这个词的tfidf
    for key in tfidf_in_query:
        if(key in word_set):
            tfidf_in_query[key] = tfidf_in_query[key] / len(words_in_query)
            query_vector.append(tfidf_in_query[key])
        else:
            tfidf_in_query[key] = 0
            query_vector.append(tfidf_in_query[key])
    query_vector=np.array(query_vector)

# 得到query里面的词在语料集合里面的TFIDF值
    corpus_vector = pd.DataFrame(np.zeros([len(weight_pd),1]))
    for key in tfidf_in_query:
        print(key)
        if(key in word_set):
            temp_vector = weight_pd[key]
        else:
            temp_vector = pd.DataFrame(np.zeros([len(weight_pd),1]))
            temp_vector.columns= [key]
        corpus_vector = pd.concat([corpus_vector, temp_vector], axis = 1)
    corpus_vector = corpus_vector.drop(0, axis=1)
    corpus_vector = np.array(corpus_vector)#得到query相对应的向量

# 计算query每个词的词频，转化为向量
    result = np.zeros([len(weight_pd),1])
    for i in range(len(corpus_vector)):
        corpus_norm = np.sum(np.square(corpus_vector[i])) #向量模长
        # 判断向量是否为零向量
        if(abs(corpus_norm-0.0) > 0.0000001):
            # 向量点乘得到相似度
            result[i] = query_vector.dot(corpus_vector[i])
        else:
            result[i] = 0
    # 根据相似度排序，得到相应的文本编号
    index_number = np.argsort(-result, axis=0)

    # 得到和query相似的文本列表
    fileInOrder = []
    for index in range(len(index_number)):
        fileInOrder.append(file_list[index_number[index][0]])

    return fileInOrder
