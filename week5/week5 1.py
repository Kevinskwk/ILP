DNA=raw_input("DNA:")

d={'A':0, 'C':0,'G':0, 'T':0}
a=0
c=0
g=0
t=0
n=1
for i in DNA:
    if i=='A':
        a+=1
    elif i=='C':
        c+=1
    elif i=='G':
        g+=1
    elif i=='T':
        t+=1
    else:
        print 'The input DNA string is invalid'
        n=0
        break
if n==1:
    d['A']=a
    d['C']=c
    d['G']=g
    d['T']=t
    print d
    

