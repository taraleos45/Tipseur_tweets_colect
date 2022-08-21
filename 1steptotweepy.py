# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:54:04 2022

@author: doria
"""


import tweepy
import json
import requests
import os
from jsonmerge import merge
from jsonmerge import Merger
import pandas as pd
#pd.set_option('display.int_format', lambda x: '%.9f' % x)
 
# API keyws that yous saved earlier
api_key = "pmam2B1nenjFxJoxO0XRpZmJy"
api_secrets = "bNp4rU8DQGgDYJYLUflxn8iuYway5hniCP764jcmOW07Wu0yqd"
access_token = "1286334455175675905-kokAf9uVycr86ffbgRq2CoTWzpvN7C"
access_secret = "XxLw2P0zZXPOtSIEmFxLFNvpxkIiLen6Oa4ZrJ6sYYPbD"
beared = "AAAAAAAAAAAAAAAAAAAAAM7YfgEAAAAA1SMoVVrl8hT9%2Fb0DIcKM689FfWo%3DJMWS3bopqUnTDafE4wtndCNMpMmxx5bVn5Il2Ya24lw3oWPMJL"
 
callback_url = 'oob' #https://cfe.sh/twitter.callback

client = tweepy.Client(beared,api_key,api_secrets,access_token,access_secret,return_type = requests.Response)

auth = tweepy.OAuth1UserHandler(api_key,api_secrets,access_token,access_secret)
api = tweepy.API(auth)
redi = auth.get_authorization_url()
#print(redi)
#print(client)

#user_pin_input = input('value ?')
#print(user_pin_input)
#new_status = api.update_status("Hello frome my python script")
#re = client.get_liked_tweets('1104882393557712896',max_results=5)
#client.retweet('1556267441650540551', user_auth=False)
df = pd.read_excel ('tipseur_twitter_id.xlsx')
id_requete = 0
dernier_id = int(df['dernier_id_requete'][id_requete])

requete = df['str_requette'][id_requete]
#print(df['str_requette'])

#search = client.search_recent_tweets('"zufygzeuygfuerzf" -is:reply -is:retweet lang:fr',max_results=10,tweet_fields=["public_metrics"])
search = client.search_recent_tweets(requete,max_results=10) #since_id=dernier_id
#print(search.json())
search_json = search.json()
if search_json['meta']['result_count'] != 0:
    print('Data found '+ str(search_json['meta']['result_count'])+ " Tweets")
    newest_id = search_json['meta']['newest_id']
    df.at[id_requete,'dernier_id_requete'] = newest_id
    df.to_excel("tipseur_twitter_id.xlsx", sheet_name="new",index=False)

#g = open("test.txt","w",encoding="utf-8")
    ff = open("json_test.txt", "r",encoding="utf-8")
    
    if os.stat("json_test.txt").st_size == 0:
        g = open("json_test.txt","w",encoding="utf-8")
        print('empty file')
        json.dump(search_json,g)
    else:
        print('not empty file')
        before_json = json.load(ff)
        ff.close()
        g = open("json_test.txt","w",encoding="utf-8")
        json_conc = search_json['data']+before_json['data']
        dic = {'data' : json_conc}
        #g.write(str(dic))
        json.dump(dic,g)
    
    g.close()   
else:
    print('No data found')



#◘g.write('tu veux voir ma bite')

