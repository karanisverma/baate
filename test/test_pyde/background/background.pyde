

bgAni = True
def setup():
    size(1241, 877)

def draw():
    global bgAni

    if bgAni:
        bg = loadImage("pheart.jpg")
        background(bg)
        bgAni = False
        print("If part")
        delay(500)
    else:
        print("Else part")
        bg1 = loadImage("pheart_pumping.jpg")
        background(bg1)
        bgAni = True
        delay(500)

#     delay(1000)
#     redraw()
#     background(0)
#         bg = loadImage("pheart_pumping.jpg")
#         background(bg)
#         delay(1000)

