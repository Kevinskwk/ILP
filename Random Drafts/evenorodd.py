def evenorodd() :
    X= raw_input("input number")
    if X=="Are you Gaoxin?":
        print("Ni Hai Xing")
        evenorodd()
    elif unicode(X).isnumeric():
        x=int(X)
        if type(x)!= int:
            print ("wtf???")
            evenorodd()
        elif x%2 == 0 :
            print ("even")
            print ("done")
        else:
            print ("odd")
            print ("done")
    else:
        print("wtf???")
        evenorodd()


evenorodd()
