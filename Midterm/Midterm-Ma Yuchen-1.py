t= int(input("Input base 10 number:"))
d=''
while t!=0:
    d=str(t%2)+d
    t=t/2

print ("The corresponding base 2 number is: "+d)

