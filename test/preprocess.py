# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:46:19 2018

@author: Herbert
"""

import jieba  
import re  
  
class Scan(object):  
    def __init__(self,path):  
        self.path = path  
    def scan(self):  
        r = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+'  
        try:  
            f = open(self.path, "r",encoding='UTF-8')  
        except Exception as err:  
            print(err)  
        finally:  
            print("文件读取结束")  
        word_list = []  
        while True:  
            line = f.readline()  
            if line:  
                line = line.strip()  
                line = re.sub(r, '', line)  
                seg_list = jieba.cut(line, cut_all=False)  
                word_list.append(list(seg_list))  
            else:  
                break  
        f.close()  
        print(word_list)  