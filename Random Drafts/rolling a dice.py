import random
def dice():
    return random.randint(1,6)

n=100000
l=[0,0,0,0,0,0]
r=[0,0,0,0,0,0]
for i in range(n):
    l[dice()-1]+=1

s=0
a=1/6.0
for x in range(2):
    r[x]=l[x]/float(n)
    s+=(abs(r[x]-a))**2
s=s/6.0
print l
print r
print s



