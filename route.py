# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

def cat():
    return 'Cat Page!'

# app.add_url_rule('/cat',view_func=cat)
app.add_url_rule('/cat','cat',cat)

@app.route('/user/')
@app.route('/user/<username>')
def user_name(username='world'):
	return 'Hello %s'% username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id