####################################################################
# Creator : Achal Ukkhal
# Date : 23 July 2018
# Information : Genetic Algorithm 
#           1. Initilization
#           2. Selection
#           3. Evolution
#               a. Cross-over
#               b. Mutation
####################################################################

import os
import population

# Change the variables and Expriment
TARGET_STRING = "In the struggle for survival Only the fittest survive"
POPULATION_COUNT = 1000
MUTATION_RATE = 0.03

#Initalizing the base population with POPULATION_COUNT, TARGET_STRING, MUTATION_RATE (%)
population =  population.Population(POPULATION_COUNT, TARGET_STRING, MUTATION_RATE)

#Loop for creating new Generation until we have a population with the matching TARGET_STRING
while (population.isFinished != True):
   os.system('clear')
   population.evaluate()
