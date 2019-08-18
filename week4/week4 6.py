def f(n):
    l=[]
    b=0
    c=1
    while c <n:
        l.append(c)
        b,c=c,b+c
    s=0
    for i in l:
        if i%2==0:
            s+=i
    return s


n=input("input integer:")
print f(n)
