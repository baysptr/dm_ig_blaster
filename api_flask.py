import os
import sys
import time
from flask import Flask
from flask import request
from flask import json
from tqdm import tqdm
from instabot import Bot

messageTosend = 100
banDelay = 86400 / messageTosend

project_root = os.path.dirname(__name__)
template_path = os.path.join(project_root)

app = Flask(__name__,template_folder=template_path)
bot = Bot(save_logfile=False)
tasks_list = []

@app.route('/dm_to_user', methods=['post'])
def dm_to_user():
	_username = request.form['username']
	_password = request.form['password']
	_userTarget = request.form['user_target']
	_dm = request.form['dm']
	
	# os.system('python3 dm_to_followers.py')
	os.system('python3 dm_to_user.py dm '+repr(_dm)+' target '+_userTarget+' -u '+_username+' -p '+_password)

	# tasks_list.append((bot.login(username=_username, password=_password), {'username': _username}))
	# tasks_list.append((bot.send_message(_dm, _userTarget), {'dm': _dm, 'target': _userTarget}))

	return 'success'


if __name__ == '__main__':
	app.run(debug=False)