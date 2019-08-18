#Calculating Human Development Index (HDI)
#Input: Life Expectancy, Mean years of schooling, Expected years of schooling, GNI

def HDI(LE,MYS,EYS,GNI):
    import math
    LEI=(LE-20.0)/(65.0)
    if LEI>=1:
        LEI=1.0
    if LEI<=0:
        LEI=0.0

    EI=0.5*(MYS/15.0+EYS/18)
    if EI>=1:
        EI=1.0
    if EI<=0:
        EI=0.0

    II=(math.log(GNI)-math.log(100))/(math.log(75000)-math.log(100))
    if II>=1:
        II=1.0
    if II<=0:
        II=0.0

    HDI=(LEI*EI*II)**(1/3.0)

    return HDI

LE=float(input("LE:"))
MYS=float(input("MYS:"))
EYS=float(input("EYS:"))
GNI=float(input("GNI:"))

print HDI(LE,MYS,EYS,GNI)

    
