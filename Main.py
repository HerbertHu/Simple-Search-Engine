# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:11:37 2018

@author: Herbert
"""

from flask import Flask, render_template, request, redirect, url_for,flash
from similarity import inner_product

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('.success'))


@app.route('/TFIDF', methods =['POST', 'GET'])
def success():
    if request.method == "POST":
        sen_1 = request.form['sen_1']
        sen_2 = request.form['sen_2']
        
        if sen_1 == "" or sen_2 == "":
            in_pro_similarity = "请输入两个句子"
            cos_similarity = "请输入两个句子"
            jaccard_similarity = "请输入两个句子"
        else:    
            text1 = inner_product.segment(sen_1)
            text2 = inner_product.segment(sen_2)
            
            in_pro_similarity = inner_product.in_pro_sim(text1, text2)
            cos_similarity = inner_product.cosine_sim(text1, text2)           
            jaccard_similarity = inner_product.jaccard_sim(text1, text2)
        
        return render_template('SIM.html', result_1 = in_pro_similarity,result_2 = \
                           cos_similarity, result_3 = jaccard_similarity)
    else:
        return render_template('SIM.html')


if __name__=="__main__":
    app.run()