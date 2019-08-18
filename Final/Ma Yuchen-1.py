def myseries(n):
   s=n*(n+1)/2
   return s

def sqnum(n):
   root=n**0.5
   if root % 1 == 0:
      return True
   else:
      return False
   
print 'T100 = '+str(myseries(100))
print 'T2000 = '+str(myseries(2000))
print 'T50000 = '+str(myseries(50000))

i=0
n=8
SquareNumbers=[]
while i<2:
   n+=1
   T = myseries(n)
   if sqnum(T) == True:
      i+=1
      SquareNumbers.append(T)


print "The next two square nambers are:"
for x in SquareNumbers:
   print x
   

