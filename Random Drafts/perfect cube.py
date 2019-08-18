import time

n=int(input("imput cube number:"))

i=0
start=time.time()
while (i**3 < abs(n)):
    i=i+1
end=time.time()

if i**3 != abs(n):
    print n,"is not a perfect cube"
else:
    if n<0 :
        i=-i
    print i

elapsedtime = end-start
print"time is:",elapsedtime
