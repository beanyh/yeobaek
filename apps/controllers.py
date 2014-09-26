# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for, g
from apps import app, db
from pytesser import *
from PIL import Image
import logging
from database import Database

dataStorage = Database()


@app.route('/', methods=['POST','GET'])
def main():
    return render_template('main.html')

@app.route('/write', methods=['POST', 'GET'])
def write():
    if request.method == 'POST':
        im = Image.open("./apps/static/img/circle.png")
        text = image_to_string(im)
        logging.debug(text)


    storage = {}
    storage['contents'] = request.form['contents']
    storage['from_book'] = request.form['from_book']
    storage['by_author'] = request.form['by_author']
    storage['date'] = request.form['date']
    dataStorage.put(storage)


    return redirect(url_for('main'))
'''
        posting = Post(
                    author=g.user_name,
                    from_book=g.from_book,
                    by_author=g.by_author,
                    like_count = 0
            )
        db.session.add(posting)
        db.session.commit()
'''

    return render_template("write.html")




"""
ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg', 'gif', 'tif']

def allowed_file(filename):
    return '.' in filename.lower() and filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['POST','GET'])
def search():
    return render_template('main2.html')

@app.route('/write', methods=['POST', 'GET'])
def write():
    if request.method == 'POST':
        im = Image.open("./apps/static/img/circle.png")
        text = image_to_string(im)
        logging.debug(text)

        posting = Post(
                    author=g.user_name,
                    from_book=g.from_book,
                    by_author=g.by_author,
                    like_count = 0
            )
        db.session.add(posting)
        db.session.commit()

        flash(u'게시글을 작성하였습니다.','success')
        return redirect(url_for('article_list'))

        url= url_for("shows", key = upload_data.key())
    return render_template("write.html")

@app.route('/photo', methods=['POST', 'GET'])
def p_write():

    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filestream = file.read()
            im = Image.open(filestream)
            text =  pytesseract.image_to_string(im, lang = 'eng')
            print text
            #upload_data = Photo()
            #upload_data.photo = db.Blob(text)
            #upload_data.put()
            posting = Post(
                    author=g.user_name,
                    from_book=g.from_book,
                    by_author=g.by_author,
                    like_count = 0
            )
            db.session.add(posting)
            db.session.commit()

            flash(u'게시글을 작성하였습니다.','success')
            return redirect(url_for('article_list'))

            url= url_for("shows", key = upload_data.key())

        return render_template()


    return render_template("write.html")
"""