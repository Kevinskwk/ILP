def decomp(x):
    r=''
    im=''
    l=[]
    if '+' in x or '-' in x:
        for i in x:
            l.append(i)
        for y in range(0,len(l),1):
            if l[y] !='+' and l[y] !='-':
                r+=str(l[y])
            else:
                ll=l[y:]
                break
        for z in range(len(ll)):
            if ll[z]!='i':
                im+=str(ll[z])
        if len(im)==1:
            im+=str(1)
        if len(r)==0:
            r=0
        return [float(r),float(im)]

    else:
        if 'i' in x:
            for y in x:
                l.append(y)
            for z in range(len(l)):
                if l[z]!='i':
                    im+=str(l[z])
            if im=='':
                im=1
            if im=='-':
                im=-1
            return [0.0,float(im)]
        else:
            return [float(x),0.0]
            
def add(a,b):
    x=a[0]+b[0]
    y=a[1]+b[1]
    return [x,y]

def subtract(a,b):
    x=a[0]-b[0]
    y=a[1]-b[1]
    return [x,y]

def multiply(a,b):
    x=a[0]*b[0]-a[1]*b[1]
    y=a[0]*b[1]+a[1]*b[0]
    return [x,y]

def divide(a,b):
    x=(a[0]*b[0]+a[1]*b[1])/float((b[0])**2+(b[1])**2)
    y=(a[1]*b[0]-a[0]*b[1])/float((b[0])**2+(b[1])**2)
    return [x,y]

def output(n):
    if n[0]==0:
        return str(n[1])+'i'
    elif n[1]==0:
        return str(n[0])
    elif n[1]>0:
        return str(n[0]) + '+' + str(n[1]) + 'i'
    else:
        return str(n[0]) + str(n[1]) + 'i'

a=raw_input('complex1 :')
b=raw_input('complex2 :')
op=raw_input('operator:')

if ' ' in a or ' ' in b:
    print 'no space allowed'
else:
    a=decomp(a)
    b=decomp(b)

    if op=='add':
        print output(add(a,b))
    elif op=='subtract':
        print output(subtract(a,b))
    elif op=='multiply':
        print output(multiply(a,b))
    elif op=='divide':
        if b==[0,0]:
            print 'divisor cannot be zero'
        else:
            print output(divide(a,b))
    else:
        print 'invalid operator'



        
    
        
            
