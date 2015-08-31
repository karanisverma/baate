from __future__ import division
PerMonth = {1: 21183, 2: 18801, 3: 25388, 4: 14609}
i = 1
ylimit = 100
test = False
j = 1

def bargraph(x, y, height, width, dict):
    i = 1
    maxv = 1
    xval = 0
    yval = 0
    for a, b in dict.items():
        if y > maxv:
            maxv = b
    xUnit = width / len(dict)
    yUnit = height / maxv
    for index, val in dict.items():
        xval += xUnit
        yval = val * yUnit
        rect(xval+x,y, 10, -yval)

def setup():
    size(360, 360)
    stroke(255)

def draw():
    background(0)
    bargraph(0, 355, 250, 250, PerMonth)
    test = True
    # bargraph(x,y,height,width,dict)

def mouseClicked():
    global test
    text("Mouse was clicked", 250, 250)

