import tweepy
from twitter_keys import consumer_key, consumer_secret, access_key, access_secret
import logging

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

def send_tweet(copy, in_reply_to=None):
	return api.update_status(copy, in_reply_to_status_id=in_reply_to)

def construct(movie):
	tweets = []
	last_index = 0
	new_tweet = True
	header = movie['page_title']+":"

	text = ""
	
	for idx, i in enumerate(movie['link_titles'][last_index:]):
		if new_tweet == True:
			text += header
			new_tweet = False
		
		item = "\n- " + i
		
		if len(text) + len(item) <= 274:
			text += item
			if idx == len(movie['link_titles']) - 1:
				tweets.append(text)
		
		else:
			tweets.append(text)
			new_tweet = True
			text = ""
			last_index = idx

	if len(tweets) > 1:
		for idx, i in enumerate(tweets):
			numbered = "%s\n(%i/%i)" % (i, idx+1, len(tweets))
			tweets[idx] = numbered


	return tweets