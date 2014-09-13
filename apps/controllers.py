# -*- coding: utf-8 -*-
from flask import render_template, request, redirect, url_for
from apps import app, db

@app.route('/', methods=['POST','GET'])
def article_list():

    return render_template('main.html')
