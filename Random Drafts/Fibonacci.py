n=input("input integer:")
s=""
i=0
b=0
c=1
while i <n-1:
    s=s+str(c)+", "
    b,c=c,b+c
    i+=1

if i==n-1:
    s=s+str(c)
print(str(s))
    
