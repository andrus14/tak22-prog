import praw
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from yl27_config import config

reddit = praw.Reddit(
    client_id = config['client_id'],
    client_secret = config['client_secret'],
    user_agent = config['user_agent'],
)

print(reddit.read_only)

for submission in reddit.subreddit("eesti").hot(limit=10):
    print(submission.title)