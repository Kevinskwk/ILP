import turtle

def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,200)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1600,900,0,0)
    pythonsize = 25
    turtle.pensize(pythonsize)
    turtle.pencolor("purple")
    turtle.seth(-30)
    drawSnake(31,95,8,pythonsize*2)

main()
