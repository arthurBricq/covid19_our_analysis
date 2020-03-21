# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:36:47 2020

@author: Arthur Bricq and Johan Felizas
"""
#%% Required imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import system 


#%% Get the data 

path = "../COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
confirmed = pd.read_csv(path + "time_series_19-covid-Confirmed.csv")    
death = pd.read_csv(path + "time_series_19-covid-Deaths.csv")     
recovered = pd.read_csv(path + "time_series_19-covid-Recovered.csv")    

#%% Basic operations


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


def getInfected(country,start,numberOfDays=confirmed.keys().shape[0]-4):
    """
    Returns an array with the cumulative number of infection starting from day start to day end.
    - start is supposed to be indexed (starting from 0)
    0 means it is day 1/22/20 (January 22)
    - numberOfDays: if not set, will display until last day
    """
    return sum(confirmed[confirmed['Country/Region'] == country].iloc[:,4+start:4+numberOfDays].values)

def getDeaths(country,start,numberOfDays=confirmed.keys().shape[0]-4):
    """
    Returns an array with the cumulative number of death starting from day start to day end.
    - start is supposed to be indexed (starting from 0)
    0 means it is day 1/22/20 (January 22)
    - numberOfDays: if not set, will display until last day
    """
    return sum(death[confirmed['Country/Region'] == country].iloc[:,4+start:4+numberOfDays].values)

def getRecovered(country,start,numberOfDays=confirmed.keys().shape[0]-4):
    """
    Returns an array with the cumulative number of recovered starting from day start to day end.
    - start is supposed to be indexed (starting from 0)
    0 means it is day 1/22/20 (January 22)
    - numberOfDays: if not set, will display until last day
    """
    return sum(recovered[confirmed['Country/Region'] == country].iloc[:,4+start:4+numberOfDays].values)

def getDateIndex(date):
    """
    Return the index of the given date. This function is used to plot the data starting at the given date
    """
    return np.argwhere(confirmed.columns == date)[0,0]-4



#%% data to be used to generate the plots

countries = ['Italy','France','Switzerland','Spain','Netherlands','US']
populations = [60.5e6, 67e6, 8.6e6, 46.6e6, 17.2e6,328e6]
n_countries = [0,9,3,5,10,10]
date = '2/22/20'

# For the ongoing part, I want to compare one european country with Italy, which can be quite tricky
# One one plot, we are going to show Italy, the country X, and the country X shifted by n_x days 

#%% Plot 1: normalised infection in different countries 

fig1, axs = plt.subplots(2,2,figsize = (10,12))
axs = axs.ravel()

for i, ax in enumerate(axs):

    country = countries[i+1]
    n = n_countries[i+1]
    y_italy = getInfected('Italy',getDateIndex(date)) / populations[0]
    y_country = getInfected(country,getDateIndex(date)) / populations[i+1]
    
    ax.plot(y_italy,'x',label='Italy')
    ax.plot(y_country,'x',label=country)
    ax.plot(y_country[n:],'x-.',label=country + ' shifted by ' + str(n) + ' days')
    ax.set_xlabel('Number of days after ' + date)
    ax.set_ylabel('Ratio of infected persons')
    ax.set_title('Italy versus ' + country + ' \nDays lagging behind Italy: ' + str(n) + '\nNumber of cases : ' + str(getNumberOfInfectedForCountry(country)))
    ax.legend()
    
fig1.subplots_adjust(wspace=0.3,hspace=0.4)
fig1.suptitle('COVID-19 Comparison of different normalised european countries \nDate : '+ confirmed.columns[-1])

    
#%% Plot 2: number of new cases and cumulative cases for different european countries

fig2, axs = plt.subplots(3,2,figsize = (10,15))
axs = axs.ravel()

for i, ax in enumerate(axs):
    
    country = countries[i]
    n = n_countries[i]
    cumulative = getInfected(country,getDateIndex(date)) 
    newCases = cumulative[1:]-cumulative[:-1]
    
    x = range(len(cumulative))
    fit = np.polyfit(np.log(x[-10:]),np.log(cumulative[-10:]),1)
    print(fit)
    
    ax.set_title(country + '  (' + str(getNumberOfInfectedForCountry(country)) + ' cases)')
    ax1 = ax
    
    ax1.bar(np.arange(len(newCases)),newCases,label='New cases per day')
    ax1.set_xlabel('Number of days after ' + date)
    ax1.set_ylabel('New cases per day')
    ax1.tick_params(axis='y')
    
    ax2 = ax1.twinx()
    
    ax2.plot(x,cumulative,color = 'red',label='Total number of cases')
    ax2.set_ylabel('Total number of cases')
    ax2.tick_params(axis='y', labelcolor='red')
    # ax2.plot(np.log(x), np.log(fit[0] * x + fit[1]))
    
    
fig2.subplots_adjust(wspace=0.8,hspace=0.4)
fig2.suptitle('COVID-19 Number of cases in various countries \nDate : '+ confirmed.columns[-1])

#%% Plot 3: Infected, Death and Recoverded


fig3, axs = plt.subplots(3,2,figsize = (10,15))
axs = axs.ravel()
date = '3/10/20'

for i, ax in enumerate(axs):
    country = countries[i]
    n = n_countries[i]
    cumulative = getInfected(country,getDateIndex(date)) 
    deaths = getDeaths(country,getDateIndex(date))
    recovereds = getRecovered(country,getDateIndex(date))   
    
    x = np.arange(len(cumulative)) # range(len(cumulative))
    width = 0.5
    
    
    title = country + ' \n(Infected, Deads, Recovered)\n({},  {},  {})'.format(cumulative[-1],deaths[-1],recovereds[-1]) 
    ax.set_title(title)    
    ax.bar(x,cumulative,width, label='Infected')
    ax.bar(x,deaths,width, bottom=cumulative,label = 'Deads')
    ax.bar(x,recovereds,width,bottom=cumulative+deaths, label = 'Recovered')
    ax.set_xlabel('Number of days after ' + date)
    ax.legend()
    #ax.tick_params(axis='y')
    

fig3.subplots_adjust(wspace=0.8,hspace=0.4)
fig3.suptitle('COVID-19 Number of infected, deaths and recovered in various countries \nDate : '+ confirmed.columns[-1])


#%% Export the figures 

today = confirmed.columns[-1]
todayFormated = today[2:4] + '_' + today[0]
fig1.savefig('figures/_normalisedComparisonWithItaly')
fig2.savefig('figures/_numberOfCases')
fig3.savefig('figures/_infectedDeathsRecovered')

#%% Push them to github (if wanted, password required) 

system("git add figures")
system("git commit -m \"Adding new figures\"")
system("git push")
