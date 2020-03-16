# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:36:47 2020

@author: Arthur Bricq and Johan Felizas
"""
#%% Required imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%% Get the data 

path = "../COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
confirmed = pd.read_csv(path + "time_series_19-covid-Confirmed.csv")    
death = pd.read_csv(path + "time_series_19-covid-Deaths.csv")     
recovered = pd.read_csv(path + "time_series_19-covid-Recovered.csv")    

#%% Basic operations

# Count the number of infected persons 

def getNumberOfInfected():
    """
    Return the total number of infected persons
    """
    return sum(confirmed.iloc[:,-1])

print("Number of cases in the world: ", getNumberOfInfected())

def getNumberOfInfectedForCountry(country): 
    """
    Return the total number of infected persons in the given country.
    If country is wrong, returns -1
    """
    indexes = confirmed['Country/Region'] == country
    if not np.count_nonzero(indexes):
        return -1
    return sum(confirmed[indexes].iloc[:,-1])

print("Number of cases in France: ", getNumberOfInfectedForCountry('France'))


#%% Make some plots of what we want 

def getInfected(country,start,numberOfDays=confirmed.keys().shape[0]-4):
    """
    Returns an array with the cumulative number of infection starting from day start to day end.
    - start is supposed to be indexed (starting from 0)
    0 means it is day 1/22/20 (January 22)
    - numberOfDays: if not set, will display until last day
    """
    return sum(confirmed[confirmed['Country/Region'] == country].iloc[:,4+start:4+numberOfDays].values)

print(getInfected('France',0))

def getDateIndex(date):
    return np.argwhere(confirmed.columns == date)[0,0]-4


#%% Plots


plt.figure()
plt.plot(getInfected('France',getDateIndex('2/22/20')),'x',label='France')
plt.plot(getInfected('Italy',getDateIndex('2/22/20')),'x',label='Italy')
plt.xlabel('Number of days after February 22th')
plt.ylabel('Number of infected persons')
plt.legend()







