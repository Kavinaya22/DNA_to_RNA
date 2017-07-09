from apcs import Window

x = 100
y = 100
dx = 0 #goes downwards or upwards , change
dy = 0 #goes downwards or upwards , change

def drawBackground():
    Window.out.backround("blue")

def drawBall(): #def= define, you are not calling the function btw
#why use def? - required in python3
    Window.out.color("white")
    Window.out.circle(x, y, 6)

#move the ball by its x and y position
def moveBall():
    global x, y, dx, dy
    x = x + dx
    y + y + dy

def detectHit():
    global x, y, dx, dy

    if abs(Window.mouse.getx() - x) < 20 and abs(Window.mouse.getY() - y) < 20:
        dx = x - Window.mouse.getX()
        dy = y - Window.mouse.getY()

def detectBounce():
    global x, y, dx, dy
    if x > 795:
        x = 5
        dx = -dx
    if x < 5:


    #collabedit.com/25qxe





Window.size(800, 800)
Window.frame(drawBall)
Window.frame(moveBall)
Window.frame(detectHit)
Window.start()
