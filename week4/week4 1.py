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
listn.append(-3)
listt=[]
for i in range(1,len(listn)-1):
    listt.append(listn[i])
    if listn[i+1]!=listn[i]+2:
        if len(listt)>=2:
            print listt
            listt=[]
        else:
            listt=[]



        
