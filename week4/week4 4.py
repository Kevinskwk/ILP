a=int(input("a:"))
b=int(input("b:"))

l=[]
for i in range(1,1000):
    if i%a==0 or i%b==0:
        l.append(i)
s=0
for n in l:
    s+=n

print s
    
       
