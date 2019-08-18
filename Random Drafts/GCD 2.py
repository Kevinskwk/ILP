x=int(input('x:'))
y=int(input('y:'))

while (y):
    x,y=y,x%y
    
print x 
    

a=int(input('a:'))
b=int(input('b:'))

i=a
while a%i != 0 or b%i != 0:
    i-=1

print i

