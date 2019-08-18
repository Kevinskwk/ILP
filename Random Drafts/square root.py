n=float(input(":"))
error =0
guess = 0
previous = 1.0
new = 0.5*(previous+n/previous)
while abs(new-previous)> error:
    previous , new = new , 0.5*(new+n/new)
    guess+=1

print new
print ("guesses:"+str(guess))
