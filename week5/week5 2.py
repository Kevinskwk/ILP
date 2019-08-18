ip=[9,30,3,9,3,2,4,4,4,4,4]
op=[]
dic={}
for i in ip:
    if i not in dic:
        dic[i]=1
    if i in dic:
        dic[i]+=1
print dic
m=0
for i in dic:
    if dic[i]>m:
        m=dic[i]
        op=[i]
    elif dic[i]==m:
        op.append(i)

print op

        
        
