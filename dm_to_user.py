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
parser.add_argument("-m", '--message', type=str, help="message")
parser.add_argument("-t", '--target', type=str, help="target")
args = parser.parse_args()

bot = Bot(save_logfile=False)
bot.login(username=args.u, password=args.p)

bot.send_message(args.dm, args.target)
bot.logout(username=args.u, password=args.p)