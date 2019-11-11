"""
    instabot example

    Send photo to user
"""

import argparse
import os
import sys

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-t", type=str, help="target user")
parser.add_argument("-d", type=str, help="direct message")
args = parser.parse_args()

bot = Bot(save_logfile=False)
bot.login(username=args.u, password=args.p)

users = args.t
users = users.split(',')


bot.send_messages(args.d, users)
bot.logout(username=args.u, password=args.p)
