# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 13:02:42 2017

@author: scaravex
"""

from pandas import read_csv 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from RF_model import ModelForest

import warnings
warnings.simplefilter(action = "ignore", category = DeprecationWarning)
import pymongo
import pickle

### Now importing data locally: the following function can import data from Mongo, if we can set in time
def getResultsAsDF_MongoAggregate(self, pipeline, collection=''):
    """
    get data from MongoDB by aggregate    
    """
    if collection=='':
        collection=self.mongo_collection
        #returns results of query in pandas.DataFrame format
    try:
        client = pymongo.MongoClient(self.mongo_host)
        db = client[self.mongo_db]
        res = db[collection].aggregate(pipeline, allowDiskUse=True)
        df = pd.DataFrame(list(res))
        res.close()
        client.close()
    except:
        print("Exception thrown in getResults - Mongo Aggregate!")
        pass
    else:
        return df
        
def getDummies(dfz, col, minCtn = 10):
    '''
    function which create dummy variables 
    for the different categories
    '''    
    df2 = dfz.copy()
    df2['_id'] = 1
    df_aux = df2.groupby(col).aggregate({'_id':'count'}).reset_index() 
    df_aux = df_aux[df_aux._id>=minCtn]
    topColTypes = list(set(df_aux[col].values))
    dfz[col] = dfz.apply(lambda r: r[col] if r[col] in topColTypes else 'OTHER' , axis=1)
    dummies = pd.get_dummies(dfz[col], prefix=col) # +'_')
    
    return dummies, topColTypes

    
filename = 'DemographicInfoDataFinal.csv'
filename_risk_stability= 'Security_RiskAppettite.csv' 

dataframe_riskAppetite = read_csv(filename, encoding="latin1") 
dataframe_risk_stability = read_csv(filename_risk_stability)

Y_riskAppetite = dataframe_risk_stability.values[:, 2] # prepare models 
Y_Stability = dataframe_risk_stability.values[:, 1] # prepare models 


def riskAppetite_data_preparation(dataframe_riskAppetite):
    '''
    working on the profits dataset (1_1)
    Takes the dataframe and rework values
    As output, the useful data used for training/testing
    '''
    dataframe_riskAppetite.drop(['ADR_NR','StreetAddress','City','Latitude',
                                 'Longitude','GivenName','Surname','Company',
                                 'Occupation','Country','ZipCode'], axis=1, inplace=True)
#   array_riskAppetite = dataframe_riskAppetite.values 
#   X_risk = array_riskAppetite[:, 0:4]
    
#   dumState,  state      = getDummies(dataframe_riskAppetite, "State")   --> too long for the Random Forest
    dumGender, gender = getDummies(dataframe_riskAppetite, "Gender")
    dumVehicle_aging, vehicle_aging = getDummies(dataframe_riskAppetite, "Vehicle_aging")
    dumTypeOfLocation, TypeOfLocation = getDummies(dataframe_riskAppetite, "TypeOfLocation")
    dumAgeGroup, ageGroup = getDummies(dataframe_riskAppetite, "AgeGroup")
    dumCrimeRisk, crimeRisk = getDummies(dataframe_riskAppetite, "CrimeRisk")
    BMI = dataframe_riskAppetite['BMI']
    
    Xfull_risk = pd.concat([BMI, dumGender, dumVehicle_aging, dumTypeOfLocation, dumAgeGroup, dumCrimeRisk], axis=1) 
    X_risk     = Xfull_risk.values
    names_risk = Xfull_risk.columns
    
    '''
    Model test --> if it takes to much time the RF model to get Trained

    num_trees    = 100
    max_features = 15
    min_leafs    = 4
    regressor = RandomForestRegressor(min_samples_leaf = min_leafs, n_estimators = num_trees, max_features = max_features)
    regressor.fit(X_risk, Y_risk)
    test_profits = X_risk[3000,]
    regressor.predict(test_profits)
    '''

    return X_risk, Xfull_risk, names_risk
   
Y_risk,    X_risk,    Xfull_risk,    names_risk    = riskAppetite_data_preparation   (dataframe_riskAppetite)
Y_stability, X_stability, Xfull_stability, names_stability = stability_data_preparation(dataframe_stability)

        
Forest_riskAppetite    = ModelForest(X_risk[0:7999,:],    Y_riskAppetite)    # z_transform = True
Forest_stability = ModelForest(X_risk[0:7999,:], Y_Stability) # z_transform = True


###Saving on different files the inputs that will be used in the prediction model
output = open('RForest_riskAppetite2.pkl', 'wb')
pickle.dump(Forest_riskAppetite, output)
output.close()

output = open('RForest_stability.pkl', 'wb')
pickle.dump(Forest_stability, output)
output.close()


# Section if we manage to create new outputs
NewQuery_score = Xfull_risk.loc[1] * 0

output = open('RForest_Query_score.pkl', 'wb')
pickle.dump(NewQuery_score, output)
output.close()
