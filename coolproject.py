from apcs import Window
from random import randint, choice

#randit = random integer

balls = []
#this command isn't really necessary i is not intended to do anything
for i in range(100):
    #               0 - x           1-y                 2 - dx          3 -dy
    balls.append( [ randint(0, 500), randint(0, 500), randint(-5, 5), randint(-5,5)])

def drawBalls():
    for ball in balls:
        Window.out.color(ball[4])
        Window.out.circle(ball[0], ball[1], 5)

def moveBalls():
    global balls   #wassupgAAAAys
    for ball in balls:
        ball[0] += ball[2]
        ball[1] += ball[3]

        if ball[0] < 5 or ball[0] > 495:
            ball[2] = -ball[2]
        if ball[1] < 5 or ball[0] > 495:
            ball[3] = -ball[3]
    pass

Window.size(500, 500)
Window.frame(drawBalls)
Window.frame(moveBalls)
Window.start()
