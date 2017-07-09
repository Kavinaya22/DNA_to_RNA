from apcs import Window
from random import randint

x = 300
y = 700
coins = [{ "x": 100, "y": 100 }]

def catcher():
    global x, y
    Window.out.color("green")
    Window.out.circle(x, y, 20)
    x = Window.mouse.getX()
    if Window.key.pressed("a"):
        x = x - 10
    if Window.key.pressed("d"):
        x = x+10

def drawCoins():
    global coins
    for coin in coins:
        Window.out.color("yellow")
        Window.out.circle(coin["x"], coin["y"], 5)
        coin["y"] += 5

def addCoin():
    if randint(1, 10) == 1:
        coins.append({ "x": randint(20, 580), "y": -10})

def detectCoins():
    global coins
    for coin in coins:
        if abs(x - coin["x"] < 20 and abs(y - coin["y"]) < 20:
            coins.remove(coin)

Window.size(600, 800)
Window.frame(catcher)
Window.frame(drawCoins)
Window.frame(addCoin)
Window.frame(detectCoins)

Window.start()
