# Simulation Presentation

The COVID-19 virus is striking the world and there is an evident lack on data to handle the problem with the most efficient stragety. Politicians and decision-making instances have this need of accurate data. That is why we want to see if it is possible to create a new mathematical model of the virus, to better predict the evolution of the virus on countries where we have accurate and local data about the virus

We will participate to the Hackaton done in Lausanne and sponsored by EPFL, to construct this model in 3 days. If you wish to participate with us, we are recruiting talents for our team. 

We have access to very accurate and updated database from many regions accross the world (at least every western country has accurate database). 

We already worked with this data, you can checkout this link : [data processing link]: 'README.md'

## The model that we have so far

We already started to develop a model that's quite complex to simulate a population. 

This model includes 5 types of persons
1. Susceptible subjects
2. Exposed subjects
3. Infected subjects of type 1
4. Infected subjects of type 2
5. Recovered subjects
6. Dead subjects

Our model also includes different confinement strategies, to take into account the influence of the confinment in this region. Using our dynamic model, we already obtained promising results that have already been observed with epydimic spreading in the past. 

!['figures/sim.png']

Those resultst are not fitting (yet) what has been observed with the COVID-19, and there are many parameters to tune in order to make our model accurante. 
We also want to make the model more complex by 
- including a third type of persons (Infected subjects of type 3), by also
- including a model of the testing strategies of the different regions
- including in the first model the health conditions of the hostpitals of the region. 

Once our model will be ready, we would like to apply machine learning techniques to train our model (i.e. find the optimal parameters) in order to match the actual propoagatin of the virus observed in some regions. If this works, we would then be able to use this model to best predict the evolution of the virus in other regions, which could help decision makers to take the best decision. 
