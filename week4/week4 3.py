def prime(n):
    i=1
    if n%2==0:
        i=0
    else:
        for x in range(3,int(n**0.5)+1,2):
            if n%x==0:
                i=0
                break
    if i==1:
        return 1
    else:
        return 0

import time
c=1
n=1
t1=time.time()
while c<9999:
    n+=2
    if prime(n)==1:
        c+=1
t2=time.time()         
print n
print (t2-t1)    
    
