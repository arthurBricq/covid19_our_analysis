# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:36:47 2020

@author: Arthur Bricq and Johan Felizas
"""


#%% Required imports
import pandas as pd

#%% Get the data 
path = "../COVID-19/csse_covid_19_data/csse_covid_19_time_series/"
confirmed = pd.read_csv(path + "time_series_19-covid-Confirmed.csv")    
death = pd.read_csv(path + "time_series_19-covid-Deaths.csv")     
recovered = pd.read_csv(path + "time_series_19-covid-Recovered.csv")    