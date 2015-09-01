from __future__ import division
perDay = [334, 2768, 1182, 90, 1755, 778, 1911, 20, 1608, 1541, 1093, 1502, 207, 679, 780, 422, 636, 309, 358, 472, 2, 2188, 324, 202, 3142, 1213, 1097, 6, 23, 555, 1261, 622, 1281, 896, 593, 1543, 1871, 940, 2052, 1081, 403, 1, 6, 196, 166, 348, 2462, 549, 352, 481, 1471, 2336, 1786, 302, None, 2, 747, 1454, 1675, 892, 191, 1651, 1824, 1098, 639, 1314, 1346, 24, 1451, 802, 33, 504, 594, 2501, 691, 937, 1466, 896, 498, 445, 1883, 2055, 1641, 452, None, None, None, None, None, None]
perHour = [0, 333, 470, 740, 456, 3, 0, 38, 0, 13, 80, 720, 238, 1, 1, 100, 512, 11, 0, 394, 151, 4, 3, 14, 68, 0, 1, 48, 2, 1, 18, 0, 405, 227, 86, 154, 310, 494, 561, 11, 4, 0, 0, 1, 0, 114, 21, 45, 1, 0, 0, 7, 731, 589, 303, 285, 20, 627, 308, 2, 57, 9, 370, 229, 399, 316, 1, 0, 3, 16, 463, 1, 102, 231, 2, 1, 1, 15, 202, 85, 72, 123, 584, 583, 466, 378, 0, 0, 0, 8, 6, 53, 71, 0, 4, 1, 127, 223, 421, 8, 24, 230, 9, 0, 267, 269, 0, 13, 47, 3, 0, 1, 10, 226, 9, 32, 72, 182, 5, 10, 339, 15, 9, 14, 3, 3, 0, 8, 5, 31, 295, 1, 1, 0, 0, 1, 0, 0, 3, 0, 1, 3, 1, 184, 0, 3, 3, 0, 0, 0, 152, 0, 29, 1, 4, 0, 5, 252, 174, 2, 0, 5, 248, 288, 369, 688, 468, 2, 5, 9, 17, 24, 53, 6, 97, 0, 68, 3, 0, 79, 64, 11, 8, 181, 379, 1040, 338, 455, 2, 83, 259, 51, 392, 113, 17, 2, 1, 1, 24, 445, 469, 51, 0, 58, 4, 1, 43, 0, 16, 87, 282, 1, 0, 1, 0, 31, 0, 268, 254, 109, 116, 24, 4, 0, 0, 14, 0, 2, 4, 10, 4, 3, 1, 1, 531, 314, 0, 3, 6, 36, 119, 0, 0, 156, 220, 32, 342, 3, 17, 3, 8, 13, 2, 0, 0, 0, 1, 337, 116, 129, 0, 1, 0, 0, 6, 25, 189, 324, 407, 1, 21, 46, 121, 61, 68, 562, 333, 1, 2, 27, 1, 6, 20, 109, 420, 134, 8, 4, 9, 212, 9, 18, 15, 106, 141, 33, 79, 438, 1, 173, 148, 377, 481, 187, 6, 1, 93, 4, 10, 8, 111, 6, 75, 434, 65, 465, 319, 0, 1, 1, 2, 1, 3, 5, 1, 7, 12, 101, 9, 313, 321, 0, 5, 431, 334, 310, 1, 0, 6, 0, 6, 3, 9, 46, 103, 140, 7, 118, 307, 239, 38, 6, 80, 16, 57, 0, 2, 184, 0, 0, 21, 5, 7, 4, 1, 4, 19, 177, 2, 0, 161, 6, 1, 4, 1, 6, 0, 1, 10, 6, 5, 167, 1, 124, 14, 16, 5, 3, 3, 1, 0, 0, 140, 0, 116, 56, 24, 98, 552, 524, 498, 53, 6, 5, 374, 97, 77, 35, 72, 59, 1, 8, 104, 15, 42, 8, 96, 114, 148, 4, 1, 1, 1, 1, 11, 5, 5, 320, 95, 138, 117, 0, 54, 1, 58, 1, 9, 2, 3, 0, 3, 360, 536, 42, 72, 87, 50, 3, 302, 582, 573, 516, 317, 0, 275, 29, 28, 1, 1, 4, 184, 542, 552, 445, 1, 0, 0, 0, 1, 0, 45, 5, 76, 1, 4, 61, 17, 0, 77, 0, 0, 21, 34, 0, 0, 2, 254, 57, 2, 2, 99, 70, 257, 509, 484, 393, 1, 2, 30, 29, 320, 370, 390, 93, 0, 5, 289, 0, 2, 18, 119, 28, 8, 0, 7, 11, 73, 1, 164, 111, 210, 0, 296, 1, 1, 1, 2, 0, 20, 0, 0, 11, 62, 7, 1, 1, 5, 0, 20, 74, 74, 16, 359, 450, 22, 0, 90, 3, 46, 1, 8, 27, 24, 69, 43, 79, 1, 322, 448, 575, 372, 6, 99, 0, 22, 124, 5, 4, 1, 0, 156, 233, 22, 94, 377, 0, 3, 170, 0, 32, 7, 4, 1, 52, 84, 0, 3, 0, 0, 0, 32, 191, 5, 0, 11, 10, 2, 379, 350, 487, 352, 4, 58, 51, 1, 4, 1, 2, 33, 176, 0, 32, 454, 61, 52, 265, 5, 0, 24, 17, 210, 4, 3, 10, 0, 0, 0, 1, 43, 12, 0, 6, 14, 243, 75, 159, 0, 49, 396, 443, 243, 1, 0, 78, 20, 94, 7, 152, 22, 52, 66, 49, 6, 0, 0, 9, 0, 7, 1, 10, 4, 0, 29, 19, 3, 0, 104, 121, 216, 61, 0, 145, 12, 1, 1, 0, 62, 304, 472, 463, 452, 175, 74, 264, 145, 75, 32, 5, 314, 16, 2, 0, 391, 248, 1, 0, 0, 2, 3, 38, 4, 0, 29, 31, 21, 0, 0, 82, 218, 22, 188, 205, 0, 124, 3, 0, 0, 2, 3, 1, 1, 3, 64, 275, 444, 322, 325, 9, 0, 3, 0, 99, 167, 52, 340, 110, 8, 51, 51, 0, 4, 0, 0, 36, 0, 25, 5, 36, 40, 67, 1, 1, 130, 132, 4, 7, 0, 47, 1, 161, 3, 17, 47, 0, 0, 160, 13, 0, 0, 121, 150, 112, 240, 95, 457, 11, 159, 514, 324, 320, 401, 397, 111, 2, 2, 1, 66, 1, 2, 0, 0, 4, 25, 0, 125, 227, 29, 201, 307, 260, 286, 3, 115, 220, 80, 2, 15, 64, 77, 259, 191, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
perMonthList = [21184, 18801, 25388, 14609, None, None, None, None, None, None, None, None]

i = 1
ylimit = 100
test = False
j = 1
barcount = 0
newbar = {}
#bar object for the box
class bar(object):
    #__metaclass++ = IterRegistry
    x0 = 0
    x1 = 0
    y0 = 0
    y1 = 0
    
    def __iter__(self):
        for user in dir(bar):
            if not user.startswith("__"):
                yield user    
                

def bargraphList(x, y, height, width, hfactor, barwidth,tsize, list):
    global barcount
    global newbar
    i = 1
    maxv = 1
    xval = 0
    listLan = 0
    yval = 0
    i=0
    start = True

    for b in list:
        if y > maxv:
            maxv = b
        if b is not None:
            listLan += 1
    xUnit = width / listLan
    yUnit = height / (maxv * hfactor)
    for val in list:
        if val is not None:
            xval += xUnit
            if start:
                xval = 10
                start = False
            yval = val * yUnit
            newbar[barcount] = bar()
            newbar[barcount].x0=xval+x
            newbar[barcount].y0=y
            newbar[barcount].x1=xval+x+(xUnit/barwidth)
            newbar[barcount].y1=-yval+y
            rect(xval + x, y, xUnit / barwidth, -yval)
            line(x,y,x+(xUnit*listLan)+10,y)
            textSize(tsize)
            fill(12,11,8)
            text(val,xval+x-10,y-yval-5)
#             text(" ldown",newbar[barcount].x0,newbar[barcount].y0)
#             text(" rup",newbar[barcount].x1,newbar[barcount].y1)
#             text("up",xval+x+(xUnit/barwidth),-yval+y)
            fill(255,165,0)
            barcount +=1

        

def setup():
    size(1480, 720)
    stroke(0)

def draw():
    background(230,228,224)
#     bargraph(x, y, height, width, hfactor,barwidth, list)
    bargraphList(100, 700, 720 , 1280, 7, 3, 8, perHour)
    fill(255,165,0)
    bargraphList(100, 330, 720, 1280, 3, 4, 14, perMonthList)
    fill(145,96,6)
    bargraphList(100, 500, 720 , 1280, 7, 3, 12, perDay)
    noLoop()



def mouseClicked():
    global test
    j = 0
    x = mouseX
    y = mouseY
    print barcount
#     while(j<barcount):
#         print newbar[j].x0
#         print newbar[j].x1
#         print newbar[j].y0
#         print newbar[j].y1
#         text("onclick!!",newbar[j].x0,newbar[j].y0)
#         text("onclick!!",newbar[j].x1,newbar[j].y1)
#         text("up",newbar[j].x0,newbar[j].y0)
#         text("down",newbar[j].x1,newbar[j].y1)
#         if x > newbar[j].x0 and x < newbar[j].x1 and y > newbar[j].y0 and  y < newbar[j].y1:
#             print "it worked bitch :P"
#             text("here",mouseX,mouseY)
#             fill(0, 102, 153, 51)
#         j += 1
    
