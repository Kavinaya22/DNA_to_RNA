from apcs import Window

Window.size(500, 500)

def drawRainbow():
    Window.out.color("red")
    Window.out.circle(250, 500, 250)
    Window.out.color("orange")
    Window.out.circle(250, 500, 225)

Window.frame(drawRainbow)
Window.start()
