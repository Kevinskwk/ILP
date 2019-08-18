n=int(input(":"))

t=False
for x in range(1,n):
    for y in range(1,n):
        if x**2+y**2==n:
            t=True
            break

if t==True:
    print ("Yes!")
else:
    print("No")
            
