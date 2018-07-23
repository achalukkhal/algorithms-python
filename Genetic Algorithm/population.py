####################################################################
# Creator : Achal Ukkhal
# Date : 23 July 2018
# Class Information : 
#   Name : Population
#   About : Generates population for "n" generation
####################################################################

import dna
import string
import math
from termcolor import colored


class Population:

    populationList = []
    populationSize = 0
    populationFitness = 0
    generationCount = 1
    targetPhrase = ""
    dnaSize = 0
    matingPool = []
    mutationRate = 0
    maxFitness = 0
    generationBest = ""
    isFinished = False
    
# Defining Basic Parameters for Base Population
    def __init__(self, populationSize, target, mutation):
        self.targetPhrase = target
        self.populationSize = populationSize
        self.dnaSize = len(self.targetPhrase)
        self.mutationRate =  int(mutation * 100)

        self.generationCount = self.generationCount+1
        for population in range(0,populationSize+1):
            self.populationList.append(dna.Dna(self.dnaSize))
        

# Calculate the fitenss of every element in the population
    def calculateFitness(self, target):
        targetList = list(target)
        for population in self.populationList: 
            score = 0     
            for i in range(0, len(targetList)):
                if targetList[i] == population.dnaSequence[i]:
                    score = score + 1

            population.fitnessScore = score
            self.populationFitness = self.populationFitness + score 
            if (self.maxFitness <= score):
                self.maxFitness = score
                self.generationBest = string.join(population.dnaSequence,'')
                
            if ( self.generationBest == self.targetPhrase):
                self.isFinished = True
              

# Generates a mating pool that is population[i] * population[i].fitness
    def createMatingPool(self):
        self.matingPool = []
        for population in self.populationList:
            if population.fitnessScore >= 1 : 
                for score in range(0, (population.fitnessScore / self.maxFitness) * 100  + 1):
                    self.matingPool.append(population.dnaSequence)

# Generates a new Generation from the mating pool
    def generateNewGeneration(self):
        self.generationCount = self.generationCount + 1
        self.maxFitness = 0
        self.populationFitness = 0
        for population in self.populationList:
            population.getNewGenesFromMatingPool(self.matingPool, self.mutationRate, list(self.targetPhrase))

# Evaluates the generation for a Matching TARGET_STRING
    def evaluate(self):
            self.calculateFitness(self.targetPhrase)
            self.showpopulationStats()
            self.createMatingPool()
            self.generateNewGeneration()
            

# Displays Deneration Information
    def showpopulationStats(self):
        print "\n \t================================ GENETIC ALGORITHM ================================ \n"
        print "\t\tTarget Phrase : ", self.targetPhrase 
        print "\t\tpopulation Size :", self.populationSize
        print "\t\tMutation Rate :", self.mutationRate, "%"
        print "\t\tCurrent Generation :", self.generationCount
        print "\t\tGeneration Best : " + colored(self.generationBest, "green" )
        print "\t\tGeneration Fitness :", self.populationFitness / self.populationSize, "% \n"