# Overview
Our backend is designed to be fully integrated. The problem we faced was to integrate score extracted from the social media from a sub sample to the whole data sample and do inference out of that.


# Data Description
For a total of more 260 thousands user data, the raw dataset used are three: 

 -  NEW_P_NAPA.csv
 
 -  NEW_P_PARTNERADRESSE.csv
 
 -  NEW_P_NAPA.csv

Data include the following sections:

- Demographic information about users, including age, sex, etc.

- Location information, including street name and geolocalization details.


# Data Enrichment

The first step of the analysis, has been to enrich current data with new features which could be helpful for the analysis.
In order to perform this the following steps have been performed:

- A dataset from United States Statistics has been added, containing cities with a population greater than 100'000 inhabitants in Germany.

- Three layers have been defined in the following manner: 

       Big cities, cities with more than 500'000 people (total 13 millions people)
    
       Mid-cities, cities between 100'000 and 500'000 (total 12 millions people)
    
       Rural and villages, defined as all the remaining population

- Additional data of Crime Index for each data have been taken, showing a risk score for main city. Data came from Nimbeo.com

On top, we added several information from the users that can help the social media clustering of users in categories of similar behaviours:

- 'age_range': 5 dummies for age, to identify different online behaviours --> users 18-24, 25-34, 45-55, >55

- 'bmi': an index which is defined as weight divided by the square of height, it is a proxy of how a certain person could be unfit.

- 'vehicle aging': an indicator of how old is the car and it is a proxy of how the person is open to the change


# Methods

## Demographics_metadata.py

In this file data have been reworked to added the two features previously described using GoogleMaps API. Firstly it is used:

**maps_geometry_creator(city_list, api)** which maps the geometry location of each major cities and add info on the geographical borders.

**gmaps_enricher(db_people, city_gmaps)** where data have been enriched of new features, associating for each of the 250,000 the area where the city was located at and attributing each profile to the latter categories, after having used GoogleMaps API


**Cleaning_DB** a function which takes data and clean them to the useful analysis


# Random Forest modeling

Scores concerning risk propension (deriving from Facebook data) and for Economic stability (deriving from Linkedin data) have been created in order to represent a target an usual situation, where data are only available in a small subset of the population (roughly 4 %).
With this method, we show is possible how social media don't gain more value on current users, but actually can give better estimates of the risk assessment for the whole population by assuming similar behaviour of similar people.

## RF model.py

The random forest model used for regression in the latter analysis

## RF main engine scoring.py

Here all the magic begins, predicting from 8000 data the scoring to the rest of data, by weighting different variables

## RF query predict scoring.py

Interaction with the front end and predcting a new user by adding new features 
A new query is evaluated by the algorithm, providing estimates for Risk Appetite and Stability



# Front end

