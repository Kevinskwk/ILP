def CnF(a,b):
    if a=="F" or a =="f":
        f = 1.8*b+32
        return f
    elif a == "C" or a =="c":
        c = (5.0/9)*(b-32)
        return c
    else:
        return "Wrong input"
    


a=raw_input("type:")
b=float(input("temperature:"))
print CnF(a,b)



