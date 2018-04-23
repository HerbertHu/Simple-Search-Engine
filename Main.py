# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 17:11:37 2018

@author: Herbert
"""
import os
from werkzeug import secure_filename
from flask import Flask, render_template, request, redirect, url_for,flash
from similarity import inner_product
from TF_IDF import tf_idf
from SJet import SJet_result

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456' 
#UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['txt'])

app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return redirect(url_for('.success'))


@app.route('/SIM', methods =['POST', 'GET'])
def success():
    if request.method == "POST":
        sen_1 = request.form['sen_1']
        sen_2 = request.form['sen_2']
        
        if sen_1 == "" or sen_2 == "":
            
            flash("提示：输入句子不能为空")
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

app.config['SECRET_KEY'] = '123456'   

@app.route('/TFIDF', methods=['GET', 'POST'])
def upload_file():        
    if request.method == 'POST':
        try:
            file = request.files['file']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                BASE_DIR = os.path.dirname(__file__)
                file_dir = os.path.join(BASE_DIR, 'uploadFile/')
                file.save(os.path.join(file_dir, filename))
                tf_idf.cal_tfidf()
                flash("TF-IDF计算已完成")
                render_template('TFIDF.html')
            else:
                flash("提示：文件只能为txt格式")
                render_template('TFIDF.html')
        except:
            flash("提示：文件不能为空")
            render_template('TFIDF.html')

    return render_template('TFIDF.html')

# 展示新闻内容
@app.route('/news_page/<int:id>', methods=['GET'])
def news_page(id):
    BASE_DIR = os.path.dirname(__file__)
    file_dir = os.path.join(BASE_DIR, 'Sjet/CorpusCollection/')
    with open(file_dir + 'output_' + str(id) + '.txt', 'r', encoding='UTF-8') as f:
        title = f.readline()
        content = []
        while True:
            c = f.readline()
            if c:
                content.append(c)
            else:
                break

    return render_template('NEWS.html', title=title, content=content)

@app.route('/SJet', methods=['GET','POST'])
def sjet():
    if request.method == "POST":
        query = request.form['query']
        text_result = SJet_result.text_sort(query)

        BASE_DIR = os.path.dirname(__file__)
        file_dir = os.path.join(BASE_DIR, 'Sjet/CorpusCollection/')
        
        results = []
        for i in range(10):
            with open(file_dir + text_result[i] + '.txt', 'r', encoding='UTF-8') as f:
                id_num = text_result[i][7:]
                title = f.readline()
                content = []
                c = f.readline()
                c = f.readline()
                if c:
                    content.append(c[0:50])
                else:
                    c = f.readline()
                    content.append(c[0:50])
                results.append([id_num, title,content])
        
        return render_template('SJET.html', results = results)
    else:
        return render_template('SJET.html')


if __name__=="__main__":
    app.run(debug=True)
