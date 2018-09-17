#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import urllib
import requests


#Twitter API credentials
consumer_key = 
consumer_secret = 
access_key = 
access_secret = 


def get_tweets_pic(screen_name):
    i=0

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

  
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    users_tweets = api.user_timeline(screen_name = screen_name,count=10)
    while (i<10):
        for pic in users_tweets:
            if "media" in pic.entities.keys():    
                urllib.request.urlretrieve(pic.entities["media"][0]["media_url"],'/media/sf_EC601_Product_Design/twitter_pics/%d.jpg'%(i+1))
                i=i+1
                if i==10:
                    break   
            
get_tweets_pic("@ShawnMendes")





    
