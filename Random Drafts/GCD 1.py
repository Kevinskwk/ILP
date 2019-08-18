def gcd(a,b):
    if a==b:
        return a
    else:
        return gcd(abs(a-b),min(a,b))

a=input("a:")
b=input("b:")

print gcd(a,b)
