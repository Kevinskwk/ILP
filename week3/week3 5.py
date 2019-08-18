n = int(input(":"))

if n<=1:
    print("None")
else:
    listn=[]
    i=2
    while i<=n:
        listn.append(i)
        i+=1
    for x in range(n):
        l=len(listn)
        for y in listn[x+1:l]:
            if y%listn[x]==0:
                listn.remove(y)
        
print listn
