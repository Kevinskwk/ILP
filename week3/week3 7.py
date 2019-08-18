lista = [[1,2,4],[4,5,6],[7,8,9]]
listb = []

for x in lista:
    l = len(x)
    t=0.0
    for y in x:
        t+=y
    listb.append(round(t/l,2))

print listb
        
