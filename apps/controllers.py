# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from apps import app, db
from pytesseract
import Image

@app.route('/', methods=['POST','GET'])
def article_list():

    return render_template('main.html')








"""
pytessearct usage
 > import Image
 > import pytesseract
 > print pytesseract.image_to_string(Image.open('test.png'))
 > print pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra')
'''


