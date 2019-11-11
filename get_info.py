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
args = parser.parse_args()

bot = Bot(save_logfile=False)
bot.login(username=args.u, password=args.p)

id_user = bot.get_user_id_from_username(args.u)
following = bot.get_user_following(id_user)
followers = bot.get_user_followers(id_user)

info_user = {"username": args.u, "followers": len(followers), "following": len(following)}

print(info_user)