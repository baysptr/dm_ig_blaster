import os
import sys
import time
import glob
import set_user
import argparse
from tqdm import tqdm
from instabot import Bot

messageTosend = 100
banDelay = 86400 / messageTosend

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
args = parser.parse_args()

bot = Bot(save_logfile=False)
bot.login(username=set_user.username, password=set_user.password)

bot.send_message(args.u, args.p)
bot.logout(username=set_user.username, password=set_user.password)