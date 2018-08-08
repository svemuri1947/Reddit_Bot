#/Users/vemuri/anaconda/bin/python

import praw
import config


def bot_login():

	print ("Logging in...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id, 
			client_secret = config.client_secret,
			user_agent = "XYZ" )

	print ("Logged in")


	return r

def run_bot(r):

	print("Obtaining 10 comments")
	for comment in r.subreddit('programming').comments(limit=10):
		if "beginner" in comment.body:
			comment.reply("Welcome to the club")
