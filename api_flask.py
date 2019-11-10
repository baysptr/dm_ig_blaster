import os
import sys
import time
from flask import Flask
from flask import request
from flask import json

messageTosend = 100
banDelay = 86400 / messageTosend

project_root = os.path.dirname(__name__)
template_path = os.path.join(project_root)

app = Flask(__name__,template_folder=template_path)

@app.route('/dm_to_user', methods=['post'])
def dm_to_user():
	_username = request.form['username']
	_password = request.form['password']
	_userTarget = request.form['user_target']
	_dm = request.form['dm']
	
	os.system('python3 dm_to_user.py -d '+repr(_dm)+' -t '+_userTarget+' -u '+_username+' -p '+_password)

	return 'success'

@app.route('/follow_by_hashtag', methods=['post'])
def follow_by_hashtag():
	_username = request.form['username']
	_password = request.form['password']
	_hashtag = request.form['hashtag']

	os.system('python3 bot_follow_where_hashtag.py -u '+_username+' -p '+_password+' hashtags '+_hashtag)
	return 'success'
	
@app.route('/dm_by_following', methods=['post'])
def dm_by_following():
	_username = request.form['username']
	_password = request.form['password']
	_message = request.form['message']

	os.system('python3 dm_to_following.py -u '+_username+' -p '+_password+' -d '+repr(_message))

	return 'success'

@app.route('/dm_by_followers', methods=['post'])
def dm_by_followers():
	_username = request.form['username']
	_password = request.form['password']
	_message = request.form['message']

	os.system('python3 dm_to_followers.py -u '+_username+' -p '+_password+' -d '+repr(_message))

	return 'success'

if __name__ == '__main__':
	app.run(debug=False)