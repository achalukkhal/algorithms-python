####################################################################
# Creator : Achal Ukkhal
# Date : 23 July 2018
# Class Information : 
#   Name : Dna
#   About : Stores the fitness score and genes for a element in population ie population[i]
####################################################################

import string
import random

class Dna:

    fitnessScore = 0
    dnaSequence = []
    dnaSize = 0

    def __init__(self, dnaSize):
        self.fitnessScore = 0
        self.dnaSize = dnaSize
        self.getNewGenes()

# Generating the DNA sequence for an element of size "n" where n is the lenght of the TARGET_STRING
    def getNewGenes(self):
        self.dnaSequence = list()
        for s in range(0, self.dnaSize):
            self.dnaSequence.append(self.getMeRandomCharactor()) 

# returns a random character between [a-z,A-Z] and " " (space)
    def getMeRandomCharactor(self):
        return random.choice(string.ascii_letters + " ")

# returns the Dna sequence as a String
    def getPhrase(self):
        return string.join(self.dnaSequence,'')

# generates a new dna sequence from a mating pool
    def getNewGenesFromMatingPool(self, matingPool, mutationRate, targetList):
        parentA = random.choice(matingPool)
        parentB = random.choice(matingPool)
        self.dnaSequence = self.crossOver( parentA, parentB, mutationRate, targetList)

# Crossover
    def crossOver(self, parentA, parentB, mutationRate, targetList):
        mid = (self.dnaSize-1) / 2
        child = []
        for i in range(0,self.dnaSize):
            child.append(parentA[i]) if(i < mid) else child.append(parentA[i]) 
        return self.mutation(child ,mutationRate, targetList)

# mutation  
    def mutation(self, child ,mutationRate, targetList):   
        # if mutationRate >= 1 :        
        for i in range(0, len(child)):
            if(child[i] != targetList[i]):
                if(mutationRate > random.choice(range(1,100))):
                    child[i] = self.getMeRandomCharactor()
        return child





