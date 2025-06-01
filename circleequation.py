from math import sqrt

def drawPoint(x,y):
    Circle(200 + x*20, 200+y*20, 1)
    
for z in range(501):
    x = z/100
    print(x)
    xsquare = x * x
    ysquare = 25 - xsquare
    y1 = sqrt(ysquare)
    y2 = -1 * y1
    drawPoint(x, y1)
    drawPoint (x, y2)
    drawPoint(-1 * x, y1)
    drawPoint(-1 * x, y2)

Circle(200, 200, 98, fill='green')
