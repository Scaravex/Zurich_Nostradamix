# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:45:49 2017

@author: mskara
"""
import pickle
import numpy as np
import pandas as pd

'''
File for Data processing and testing
This section takes a new query, preprocess it and run
the two models to provides estimates for risk appetite score and stability score
'''
forest_riskAppetite = pickle.load(open("RForest_riskAppetite.pkl", "rb"))
forest_stability = pickle.load(open("RForest_stability.pkl", "rb"))
newQuery_scoring = pickle.load(open("RForest_Query_score.pkl", "rb"))

#example of options
new_query = {}

new_query['Gender']  = 'female'           #options: male, female --> need same wording
new_query['AgeGroup'] = '18-24'         #options:18-24, 25-34, 35-44, 45-54, >55 
new_query['TypeOfLocation'] = 'Big city'#options: Big city, Medium city, Village or rural
new_query['City_type'] = 'big'          #options: big, small_medium, rural
new_query['CrimeRisk'] = 'Low'          #options: Low, Medium, Unknown
new_query['BMI'] = 20                   #range: 10 - 40


def process_NewQuery(newQuery_scoring, forest_riskAppetite, forest_stability, new_query):
    '''
    1) take data from Mongo of a user of the Chatbot
    2) Rransform data in a format usable by the Random Forest
    3) Generate estimates and return them
    '''
    #for now is set as fixed (only male considered) due to the fact there is no question about sex
    newQuery_scoring['Gender_%s'% str(new_query["Gender"])] = 1

    newQuery_scoring['AgeGroup_%s' % str(new_query["AgeGroup"])] = 1

    newQuery_scoring['TypeOfLocation_%s' % str(new_query["TypeOfLocation"])] = 1

    newQuery_scoring['City_type%s' % str(new_query["City_type"])] = 1

    newQuery_scoring['CrimeRisk%s' % str(new_query["CrimeRisk"])] = 1

    estimated_riskAppetiteScore = forest_riskAppetite.predict(newQuery_scoring)["estimate"]
    estimated_stabilityScore = forest_riskAppetite.predict(newQuery_scoring)["estimate"]

    return estimated_riskAppetiteScore, estimated_stabilityScore


estimated_riskAppetiteScore, estimated_stabilityScore = process_NewQuery(
                                                                         newQuery_scoring    = newQuery_scoring,
                                                                         forest_riskAppetite = forest_riskAppetite,
                                                                         forest_stability    = forest_stability,
                                                                         new_query           = new_query
                                                                         )

print(estimated_riskAppetiteScore)
print(estimated_stabilityScore)
