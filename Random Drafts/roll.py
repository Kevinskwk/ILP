import random
def dice():
    return random.choice((0,1))

def rolln(n):
    r=''
    for i in range(n):
        r=r+str(dice())
    return r

s=0
while rolln(10)!='0000000000':
    print rolln(10)
    s+=1

print ("Found 0*10")

print s
