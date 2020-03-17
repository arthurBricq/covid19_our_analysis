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


#%% data to be used  

countries = ['Italy','France','Switzerland','Spain','Netherlands']
populations = [60.5e6, 67e6, 8.6e6, 46.6e6, 17.2e6]
n_countries = [0,8,5,5,9]
date = '2/22/20'




#%% 
# For the ongoing part, I want to compare one european country with Italy, which can be quite tricky
# One one plot, we are going to show Italy, the country X, and the country X shifted by n_x days 

countryIndex = 4
country = countries[countryIndex]
n = n_countries[countryIndex]
y_italy = getInfected('Italy',getDateIndex(date)) / populations[0]
y_country = getInfected(country,getDateIndex(date)) / populations[countryIndex]
plt.figure()
# Italy is the reference 
plt.plot(y_italy,'x',label='Italy')
# Plot the second country
plt.plot(y_country,'x',label=country)
plt.plot(y_country[n:],'x-.',label=country + ' shifted by ' + str(n) + ' days')
plt.xlabel('Number of days after ' + date)
plt.ylabel('Ratio of infected persons')
plt.title('Italy versus ' + country + '  (normalized by population) \nDays lagging behind Italy: ' + str(n))
plt.legend()

#%% Make of this a nice plot that recap this situation in europe

title = 'Analysis of Covid-19 for different european countries \n' 
title += 'Normalised populations are used to compare the progress of the virus.\n'
title += 'Italy is used as the reference to compare other european countries.\n'
title += 'Each country is shifted by an amount of days and then compared with Italy.\n'
title += 'A. Bricq & J. Felisaz - updated on ' + confirmed.columns[-1]

fig = plt.figure(figsize = (15,18))
#fig.suptitle('bold figure suptitle', fontsize=14, fontweight='bold')
plt.figtext(0.1, 0.98, title, fontsize = 20, linespacing = 2)

for i in range(1,len(countries)):

    country = countries[i]
    n = n_countries[i]
    y_italy = getInfected('Italy',getDateIndex(date)) / populations[0]
    y_country = getInfected(country,getDateIndex(date)) / populations[i]
    
    plt.subplot(2,2,i)
    plt.plot(y_italy,'x',label='Italy')
    plt.plot(y_country,'x',label=country)
    plt.plot(y_country[n:],'x-.',label=country + ' shifted by ' + str(n) + ' days')
    plt.xlabel('Number of days after ' + date)
    plt.ylabel('Ratio of infected persons')
    plt.title('Italy versus ' + country + ' \nDays lagging behind Italy: ' + str(n))
    plt.legend()
    







