#!/usr/bin/env python
# encoding: utf-8
#Author - Prateek Mehta


import tweepy #https://github.com/tweepy/tweepy
import json
import urllib
import requests


#Twitter API credentials
consumer_key = "T5LUpPCVrvX6ogd4BdRQhtRKz"
consumer_secret = "3ptof8Ry1L7gkcIfaeK8egLZEsqAPzIulm9Kp4ixMh7nV4fqnh"
access_key = "1035597034584199170-Hpn1372cGrcKl2zs0VqRFh0FQZvb8G"
access_secret = "3APPZr1IQoG339QWJRdEBd0HpWqNfo8hgMzRp0VacUh60"


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





    