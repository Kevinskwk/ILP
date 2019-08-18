def s(n):
    return n*(n+1)/2

def d(x):
    n=0
    for i in range(1,1+int(x**0.5)):
        if x%i ==0:
            n+=2
    if x**0.5 %1==0:
       n-=1
    return n

n=1
while d(s(n))<500:
    n+=1

print s(n)
    

    
