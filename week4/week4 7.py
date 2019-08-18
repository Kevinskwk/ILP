def interlock(s1,s2,s3):
    if len(s1)!=len(s2):
        return False
    elif len(s3)!=2*len(s1):
        return False
    else:
        for i in range(len(s1)):
            if s1[i]!=s3[2*i] or s2[i]!=s3[2*i+1]:
                return False
        return True

s1=raw_input('s1:')
s2=raw_input('s2:')
s3=raw_input('s3:')

print interlock(s1,s2,s3)
