from apcs import Window
#COMMAND S TO SAVE THEN YOU CAN RUN!!!!
#if you deleted terminal, then just do cd Desktop and cd Kavinaya and finally python3 bouncingball.py
x = 100
y = 100
dx = 5
dy = 3
def drawBall(): #def= define, you are not calling the function btw
    global x, y, dx, dy  #you can change the value of x and y, only in a function
    Window.out.circle(x, y, 10)

    x = x + dx #dx is the change in the x value
    y = y + dy #dy is the change in the y value

    if x > 500 or x < 0:
        dx = -1 * dx
    if y > 500 or y < 0:
        dy = -1 *dy

Window.size(500,500)
Window.frame(drawBall)
Window.start() #makes window show up, in java it is already given
