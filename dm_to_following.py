import os
import sys
import time
import argparse

from tqdm import tqdm
from instabot import Bot

messageTosend = 100
banDelay = 86400 / messageTosend

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-d", type=str, help="direct message")
args = parser.parse_args()

bot = Bot(save_logfile=False)
bot.login(username=args.u, password=args.p)

for following in tqdm(bot.following):
	bot.send_message(args.d, following)

bot.logout(username=args.u, password=args.p)	