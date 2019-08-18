n=int(input(":"))
i=1
d=0
while i<=n:
    if n%i ==0:
        d+=1
    i+=1

if d==2:
    print ("True")
else:
    print ("False")

