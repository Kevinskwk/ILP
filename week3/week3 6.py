lista=[1,2,3,4,5,6,7,8,8]
l=len(lista)
n=False
for x in range(l):
    for y in range(l):
        if x!=y and lista[y]==lista[x]:
            n=True

if n==True:
    print ('Yes')
else:
    print('No')
            
