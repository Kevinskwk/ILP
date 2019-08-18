
def age():
    a=raw_input("What's your age?\n")
    try:
        a=int(float(a))
        if a<0:
            print"Your age cannot be negative! Type again!"
            age()
        elif 0<=a<=50:
            print"Young and Naive!"
        elif 50<a<=100:
            print"You are dying!"
        else:
            print"You are still alive?"
    except:
        print"Please input a number! Type again!"
        age()


age()

    
        
