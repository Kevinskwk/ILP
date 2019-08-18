p=int(input(':'))
l=[]
lr=[]
for n in str(p):
    l.append(int(n))

for m in str(p):
    lr=[int(m)]+lr

if l==lr:
    i=True
else:
    i=False
print i
