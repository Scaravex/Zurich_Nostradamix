# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:19:12 2017

@author: scaravex
"""

'''

@IBM Watson™ Personality

The IBM Watson™ Personality Insights service enables applications to @derive insights
from social media, enterprise data, or other digital communications. 
The service uses linguistic analytics to infer individuals' intrinsic personality 
characteristics, including Big Five, Needs, and Values, from digital communications 
such as email, text messages, tweets, and forum posts.

'''
# https://github.com/watson-developer-cloud/python-sdk
# pip install --upgrade watson-developer-cloud
from os.path import dirname
import json

personality_insights = PersonalityInsightsV3(
  version='2016-10-20',
  username='{username}',
  password='{password}'
)

profile(text, content_type='text/plain', content_language=en ,
  accept='application/json', accept_language=None, raw_scores=False,
  consumption_preferences=False, csv_headers=False)




with open(join(dirname(__file__), './profile.json')) as profile_json:
  profile = personality_insights.profile(
    profile_json.read(), content_type='application/json',
    raw_scores=True, consumption_preferences=True)

print(json.dumps(profile, indent=2))


