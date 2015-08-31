PerMonth = {1: 21183, 2: 18801, 3: 25388, 4: 14609}
test = False
        
def bargraph(xlimit,y,margin,h,w,dict):
    xtemp = margin
    i = 1
    for a,b in dict.items():
        rect(xtemp,y,w,-b/h)    
        xtemp += margin
        i += 1

def setup():
    size(1000,360)
    stroke(255)
    
    
def draw():
    background(0)
    test=True
#     bargraph(x,y,margin,height,width,dict) 
    bargraph(10,100,20,500,10,PerMonth)
    print "(%s,%s)"%(mouseX,mouseY)
    if mouseX>30:
        test = True
    else:
        test = False
    print test
    
    
#     rect(10,300,40,10)

def mouseClicked():
    global test
#     fill(255,0,0)
    print test
    if(test):
        fill(255,0,0)

