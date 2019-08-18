def diff(p):
    dp={}
    if 0 in p:
        del p[0]
    for i in p:
        p[i]=p[i]*i
        dp[i-1]=p[i]
    return dp

p={0:-3,3:2,5:-1}
print diff(p)

            
