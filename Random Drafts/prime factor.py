n=int(input(':'))
listf=[]
listpf=[]
for x in range(1,n+1):
    if n%x==0:
        listf.append(x)

print listf

for y in listf:
    l=[]
    for z in range(1,y+1):
        if y%z==0:
            l.append(z)
    if len(l)==2:
        listpf.append(y)

print listpf
