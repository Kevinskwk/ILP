n = int(input())
d=2
f=[]
while n%d==0:
    f.append(d)
    n=n/d
d=3
while n>1 and d*d<=n:
    if n%d==0:
        f.append(d)
        n=n/d
    else:
        d=d+2
if n>1:
    f.append(n)

print f
