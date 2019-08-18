lista = [[1,2,3],[4,5,6],[7,8,9]]

n=len(lista[1])
listb = []
for i in range(n):
    listb.append([])
print listb
for x in lista:
    for y in range(n):
        listb[y].append(x[y])

print listb

