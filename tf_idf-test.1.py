import sys
import os
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
sys.path.append(os.path.dirname(__file__)) 
import word_list

total_text = []

current_path = os.path.dirname(__file__)
text_path = '/uploadFile/' + 'output_1.txt' #设置要分析的文本路径
filePath = current_path + text_path

wordSeg = word_list.WordSeg()
text = wordSeg.segment(filePath)
total_text.append(text)

vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
tfidf=transformer.fit_transform(vectorizer.fit_transform(total_text))
#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  

for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    
    f = open(current_path + '/tes_tfidf.txt', 'w', encoding='UTF-8')
    
    for j in range(len(word)):  
        f.write(word[j] + ' ')
        f.write(str(weight[i][j]) + '\n')
    #        f.write('\n')
f.close()


