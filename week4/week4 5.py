def f(a,b,c):
    x=1
    for i in range(2,min(a,b,c)+1):
        if a%i==0 and b%1==0 and c%i==0:
            x=0
            break
    if a**2+b**2==c**2 and x==1:
        return True
    else:
        return False

a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

print f(a,b,c)
