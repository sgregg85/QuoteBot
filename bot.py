import key
import tweepy
import requests
import json
import time
import random

auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)
api = tweepy.API(auth)


def getQuote():
	url = 'http://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=json'#p&jsonp=?'
	response = requests.get(url)
	if (response.ok):
		try:
			jData = json.loads(response.content)
			quote = (jData['quoteText']).decode("unicode_escape")
			if(jData['quoteAuthor'] == ''):
				author = "Anonymous"
			else:
				author = jData['quoteAuthor']
			tweet = quote + " -" + author
			if(len(tweet) > 160):
				print("Quote too long")
				getQuote()
			api.update_status(tweet)
		except ValueError:
			getQuote()
	else:
		response.raise_for_status()

	



while True:
	getQuote()
	sleep_time = random.randrange(1800, 3601)
	print("Sleeping for " + str(sleep_time) + " seconds.")
	time.sleep(sleep_time)



