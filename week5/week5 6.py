def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

n=int(input('n:'))

print f(n)
        
