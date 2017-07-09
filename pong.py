from apcs import Window
#when the blue light pings, then save: command S

#ball position
x, y, dx, dy = 400, 300, 5, 0

#paddle1y = 300, paddle2y = 300
paddle1y, paddle2y = 300, 300

#work on background
def drawBackground():
    Window.out.background("grey")
    Window.out.color("dark blue")
    Window.out.circle(50, 300, 50)
    Window.out.color("white")
    Window.out.circle(50, 300, 46)
    pass

def drawBall():
    Window.out.color("yellow")
    Window.out.circle(x, y, 10)
    pass

def moveBall():
    global x, y, dx, dy
    x += dx
    y += dy
    pass

def drawPaddle():
    Window.out.color("black")
    Window.out.rectangle(50, paddle1y, 10, 100) #50 = xposition, paddle1y = paddle 1 y position,
    Window.out.color("red")
    Window.out.rectangle(750, paddle2y, 10, 100)
    pass

def movePaddle():
    global paddle1y, paddle2y
    if Window.key.pressed("q"):
        paddle1y -= 10
    if Window.key.pressed("w"):
        paddle1y += 10
    if Window.key.pressed("e"):
        paddle2y -= 10
    if Window.key.pressed("r"):
        paddle2y += 10
    pass


def checkBounce():
    global dx, dy
    if x< 10 or x> 790:
        dx = -dx
    if y< 10 or y> 590:
        dy = -dy
    pass

#Make sure you always use a : not a semicolon
def checkPaddle():
    global dx, dy
    if abs(x - 740) <= 10 and abs(y - paddle2y) <= 50:
        dx = -dx
        dy = dy + (y - paddle2y) / 10
    if abs(x - 60) <= 10 and abs(y - paddle1y) <= 50:
        dx = -dx
        dy = dy + (y- paddle1y) /10
    pass

def checkScore():
    pass

#set size
Window.size(800, 600)

#functions for drawing the Frame
Window.frame(drawBackground)
Window.frame(drawBall)
Window.frame(moveBall)
Window.frame(drawPaddle)
Window.frame(movePaddle)
Window.frame(checkBounce)
Window.frame(checkPaddle)
Window.frame(checkScore)

#start animation
Window.start()
