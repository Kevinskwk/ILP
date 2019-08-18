import random

def median(l):
    l.sort()
    length=len(l)
    if length%2==0:
        m=(l[length/2]+l[length/2-1])/2.0
    else:
        m=l[length/2]
    return m
 
def flip(numFlips):
    heads = 0.0
    for i in range(numFlips):
        if random.random() < 0.5:
            heads += 1
    return heads/numFlips
 
def flipSim(numFlipsPerTrial, numTrials):
    fracHeads = []
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    return median(fracHeads)
    
print flipSim(100, 1)
print flipSim(100, 10)
print flipSim(100, 100)
print flipSim(100, 1000)
print flipSim(100, 10000)
print flipSim(100, 100000)
