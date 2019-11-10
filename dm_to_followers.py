import os
import sys
import time
import glob
import set_user

from tqdm import tqdm
from instabot import Bot

messageTosend = 100
banDelay = 86400 / messageTosend

bot = Bot(save_logfile=False)
bot.login(username=set_user.username, password=set_user.password)

for follower in tqdm(bot.followers):
	bot.send_message("Judul\n\nini berita ku", follower)
	