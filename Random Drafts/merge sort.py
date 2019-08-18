def merge(x,y):
    c=[]
    while len(x)!=0 and len(y)!=0:
        if x[0]<y[0]:
            c.append(x[0])
            x.remove(x[0])
        else:
            c.append(y[0])
            y.remove(y[0])
    if len(x) ==0:
        c+=y
    else:
        c+=x
    return c

def s(n):
    l=len(n)
    if l==0 or l==1:
        return n
    else:
        x=s(n[:l/2])
        y=s(n[l/2:])
        return merge(x,y)

def ll(n):
    l=[]
    for i in range(1,n+1):
        l=l+[i]
    return l
import time
for i in range(10000,50000,2500):
    l=ll(i)
    t1=time.time()
    s(l)
    t2=time.time()
    print (t2-t1)
