# -*- coding: utf-8 -*-
import os.path

from flask import Flask,send_file,request
import pymongo


app = Flask(__name__, static_url_path='')


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()

DB = myclient.isweek2018.gifts

@app.route('/')
def root():
    return send_file('index.html')
@app.route('/login', methods=['GET', 'POST']) 
def login():
	if request.method == 'POST': 

		# create new post object
		post = {'type':'RPG',"username": request.values['username'],'redeemed':False}
		# insert into collection
		post_id = DB.insert_one(post).inserted_id
		return "成功"
	return "<form method='post' action='/login'><input type='text' name='username' /></br><button type='submit'>Submit</button></form>"
@app.route('/js/<path>')
def send_js(path):
    return send_file('js/'+path)
@app.route('/style/<path>')
def send_css(path):
    return send_file('style/'+path)
@app.route('/style/images/<path>')
def send_css_images(path):
    return send_file('style/images/'+path)
@app.route('/image/<path>')
def send_images(path):
    return send_file('images/'+path)
@app.errorhandler(404)
def page_not_found(error):
    return send_file('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=4321) 
