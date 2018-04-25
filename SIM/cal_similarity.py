# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:45:00 2018

@author: Herbert
"""
import jieba
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from scipy.linalg import norm

def segment(original_text):
    # 对输入句子进行分词
    # print("word segmentation:")
    seg_list = jieba.cut_for_search(original_text, HMM=False)  # 搜索引擎模式
    text = " ".join(seg_list)
    # print("word segmentation finish")

    return text

def in_pro_sim(s1, s2):
    """
    计算两个句子的内积相似度
    """
    # 得到两个句子的向量
    vectorizer = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = vectorizer.fit_transform(corpus).toarray()
    # 向量点乘
    in_pr_similarity = np.dot(vectors[0], vectors[1])
    return in_pr_similarity

def cosine_sim(s1, s2):
    """
    计算两个句子的TF余弦相似度
    """
    # 得到两个句子的向量
    vectorizer = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = vectorizer.fit_transform(corpus).toarray()
    # 计算句子相似度的余弦值
    return np.dot(vectors[0], vectors[1]) / (norm(vectors[0]) * norm(vectors[1]))

def jaccard_sim(s1, s2):
    """
    计算两个句子的jaccard相似度
    """
    # 得到两个句子的向量
    vectorizer = CountVectorizer(tokenizer=lambda s: s.split())
    corpus = [s1, s2]
    vectors = vectorizer.fit_transform(corpus).toarray()
    word = vectorizer.get_feature_names()#得到词袋模型中的所有词语
    jaccard_similarity = np.dot(vectors[0], vectors[1]) * 1.0 / len(word)
    return jaccard_similarity

#s1 = "我是中国人"
#s2 = "他是美国人"
#text1 = segment(s1)
#text2 = segment(s2)
#
#in_pro_similarity = in_pro_sim(text1, text2)
#
#cos_similarity = cosine_sim(text1, text2)
#
#jaccard_similarity = jaccard_sim(text1, text2)

