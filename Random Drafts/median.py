def median(l):
    
    l.sort()
    length=len(l)
    if length%2==0:
        m=(l[length/2]+l[length/2-1])/2.0
    else:
        m=l[length/2]
    return m

import random

def Ivan():
    s=random.randint(1,100)
    if s<=10:
        return 1
    else:
        return 0

def play():
    l=[]
    for i in range(5):
        l.append(Ivan())
    if l==[0,0,0,0,1]:
        return 1
    else:
        return 0

def trial(n):
    t=0
    for i in range(n):
        p=play()
        if p==1:
            t+=1
    return t

def Sim(n):
    f=[]
    for i in range(n):
        f.append(trial(100000))
    return median(f)

print Sim(1)
print Sim(10)
print Sim(100)
        
        
        
        
