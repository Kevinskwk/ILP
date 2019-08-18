from math import *
n=7
m1=1.0
m2=float(100**n)
v1=0.0
v2=-1.0
t=0
i=-1

   

while v1>v2 or v1<0:
   if i==-1:
      u1=(v1*(m1-m2)+2*m2*v2)/(m1+m2)
      v2=(v2*(m2-m1)+2*m1*v1)/(m1+m2)
      v1=u1
   else:
      v1=-v1
   t+=1
   i*=-1

print t
      
