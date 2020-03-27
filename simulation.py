# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 08:48:55 2020

@author: abric
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters of the simulation 
N_pop = 100 
N_infected_initial = 5
N_days = 50
confinmentDay = 10
contactRatio = 1 

# Latences
T_incubation = 5
T_i1_mean = 6 
T_i2_mean = 6 

# Recovery rates
gamma1 = 0.1
gamma2 = 0.1

# Probability to move to next steps
pe1 = 1-1/T_incubation
p11 = 1/T_i1_mean 
p22 = 1/T_i2_mean 
p12 = p11 - gamma1
mu = p22 - gamma2 

# Variable parameters
beta1 = 0.5
beta2 = 0.5

# 1. Create the initial population 
pop = {} 
states = ['s','e','i1','i2','r','d']
for s in states: pop[s] = 0 
pop['s'] = N_pop-N_infected_initial
pop['i1'] = N_infected_initial
data = [np.fromiter(pop.values(), dtype=float)]

#%% 2. Start the simulation 
for i in range(N_days):
    
    if i == confinmentDay:
        contactRatio = 0.7
    
    newExposed = (beta1 * pop['i1'] + beta2 * pop['i2']) * pop['s'] / N_pop * contactRatio
    newi1 = pop['e'] * pe1
    newi2 = pop['i1'] * p12 
    newRecovered1 = gamma1 * pop['i1']
    newRecovered2 = gamma2 * pop['i2']
    newDeath = mu * pop['i2']
    
    # Update step
    pop['s'] -= newExposed
    pop['e'] += newExposed - newi1 
    pop['i1'] += newi1 - newi2 - newRecovered1
    pop['i2'] += newi2 - newDeath - newRecovered2
    pop['r'] += newRecovered1 + newRecovered2 
    pop['d'] += newDeath
    
    # Save the result
    data.append(np.fromiter(pop.values(), dtype=float))
    
data = np.transpose(np.array(data))

#%% 
labels=['s','e','i1','i2','r','d']
for line,label in zip(data,labels):
    plt.plot(line,label = label)
plt.legend()

    