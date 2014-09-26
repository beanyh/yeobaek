"""
models.py

"""

from apps import db

class Flower(db.Model):
    flower_name = db.Column(db.String(255))
    flower_meaning = db.Column(db.String(255))
    flower_color = db.Column(db.String(255))
    flower_img_name = db.Column(db.String(255))

class Letter(db.Model):
    letter_key = db.Column(db.String(255), primary_key=True)
    letter_from = db.Column(db.String(255))
    letter_by = db.Column(db.String(255))
    letter_contents = db.Column(db.String(255))

"""
class User(db.Model):
    email = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    join_date = db.Column(db.DateTime(), default=db.func.now())

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text())
    author = db.Column(db.String(255))
    category = db.Column(db.String(255))
    date_created = db.Column(db.DateTime(), default=db.func.now())
"""