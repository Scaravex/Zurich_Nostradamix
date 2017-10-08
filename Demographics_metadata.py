# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 03:02:42 2017

@author: scaravex
"""
# sudo easy_install /pip install googlemaps
# import os
# os.chdir(r'C:\Users\mskara\Desktop\zurich-hackhathon\Dati x hackhaton')

import pandas as pd
import numpy as np
from gmaps.geocoding import Geocoding

# api_key = "AIzaSyB8GqObMTav1LziX6Xuer7JuKdGaXWSyzA"
api_key = "AIzaSyBPqby3uCm0JwSCMESS_bgpLYmwQbwGX4Y"

api = Geocoding(api_key)

city_list = pd.read_csv('Mid_BigCities_Germany_enriched.csv', encoding="UTF-8")
# city_list: list of all the city with mroe than 100'000 users.
# To add:
# TypeOfLocation
#   big city 1 --> "Big city"
#   big city 0 --> "Medium city"
#   otherwise  --> "Village or rural"
# CrimeRiskIndex
db_people = pd.read_csv('DemographicInfoData.csv', encoding='latin-1', sep =';')

def gmaps_geometry_creator(city_list, api):
    '''
    function which takes a list of cities and search over google maps,
    it returns the city boundaries
    '''
    city_gmaps = []
    # for every city, fill a database of geometry bounds taken from google maps
    for i in range(79, len(city_list)):
        print(city_list.loc[i][0], " - ", str(i))
        city = {}
        city['id'] = i
        city['name'] = city_list.loc[i][0]
        sequence = [city_list.loc[i][0], ', Germany']
        output_search = ''.join(sequence)
        temp = api.geocode(output_search)
        city['bounds'] = temp[0]['geometry']['bounds']

        temp[0]['geometry']['bounds']
        city['TypeOfLocation'] = city_list.loc[i][3]
        city['CrimeRiskIndex'] = city_list.loc[i][4]
        city_gmaps.append(city)

        return city_gmaps


# for every city search for values which are of the city
def db_people_gmaps_enricher(db_people, city_gmaps):
    '''
    functions that takes the geo-location information of big cities and calculates
    if a person is in a big city, medium city or rural area
    '''
    length = len(db_people)

    db_people_new = db_people.copy()
    db_people_new['TypeOfLocation'] = None
    db_people_new['CrimeRiskIndex'] = None
    
    big = 0
    for j in range(length):
        Latitude = db_people.loc[j]['Latitude']
        Longitude = db_people.loc[j]['Longitude']
        fired=0
        temp_loc = "Village or rural"
        # for every data, it is checked whether the city is inside the value
        for i in range(len(city_gmaps)):
            temp_city = city_gmaps[i]
            northeast = temp_city['bounds']['northeast']
            southwest = temp_city['bounds']['southwest']
            # it should be in the rectangular, around the city ( a better algorithm
            # would identify exactly by scraping gmaps API, without 1000 query limit)
            if (southwest['lat'] <= Latitude <= northeast['lat']):
                if (southwest['lng'] <= Longitude <= northeast['lng']):
                    fired = 1
                    big = 0
                    print('Colpito e affondato',str(j))
                    if (temp_city['TypeOfLocation']==1):
                        temp_loc = "Big city"
                        temp_crime = temp_city['CrimeRiskIndex']
                        big = 1
                    else:
                        temp_loc = "Medium city"
            if fired == 1: 
                    break
        print (temp_loc)
        db_people_new.at[j, 'TypeOfLocation'] = temp_loc
        print(db_people_new.at[j, 'TypeOfLocation'])
        if big==1:
            db_people_new.at[j, 'CrimeRiskIndex'] = temp_crime

    return db_people_new


city_gmaps = gmaps_geometry_creator(city_list, api)
db_people_new = db_people_gmaps_enricher(db_people, city_gmaps)
db_people_new.to_csv('DemographicInfoData_processed.csv', index=False)

'''
Alternative ideas, not used in the last version:

df_otherInfo = pd.DataFrame()
df_otherInfo = df_otherInfo.append({'TypeOfLocation': temp_loc, 'CrimeRiskIndex': 9, 'height': 2}, ignore_index=True)
# db_people_new.at[j, 'TypeOfLocation'] = temp_city['TypeOfLocation']
# db_people_new.at[j, 'CrimeRiskIndex'] = temp_city['CrimeRiskIndex']
# city dimension and crime risk scoring
'''

def cleaning_db (df):
    '''
    function which clean the database with unwanted and unuseful columns
    and groups some data in categories
    '''
    # Working with age group and then deleting age
    df['AgeGroup'] = np.where(df['Age'] <= 24,"18-24", 
                              np.where(df['Age'] <=34, "25-34", 
                                       np.where(df['Age'] <=44, "35-44",
                                                np.where(df['Age'] <=54, "45-54",
                                                         ">55"))))
    df.drop('Age', axis=1, inplace=True)
    # Create an index which identifies if a person is fat or not (BMI or  Body Mass Index)
    df['BMI'] = df['Kilograms']/((df['Centimeters']/100)**2)
    df.drop(['Kilograms','Centimeters'], axis=1, inplace=True)
    # Define if a person has an old or new vehicle
    df['Vehicle_aging'] = np.where(df['Vehicle_aging'] >2012,"New", "Old")
    # Drop unuseful information 
    df.drop(['LFD_ID', 'PARENT_LFD_ID', 'StateFull', 'CountryFull', 'TelephoneCountryCode',
             'TropicalZodiac', 'Domain', 'BloodType'], axis=1, inplace=True)
    # Drop private information
    df.drop(['EmailAddress', 'CCType', 'Vehicle', 'Title'], axis=1, inplace=True)
    # Cleaning CrimeRiskIndex
    df['CrimeRisk'] = np.where(df['CrimeRiskIndex']>30, "Medium", np.where(df['CrimeRiskIndex']>0, "Low", "Unknown"))
    df.drop('CrimeRiskIndex', axis=1, inplace=True)

    return df


df_new = cleaning_db(db_people_new)

df_new.to_csv('DemographicInfoDataFinal.csv', index=False)