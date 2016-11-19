import key #key.py file with keys from twitter
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
	if (response.ok): #if we get a valid response from server
		try:
			#convert response to a json object
			jData = json.loads(response.content.decode('utf-8'))
			quote = (jData['quoteText'])
			if(jData['quoteAuthor'] == ''): #if no author, use Anonymous
				author = "Anonymous"
			else:
				author = jData['quoteAuthor']
			tweet = quote + " -" + author
			if(len(tweet) > 160): #if the tweet is more than 160 characters, we need another quote
				print("Quote too long")
				getQuote()
			api.update_status(tweet)
		except ValueError: #try again if we get a valuerror
			getQuote()
	else:
		response.raise_for_status() #print error from server

	



while True:
	getQuote()
	sleep_time = random.randrange(1800, 3601)
	print("Sleeping for " + str(sleep_time) + " seconds.")
	time.sleep(sleep_time)



