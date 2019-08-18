def h(d):
    m=0
    for i in d:
        if d[i]>m:
            m=d[i]
            name=str(i)
        elif d[i]==m:
            name=name+', '+str(i)
    return name

d={'Harry': 8, 'Alice': 9, 'John': 5, 'Jane' : 6}
print h(d)
