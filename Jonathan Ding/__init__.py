
import ccircle
import random
window=ccircle.Window("Let's just get it working!")

bigger=True
wutwut=True
size=50
color=50
dotY=[0,-100,-240,-150,-70,-90,-210,
      -110,-40,-50,-69,-508,-57,-954,-195]
#dotX=[random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),
#      random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),
#      random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),random.getint(0,1000),random.getint(0,1000)]
dotX=[593,105,729,345,645,893,294,
      169,671,716,201,801,395,487,58]
while window.isOpen():
    length,height=window.getSize()
    window.clear(0.01*color, 0.01*color, 0.02*color)
    mouseX,mouseY=window.getMousePos()
    window.hideMouse()
    window.drawCircle(mouseX, mouseY, 100, 0.5, 1, 0.5)
    #for i in range(1,40):
    #   window.drawLine(mouseX-100+i*5,mouseY-120,mouseX-100+i*5,mouseY-60,0,0,0)
    if ccircle.isMouseDown('left')==True:
        window.drawCircle(mouseX, mouseY + 30, size/1.2, 0, 0, 0)
    else:
        window.drawCircle(mouseX, mouseY + 20, size, 0, 0, 0)
        window.drawCircle(mouseX, mouseY, size, 0.5, 1, 0.5)
    window.drawCircle(mouseX - 40, mouseY - 20, 16, 1, 1, 1)
    window.drawCircle(mouseX + 40, mouseY - 20, 16, 1, 1, 1)
    window.drawCircle(mouseX - 40, mouseY - 20, size/5+2, 0, 0, 0)
    window.drawCircle(mouseX + 40, mouseY - 20, size/5+2, 0, 0, 0)
    if bigger==True:
        size+=0.003
        if size>=52:
            bigger=False
    if bigger==False:
        size-=0.003
        if size<=48:
            bigger=True
    if wutwut==True:
        color+=0.03
        if color>=100:
            wutwut=False
    if wutwut==False:
        color-=0.03
        if color<=0:
            wutwut=True
    for i in range(0,15):
        dotY[i]+=1
        if dotY[i] >=height:
            dotY[i]=0
        window.drawCircle(dotX[i],dotY[i],10,1,1,1)
    window.update()