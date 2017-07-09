from apcs import Window

x = 400
y = 200

def tree():
    global x, y
    #trunk
    Window.out.color("brown")
    Window.out.rectangle(410, 350, 30, 250)
    #leaves
    Window.out.color("green")
    Window.out.circle(380, 180, 60)
    Window.out.circle(380, 120, 60)
    Window.out.circle(440, 120, 60)
    Window.out.circle(440, 180, 60)




Window.size(800, 800)
Window.frame(tree)

Window.start()
