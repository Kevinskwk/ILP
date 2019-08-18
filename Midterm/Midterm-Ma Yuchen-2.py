i=1
a=0
b=1
while b<=10**999:
    a,b=b,a+b
    i+=1


print ("The "+str(i)+"th term is the first term to have 1000 digits.\n")

print ("The number is:\n"+str(b))
