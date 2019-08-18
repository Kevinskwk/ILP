l=[23,34,24,12,3,45,62,25]
length=len(l)

for i in range(length-1,0,-1):
    for x in range(i):
        if l[x]>l[x+1]:
            l[x],l[x+1] = l[x+1],l[x]

print l
