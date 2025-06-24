import random
from phrase import Phrase, target
from helpers import summarize 


popSize=100

population=[]
bestScore=0
generation=1


 
for i in range(popSize):
    population.append(Phrase())


while bestScore < len(target):

    for i in range(popSize):
        population[i].getFitness()
        if population[i].fitness > bestScore :
            bestScore=population[i].fitness
            summarize(generation,population[i].getContents(),bestScore)

    matingPool=[]
    parents=population[:]
    population=[]

    for i in range(popSize):
        for j in range(parents[i].fitness):
            matingPool.append(parents[i])
            
    for i in range(popSize):
        parentA=random.choice(matingPool)
        parentB=random.choice(matingPool)
        
        child=parentA.crossOver(parentB)
        child.mutate()

        population.append(child)
    generation+=1

