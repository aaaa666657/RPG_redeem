# -*- coding: utf-8 -*-
import os.path

from flask import Flask,send_file,request
import pymongo


app = Flask(__name__, static_url_path='')


myclient = pymongo.MongoClient('mongodb://localhost:27017/')
dblist = myclient.list_database_names()

@app.route('/')
def root():
    return send_file('index.html')
@app.route('/login', methods=['GET', 'POST']) 
def login():
	if request.method == 'POST': 

		# create new post object

		post = {"username": request.values['username'],}
		# insert into collection

		post_id = collect.insert_one(post3).inserted_id
		print post_id # if ObjectId('...') then successful!
		
		'''
		res = myclient.test.users.find_one({"username" : request.values['username']})       	
		if res:
			if res["redeemed"]:
				return "已兌換過獎品"
			else:
				temp = myclient.test.users.find_one({"username" : request.values['username'], "redeemed" : False})
				temp2 = temp.copy()
				temp["redeemed"] = True
				myclient.test.users.save(temp)
				return "可兌換獎品"
		else:
 			return "未參加活動"
		'''

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
    app.run(host='0.0.0.0') 
