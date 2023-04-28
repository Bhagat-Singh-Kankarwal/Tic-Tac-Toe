from graphics import *
import time
import random

# import winsound
def close():
    bg = Rectangle(Point(-1, 501), Point(501, -1))
    bg.setFill("white")
    bg.setOutline("white")
    bg.move(0, 500)
    bg.draw(win)

    for i in range(50):
        cimg.move(0, -10)
        bg.move(0, -10)
        time.sleep(0.002)

    cimg.undraw()

    time.sleep(0.2)

    cir = Circle(Point(250,-120), 110)
    cir.setFill("black")
    cir.draw(win)

    txt1 = Text(Point(250, -95), "Developed by ")
    txt1.setTextColor("black")
    txt1.setFace("SNES")
    txt1.setSize(30)
    txt1.draw(win)    

    txt = Text(Point(65, 250), "Bhagat Singh Kankarwal")
    txt.setTextColor("white")
    txt.setFace("SNES")
    txt.setSize(25)
    txt.draw(win)

    line = Line(Point(180, -65), Point(315, -65))
    line.setWidth(2)
    line.draw(win)

    for i in range(37):
        cir.move(0, 10)
        txt.move(5, 0)
        txt1.move(0, 5)
        line.move(0, 5)
        time.sleep(0.01)

    time.sleep(0.8)



    for i in range(3):
        cir = Circle(Point(250, 250), 110)
        cir.setFill("white")
        cir.setOutline("white")
        cir.draw(win)

        txt = Text(Point(250, 250), "Bhagat Singh Kankarwal")
        txt.setTextColor("black")
        txt.setFace("SNES")
        txt.setSize(25)
        txt.draw(win)

        time.sleep(0.2)

        cir = Circle(Point(250, 250), 110)
        cir.setFill("black")
        cir.setOutline("black")
        cir.draw(win)

        txt = Text(Point(250, 250), "Bhagat Singh Kankarwal")
        txt.setTextColor("white")
        txt.setFace("SNES")
        txt.setSize(25)
        txt.draw(win)

        time.sleep(0.2)

    time.sleep(1.7)
# ----------------------------------------------------------------------------#

def check_X() :
    global streak
    streak = [0,1,2]
    
    global flag
    
    if lst[0:3] == ['X']*3 or lst[0:7:3] == ['X']*3 or lst[0:9:4] == ['X']*3 \
    or lst[2:7:2] == ['X']*3 or lst[2:9:3] == ['X']*3 or lst[6:9] == ['X']*3 \
    or lst[1:8:3] == ['X']*3 or lst[3:6] == ['X']*3:

        flag = 1

        if lst[0:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:7:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:9:4] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:7:2] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350 - i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:9:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[6:9] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 350), "X.png")
                ximg.draw(win)
            
        elif lst[1:8:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(250, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[3:6] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 250), "X.png")
                ximg.draw(win)

        text = Text(Point(250, 450), "{} wins".format(A1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)
        

    elif lst[0:3] == ['O']*3 or lst[0:7:3] == ['O']*3 or lst[0:9:4] == ['O']*3 \
    or lst[2:7:2] == ['O']*3 or lst[2:9:3] == ['O']*3 or lst[6:9] == ['O']*3 \
    or lst[1:8:3] == ['O']*3 or lst[3:6] == ['O']*3:

        flag = 1

        if lst[0:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:7:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:9:4] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:7:2] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350 - i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:9:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[6:9] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 350), "O.png")
                oimg.draw(win)
            
        elif lst[1:8:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(250, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[3:6] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 250), "O.png")
                oimg.draw(win)
        
        text = Text(Point(250, 450), "{} wins".format(B1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)

def check_O() :
    global streak
    streak = [0,1,2]
    
    global flag
    
    if lst[0:3] == ['O']*3 or lst[0:7:3] == ['O']*3 or lst[0:9:4] == ['O']*3 \
    or lst[2:7:2] == ['O']*3 or lst[2:9:3] == ['O']*3 or lst[6:9] == ['O']*3 \
    or lst[1:8:3] == ['O']*3 or lst[3:6] == ['O']*3:

        flag = 1

        if lst[0:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:7:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:9:4] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:7:2] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350 - i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:9:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[6:9] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 350), "O.png")
                oimg.draw(win)
            
        elif lst[1:8:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(250, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[3:6] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 250), "O.png")
                oimg.draw(win)
        
        text = Text(Point(250, 450), "{} wins".format(B1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)

    elif lst[0:3] == ['X']*3 or lst[0:7:3] == ['X']*3 or lst[0:9:4] == ['X']*3 \
    or lst[2:7:2] == ['X']*3 or lst[2:9:3] == ['X']*3 or lst[6:9] == ['X']*3 \
    or lst[1:8:3] == ['X']*3 or lst[3:6] == ['X']*3:

        flag = 1

        if lst[0:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:7:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:9:4] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:7:2] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350 - i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:9:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[6:9] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 350), "X.png")
                ximg.draw(win)
            
        elif lst[1:8:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(250, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[3:6] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 250), "X.png")
                ximg.draw(win)

        text = Text(Point(250, 450), "{} wins".format(A1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)

def check_for_X() :
    global streak
    streak = [0,1,2]
    
    global flag
    
    if lst[0:3] == ['X']*3 or lst[0:7:3] == ['X']*3 or lst[0:9:4] == ['X']*3 \
    or lst[2:7:2] == ['X']*3 or lst[2:9:3] == ['X']*3 or lst[6:9] == ['X']*3 \
    or lst[1:8:3] == ['X']*3 or lst[3:6] == ['X']*3:

        flag = 1

        if lst[0:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:7:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:9:4] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:7:2] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350 - i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:9:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[6:9] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 350), "X.png")
                ximg.draw(win)
            
        elif lst[1:8:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(250, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[3:6] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 250), "X.png")
                ximg.draw(win)

        text = Text(Point(250, 450), "{} wins".format(A1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)
        

    elif lst[0:3] == ['O']*3 or lst[0:7:3] == ['O']*3 or lst[0:9:4] == ['O']*3 \
    or lst[2:7:2] == ['O']*3 or lst[2:9:3] == ['O']*3 or lst[6:9] == ['O']*3 \
    or lst[1:8:3] == ['O']*3 or lst[3:6] == ['O']*3:

        flag = 1

        if lst[0:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:7:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:9:4] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:7:2] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350 - i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:9:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[6:9] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 350), "O.png")
                oimg.draw(win)
            
        elif lst[1:8:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(250, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[3:6] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 250), "O.png")
                oimg.draw(win)
        
        text = Text(Point(250, 450), "{} wins".format(B1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)

def check_for_O() :
    global streak
    streak = [0,1,2]
    
    global flag
    
    if lst[0:3] == ['O']*3 or lst[0:7:3] == ['O']*3 or lst[0:9:4] == ['O']*3 \
    or lst[2:7:2] == ['O']*3 or lst[2:9:3] == ['O']*3 or lst[6:9] == ['O']*3 \
    or lst[1:8:3] == ['O']*3 or lst[3:6] == ['O']*3:

        flag = 1

        if lst[0:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:7:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[0:9:4] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:7:2] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350 - i*100, 150 + i*100), "O.png")
                oimg.draw(win)
            
        elif lst[2:9:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(350, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[6:9] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 350), "O.png")
                oimg.draw(win)
            
        elif lst[1:8:3] == ['O']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(250, i*100 + 150), "O.png")
                oimg.draw(win)
            
        elif lst[3:6] == ['O']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_O.png")
                wimg.draw(win)
                oimg = Image(Point(150 + i*100, 250), "O.png")
                oimg.draw(win)
        
        text = Text(Point(250, 450), "{} wins".format(A1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)

    elif lst[0:3] == ['X']*3 or lst[0:7:3] == ['X']*3 or lst[0:9:4] == ['X']*3 \
    or lst[2:7:2] == ['X']*3 or lst[2:9:3] == ['X']*3 or lst[6:9] == ['X']*3 \
    or lst[1:8:3] == ['X']*3 or lst[3:6] == ['X']*3:

        flag = 1

        if lst[0:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:7:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[0:9:4] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:7:2] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350 - i*100, 150 + i*100), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350 - i*100, 150 + i*100), "X.png")
                ximg.draw(win)
            
        elif lst[2:9:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(350, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(350, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[6:9] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 350), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 350), "X.png")
                ximg.draw(win)
            
        elif lst[1:8:3] == ['X']*3:

            for i in streak:
                wimg = Image(Point(250, i*100 + 150), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(250, i*100 + 150), "X.png")
                ximg.draw(win)
            
        elif lst[3:6] == ['X']*3:

            for i in streak:
                wimg = Image(Point(150 + i*100, 250), "bg_X.png")
                wimg.draw(win)
                ximg = Image(Point(150 + i*100, 250), "X.png")
                ximg.draw(win)

        text = Text(Point(250, 450), "{} wins".format(B1))
        text.setFace('Black And White Display')
        text.setTextColor(color_rgb(70, 71, 58))
        text.setSize(20)
        text.draw(win)

        

# placing letters
def letters_for_X():
            
    if a == 0:
        img = Image(Point(150, 150), "{}.png".format(B))
        img.draw(win)

    elif a == 1:
        img = Image(Point(250, 150), "{}.png".format(B))
        img.draw(win)
                    
    elif a == 2:
        img = Image(Point(350, 150), "{}.png".format(B))
        img.draw(win)

    elif a == 3:
        img = Image(Point(150, 250), "{}.png".format(B))
        img.draw(win)

    elif a == 4:
        img = Image(Point(250, 250), "{}.png".format(B))
        img.draw(win)

    elif a == 5:
        img = Image(Point(350, 250), "{}.png".format(B))
        img.draw(win)

    elif a == 6:
        img = Image(Point(150, 350), "{}.png".format(B))
        img.draw(win)

    elif a == 7:
        img = Image(Point(250, 350), "{}.png".format(B))
        img.draw(win)

    elif a == 8:
        img = Image(Point(350, 350), "{}.png".format(B))
        img.draw(win)

    else:
        pass

def letters_for_O():

    if a == 0:
        img = Image(Point(150, 150), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 1:
        img = Image(Point(250, 150), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 2:
        img = Image(Point(350, 150), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 3:
        img = Image(Point(150, 250), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 4:
        img = Image(Point(250, 250), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 5:
        img = Image(Point(350, 250), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 6:
        img = Image(Point(150, 350), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 7:
        img = Image(Point(250, 350), "{}.png".format(lst2[0]))
        img.draw(win)

    elif a == 8:
        img = Image(Point(350, 350), "{}.png".format(lst2[0]))
        img.draw(win)

    else:
        pass

# ML
def ai_for_X():
    global a
    
    if A == 'X':
    # for player = X
        if lst.count('X') == 0:
            get = 0
            if get in (0,2,6,8):
                avail = [0,2,6,8]
                avail.remove(get)
                place = random.choice(avail)
                lst[place] = 'O'
                a = place
                #letters_for_X()
                
        elif lst.count('X') == 1:
            get = lst.index('X')
            if get in (0,2,6,8):
                avail = [0,2,6,8]
                avail.remove(get)
                place = random.choice(avail)
                lst[place] = 'O'
                a = place
                #letters_for_X()
            else:
                lst[8]='O'
                a = 8
                #letters_for_X()
                
               
        elif lst.count('X')>=2:
            if lst[0:3]==['O','-','O']:
                lst[1],a='O',1
            elif lst[0:3]==['O','O','-']:
                lst[2],a='O',2
            elif lst[0:3]==['-','O','O']:
                lst[0],a='O',0
            elif lst[1:8:3]==['O','-','O']:
                lst[4],a='O',4
            elif lst[1:8:3]==['-','O','O']:
                lst[1],a='O',1
            elif lst[1:8:3]==['O','O','-']:
                lst[7],a='O',7
            elif lst[6:9]==['O','-','O']:
                lst[7],a='O',7
            elif lst[6:9]==['O','O','-']:
                lst[8],a='O',8
            elif lst[6:9]==['-','O','O']:
                lst[6],a='O',6
            elif lst[2:9:3]==['O','-','O']:
                lst[5],a='O',5
            elif lst[2:9:3]==['O','O','-']:
                lst[8],a='O',8
            elif lst[2:9:3]==['-','O','O']:
                lst[2],a='O',2
            elif lst[0:7:3]==['O','-','O']:
                lst[3],a='O',3
            elif lst[0:7:3]==['O','O','-']:
                lst[6],a='O',6
            elif lst[0:7:3]==['-','O','O']:
                lst[0],a='O',0
            elif lst[0:9:4]==['O','-','O']:
                lst[4],a='O',4
            elif lst[0:9:4]==['O','O','-']:
                lst[8],a='O',8
            elif lst[0:9:4]==['-','O','O']:
                lst[0],a='O',0
            elif lst[2:7:2]==['O','-','O']:
                lst[4],a='O',4
            elif lst[2:7:2]==['O','O','-']:
                lst[6],a='O',6
            elif lst[2:7:2]==['-','O','O']:
                lst[2],a='O',2
            elif lst[3:6]==['O','-','O']:
                lst[4],a='O',4
            elif lst[3:6]==['-','O','O']:
                lst[3],a='O',3
            elif lst[3:6]==['O','O','-']:
                lst[5],a='O',5
            elif lst[0:3]==['X','-','X']:
                lst[1],a='O',1
            elif lst[0:3]==['X','X','-']:
                lst[2],a='O',2
            elif lst[0:3]==['-','X','X']:
                lst[0],a='O',0
            elif lst[2:7:2]==['X','X','-']:
                lst[6],a='O',6
            elif lst[2:7:2]==['-','X','X']:
                lst[2],a='O',2
            elif lst[2:7:2]==['X','-','X']:
                lst[4],a='O',4
            elif lst[1:8:3]==['X','-','X']:
                lst[4],a='O',4
            elif lst[1:8:3]==['-','X','X']:
                lst[1],a='O',1
            elif lst[1:8:3]==['X','X','-']:
                lst[7],a='O',7
            elif lst[6:9]==['X','-','X']:
                lst[7],a='O',7
            elif lst[6:9]==['X','X','-']:
                lst[8],a='O',8
            elif lst[6:9]==['-','X','X']:
                lst[6],a='O',6
            elif lst[2:9:3]==['X','-','X']:
                lst[5],a='O',5
            elif lst[2:9:3]==['X','X','-']:
                lst[8],a='O',8
            elif lst[2:9:3]==['-','X','X']:
                lst[2],a='O',2
            elif lst[0:7:3]==['X','-','X']:
                lst[3],a='O',3
            elif lst[0:7:3]==['X','X','-']:
                lst[6],a='O',6
            elif lst[0:7:3]==['-','X','X']:
                lst[0],a='O',0
            elif lst[0:9:4]==['X','-','X']:
                lst[4],a='O',4
            elif lst[0:9:4]==['X','X','-']:
                lst[8],a='O',8
            elif lst[0:9:4]==['-','X','X']:
                lst[0],a='O',0
            elif lst[3:6]==['X','-','X']:
                lst[4],a='O',4
            elif lst[3:6]==['-','X','X']:
                lst[3],a='O',3
            elif lst[3:6]==['X','X','-']:
                lst[5],a='O',5
            elif lst[0]=='-':
                lst[0], a = 'O', 0
            elif lst[2] == '-':
                lst[2], a = 'O', 2
            elif lst[6] == '-':
                lst[6], a = 'O', 6
            elif lst[8] == '-':
                lst[8], a = 'O', 8
            else:
                for i in range(len(lst)):
                    if lst[i]=='-':
                        lst[i]='O'
                        a = i
                        break
                    
        check_for_X()

        if flag == 1:
            pass
        
        else:
            check_for_O()
            letters_for_X()
        
            
         
def ai_for_O():
    global a    
    #for player = O
    if lst1[0] == 'O':
        if lst.count('O') == 0:
            get = 0
            if get in (0,2,6,8):
                avail = [0,2,6,8]
                avail.remove(get)
                place = random.choice(avail)
                lst[place] = 'X'
                a = place
                #letters_for_O()
        
        elif lst.count('O')==1:
            get=lst.index('O')
            if get in (0,2,6,8):
                avail=[0,2,6,8]
                avail.remove(get)
                place=random.choice(avail)
                lst[place] = 'X'
                a = place
                #letters_for_O()
                
            else:
                lst[8] = 'X'
                a = 8
                #letters_for_O()
                
                
        elif lst.count('O')>=2:
            if lst[0:3]==['X','-','X']:
                lst[1],a='X',1
            elif lst[0:3]==['X','X','-']:
                lst[2],a='X',2
            elif lst[0:3]==['-','X','X']:
                lst[0],a='X',0
            elif lst[2:7:2]==['X','X','-']:
                lst[6],a='X',6
            elif lst[2:7:2]==['-','X','X']:
                lst[2],a='X',2
            elif lst[2:7:2]==['X','-','X']:
                lst[4],a='X',4
            elif lst[1:8:3]==['X','-','X']:
                lst[4],a='X',4
            elif lst[1:8:3]==['-','X','X']:
                lst[1],a='X',1
            elif lst[1:8:3]==['X','X','-']:
                lst[7],a='X',7
            elif lst[6:9]==['X','-','X']:
                lst[7],a='X',7
            elif lst[6:9]==['X','X','-']:
                lst[8],a='X',8
            elif lst[6:9]==['-','X','X']:
                lst[6],a='X',6
            elif lst[2:9:3]==['X','-','X']:
                lst[5],a='X',5
            elif lst[2:9:3]==['X','X','-']:
                lst[8],a='X',8
            elif lst[2:9:3]==['-','X','X']:
                lst[2],a='X',2
            elif lst[0:7:3]==['X','-','X']:
                lst[3],a='X',3
            elif lst[0:7:3]==['X','X','-']:
                lst[6],a='X',6
            elif lst[0:7:3]==['-','X','X']:
                lst[0],a='X',0
            elif lst[0:9:4]==['X','-','X']:
                lst[4],a='X',4
            elif lst[0:9:4]==['X','X','-']:
                lst[8],a='X',8
            elif lst[0:9:4]==['-','X','X']:
                lst[0],a='X',0
            elif lst[3:6]==['X','-','X']:
                lst[4],a='X',4
            elif lst[3:6]==['-','X','X']:
                lst[3],a='X',3
            elif lst[3:6]==['X','X','-']:
                lst[5],a='X',5
            elif lst[0:3]==['O','-','O']:
                lst[1],a='X',1
            elif lst[0:3]==['O','O','-']:
                lst[2],a='X',2
            elif lst[0:3]==['-','O','O']:
                lst[0],a='X',0
            elif lst[2:7:2]==['O','O','-']:
                lst[6],a='X',6
            elif lst[2:7:2]==['-','O','O']:
                lst[2],a='X',2
            elif lst[2:7:2]==['O','-','O']:
                lst[4],a='X',4
            elif lst[1:8:3]==['O','-','O']:
                lst[4],a='X',4
            elif lst[1:8:3]==['-','O','O']:
                lst[1],a='X',1
            elif lst[1:8:3]==['O','O','-']:
                lst[7],a='X',7
            elif lst[6:9]==['O','-','O']:
                lst[7],a='X',7
            elif lst[6:9]==['O','O','-']:
                lst[8],a='X',8
            elif lst[6:9]==['-','O','O']:
                lst[6],a='X',6
            elif lst[2:9:3]==['O','-','O']:
                lst[5],a='X',5
            elif lst[2:9:3]==['O','O','-']:
                lst[8],a='X',8
            elif lst[2:9:3]==['-','O','O']:
                lst[2],a='X',2
            elif lst[0:7:3]==['O','-','O']:
                lst[3],a='X',3
            elif lst[0:7:3]==['O','O','-']:
                lst[6],a='X',6
            elif lst[0:7:3]==['-','O','O']:
                lst[0],a='X',0
            elif lst[0:9:4]==['O','-','O']:
                lst[4],a='X',4
            elif lst[0:9:4]==['O','O','-']:
                lst[8],a='X',8
            elif lst[0:9:4]==['-','O','O']:
                lst[0],a='X',0
            elif lst[3:6]==['O','-','O']:
                lst[4],a='X',4
            elif lst[3:6]==['-','O','O']:
                lst[3],a='X',3
            elif lst[3:6]==['O','O','-']:
                lst[5],a='X',5
            elif lst[0]=='-':
                lst[0],a='X',0
            elif lst[2]=='-':
                lst[2],a='X',2
            elif lst[6]=='-':
                lst[6],a='X',6
            elif lst[8]=='-':
                lst[8],a='X',8
            else:
                for i in range(len(lst)):
                    if lst[i]=='-':
                        lst[i],a='X',i
                       
                        break                    
            
        
        check_for_O()

        if flag == 1:
            pass
        
        else:
            check_for_X()
            letters_for_O()
# ------------------------------------------------------------------#


def computer():
    global cimg
    
    cimg = Image(Point(250, 250), "back.png")
    cimg.draw(win)

    global A

    global B

    
    # enter player name
    inputBox = Text(Point(250, 180), "ENTER PLAYER NAME")
    inputBox.setTextColor(color_rgb(70, 71, 58))
    inputBox.setFace("Bahnschrift SemiLight Condensed")
    inputBox.setSize(25)
    inputBox.draw(win)

    # name entry

    inputName = Entry(Point(250, 250), 6)
    inputName.setTextColor(color_rgb(70, 71, 58))

    inputName.setText("Player")

    inputName.setFace("Azonix")
    inputName.setSize(20)
    inputName.setFill(color_rgb(235, 255, 255))
    inputName.draw(win)


    # exit sentence
    ext = Text(Point(250, 450), "Click anywhere to continue\nMaximum length of name is 6")
    ext.setSize(10)
    ext.draw(win)

    win.getMouse()

    global A1
    A1 = inputName.getText()

    global B1
    B1 = "A.I."

    if len(A1) > 6:
        A1 = A1[:6]
    
    inputName.undraw()

    pointer = Text(Point(250, 250), A1)
    pointer.setFace("Azonix")
    pointer.setSize(20)
    pointer.setTextColor(color_rgb(70, 71, 58))
    pointer.draw(win)

    
    for i in range(15):
        ext.move(0, 5)
        time.sleep(0.001)

    ext.undraw()

    time.sleep(0.2)
    
    opt1 = Rectangle(Point(110, 440), Point(160, 390))
    opt2 = Rectangle(Point(390, 440), Point(340, 390))
    
    opt1.setOutline(color_rgb(70, 71, 58))
    opt1.setWidth(3)
    opt2.setOutline(color_rgb(70, 71, 58))
    opt2.setWidth(3)

    opt1.move(50, -40)
    opt2.move(-50, -40)
    
    opt1.draw(win)
    opt2.draw(win)

    opt11 = Text(Point(135, 415), "X")
    opt22 = Text(Point(365, 415), "O")

    opt11.move(50, -40)
    opt22.move(-50, -40)
    
    opt11.setSize(30)
    opt22.setSize(30)
    opt11.setFace("Azonix")
    opt22.setFace("Azonix")
    opt11.setTextColor(color_rgb(70, 71, 58))
    opt22.setTextColor(color_rgb(70, 71, 58))

    opt1.move(-200, 0)
    opt11.move(-200, 0)
    opt2.move(200, 0)
    opt22.move(200, 0)

    opt11.draw(win)
    opt22.draw(win)
    
    for i in range(40):
        opt1.move(5, 0)
        opt2.move(-5, 0)
        opt11.move(5,0)
        opt22.move(-5,0)
        time.sleep(0.001)

    pointer2 = Text(Point(380, -44), B1)
    pointer2.setFace("Azonix")
    pointer2.setSize(20)
    pointer2.setTextColor(color_rgb(70, 71, 58))
    pointer2.draw(win)

    ch = True
    while ch is True:
        chk = win.getMouse()
        if 162 <= int(chk.getX()) <= 208 and 353 <= int(chk.getY()) <= 397:
                    
            opt1.setFill(color_rgb(23, 162, 27))
            opt11.setTextColor('white')

            time.sleep(0.2)
            
            opt1.setFill('white')
            opt11.setFill(color_rgb(70, 71, 58))
            ch = False

            
            A = 'X'
            B = 'O'
            
            for i in range(21):
                pointer.move(-8, -10)
                opt1.move(0, -16)
                opt11.move(0, -16)
                pointer2.move(0, 4)

                opt2.move(6.19, -16.04)
                opt22.move(6.19, -16.04)

                inputBox.move(0, 17)
                time.sleep(0.009)

            opt2.setFill('white')
            inputBox.undraw()
            
        elif 292 <= int(chk.getX()) <= 352 and 339 <= int(chk.getY()) <= 399:
            
            opt2.setFill(color_rgb(23, 162, 27))
            opt22.setTextColor('white')

            time.sleep(0.2)
            
            opt2.setFill('white')
            opt22.setFill(color_rgb(70, 71, 58))
            ch = False

            global lst1
            lst1 = ["O"]

            global lst2
            lst2 = ['X']

            try: 
                del A
                del B
                
            except:
                pass
            
            for i in range(21):
                pointer.move(-8, -10)
                opt2.move(-6.3, -16)
                opt22.move(-6.3, -16)
                pointer2.move(0, 4)

                opt1.move(11.9, -16.04)
                opt11.move(11.9, -16.04)

                inputBox.move(0, 17)
                time.sleep(0.009)
                
            opt1.setFill('white')
            inputBox.undraw()


        else:
            pass
# -----------------------------------------------------------------------#

def player():
    global cimg
    cimg = Image(Point(250, 250), "back.png")
    cimg.draw(win)

    global A

    global B
    
    # enter player name 1
    inputBox1 = Text(Point(250, 80), "ENTER PLAYER NAME")
    inputBox1.setTextColor(color_rgb(70, 71, 58))
    inputBox1.setFace("Bahnschrift SemiLight Condensed")
    inputBox1.setSize(22)
    inputBox1.draw(win)

    # name entry 1
    inputName1 = Entry(Point(250, 150), 8)
    inputName1.setTextColor(color_rgb(70, 71, 58))

    inputName1.setText("Player 1")

    inputName1.setFace("Azonix")
    inputName1.setSize(17)
    inputName1.setFill(color_rgb(235, 255, 255))
    inputName1.draw(win)

    # enter player name 2
    inputBox2 = Text(Point(250, 280), "ENTER PLAYER NAME")
    inputBox2.setTextColor(color_rgb(70, 71, 58))
    inputBox2.setFace("Bahnschrift SemiLight Condensed")
    inputBox2.setSize(22)
    inputBox2.draw(win)

    # name entry 2
    inputName2 = Entry(Point(250, 350), 8)
    inputName2.setTextColor(color_rgb(70, 71, 58))

    inputName2.setText("Player 2")

    inputName2.setFace("Azonix")
    inputName2.setSize(17)
    inputName2.setFill(color_rgb(255, 236, 176))
    inputName2.draw(win)


    # exit sentence
    ext = Text(Point(250, 450), "Click anywhere to continue\nMaximum length of name is 8")
    ext.setSize(10)
    ext.draw(win)

    # chaOS
    opt1 = Rectangle(Point(360, 175), Point(410, 125))
    opt2 = Rectangle(Point(410, 375), Point(360, 325))
    
    opt1.setOutline(color_rgb(70, 71, 58))
    opt1.setWidth(3)
    opt2.setOutline(color_rgb(70, 71, 58))
    opt2.setWidth(3)
    
    opt1.draw(win)
    opt2.draw(win)

    opt11 = Text(Point(385, 150), "X")
    opt22 = Text(Point(385, 350), "O")

    
    opt11.setSize(30)
    opt22.setSize(30)
    opt11.setFace("Azonix")
    opt22.setFace("Azonix")
    opt11.setTextColor(color_rgb(70, 71, 58))
    opt22.setTextColor(color_rgb(70, 71, 58))

    opt11.draw(win)
    opt22.draw(win)

    
    win.getMouse()

    global A1
    A1 = inputName1.getText()

    global B1
    B1 = inputName2.getText()

    if len(A1) > 8:
        A1 = A1[:8]
    if len(B1) > 8:
        B1 = B1[:8]

    
    inputName1.undraw()
    inputName2.undraw()

    pointer1 = Text(Point(250, 150), A1)
    pointer1.setFace("Azonix")
    pointer1.setSize(17)
    pointer1.setTextColor(color_rgb(70, 71, 58))
    pointer1.draw(win)

    pointer2 = Text(Point(250, 350), B1)
    pointer2.setFace("Azonix")
    pointer2.setSize(17)
    pointer2.setTextColor(color_rgb(70, 71, 58))
    pointer2.draw(win)

    opt1.setFill(color_rgb(23, 162, 27))
    opt11.setTextColor('white')
    opt2.setFill(color_rgb(23, 162, 27))
    opt22.setTextColor('white')

    time.sleep(0.2)

    opt1.setFill('white')
    opt11.setFill(color_rgb(70, 71, 58))
    opt2.setFill('white')
    opt22.setFill(color_rgb(70, 71, 58))
    
    for i in range(50):
        inputBox1.move(-8, 0)
        inputBox2.move(8, 0)
        ext.move(0, 5)
        time.sleep(0.001)

    ext.undraw()
    inputBox1.undraw()
    inputBox2.undraw()

    time.sleep(0.2)

    for i in range(21):
        pointer1.move(-7.61, -5.23)
        opt1.move(-9.42, -5.23)
        opt11.move(-9.42, -5.23)
        
        pointer2.move(4.76, -14.76)
        opt2.move(2.85, -14.76)
        opt22.move(2.85, -14.76)

        inputBox1.move(0, 17)
        inputBox2.move(0, 17)
        time.sleep(0.004)

    A = 'X'
    B = 'O'

# ------------------------------------------------------------------------#

def X():
    click1 = win.getMouse()
    
    if 100 <= click1.getX() <= 200 and 100 <= click1.getY() <= 200:

        if lst[0] != '-':
            print("Error")
        
        else:
            img = Image(Point(150, 150), "{}.png".format(A))
            img.draw(win)

            lst[0] = 'X'

    elif 200 <= click1.getX() <= 300 and 100 <= click1.getY() <= 200:

        if lst[1] != '-':
            print("Error")
        
        else:
            img = Image(Point(250, 150), "{}.png".format(A))
            img.draw(win)

            lst[1] = 'X'
        
    elif 300 <= click1.getX() <= 400 and 100 <= click1.getY() <= 200:

        if lst[2] != '-':
            print("Error")
        
        else:
            img = Image(Point(350, 150), "{}.png".format(A))
            img.draw(win)

            lst[2] = 'X'

    elif 100 <= click1.getX() <= 200 and 200 <= click1.getY() <= 300:
        
        if lst[3] != '-':
            print("Error")
        
        else:
            img = Image(Point(150, 250), "{}.png".format(A))
            img.draw(win)

            lst[3] = 'X'

    elif 200 <= click1.getX() <= 300 and 200 <= click1.getY() <= 300:

        if lst[4] != '-':
            print("Error")
        
        else:
            img = Image(Point(250, 250), "{}.png".format(A))
            img.draw(win)

            lst[4] = 'X'

    elif 300 <= click1.getX() <= 400 and 200 <= click1.getY() <= 300:

        if lst[5] != '-':
            print("Error")
        
        else:
            img = Image(Point(350, 250), "{}.png".format(A))
            img.draw(win)

            lst[5] = 'X'
        
    elif 100 <= click1.getX() <= 200 and 300 <= click1.getY() <= 400:

        if lst[6] != '-':
            print("Error")
        
        else:
            img = Image(Point(150, 350), "{}.png".format(A))
            img.draw(win)

            lst[6] = 'X'

    elif 200 <= click1.getX() <= 300 and 300 <= click1.getY() <= 400:

        if lst[7] != '-':
            print("Error")
        
        else:
            img = Image(Point(250, 350), "{}.png".format(A))
            img.draw(win)

            lst[7] = 'X'

    elif 300 <= click1.getX() <= 400 and 300 <= click1.getY() <= 400:

        if lst[8] != '-':
            print("Error")
        
        else:
            img = Image(Point(350, 350), "{}.png".format(A))
            img.draw(win)

            lst[8] = 'X'

    else:

        pass

    check_X()

def O():
    click1 = win.getMouse()
    
    if 100 <= click1.getX() <= 200 and 100 <= click1.getY() <= 200:

        if lst[0] != '-':
            print("Error")
        
        else:
            img = Image(Point(150, 150), "{}.png".format(B))
            img.draw(win)

            lst[0] = 'O'

    elif 200 <= click1.getX() <= 300 and 100 <= click1.getY() <= 200:

        if lst[1] != '-':
            print("Error")
        
        else:
            img = Image(Point(250, 150), "{}.png".format(B))
            img.draw(win)

            lst[1] = 'O'

    elif 300 <= click1.getX() <= 400 and 100 <= click1.getY() <= 200:

        if lst[2] != '-':
            print("Error")
        
        else:
            img = Image(Point(350, 150), "{}.png".format(B))
            img.draw(win)

            lst[2] = 'O'

    elif 100 <= click1.getX() <= 200 and 200 <= click1.getY() <= 300:

        if lst[3] != '-':
            print("Error")
        
        else:
            img = Image(Point(150, 250), "{}.png".format(B))
            img.draw(win)

            lst[3] = 'O'

    elif 200 <= click1.getX() <= 300 and 200 <= click1.getY() <= 300:

        if lst[4] != '-':
            print("Error")
        
        else:
            img = Image(Point(250, 250), "{}.png".format(B))
            img.draw(win)

            lst[4] = 'O'

    elif 300 <= click1.getX() <= 400 and 200 <= click1.getY() <= 300:

        if lst[5] != '-':
            print("Error")
        
        else:
            img = Image(Point(350, 250), "{}.png".format(B))
            img.draw(win)

            lst[5] = 'O'
            
    elif 100 <= click1.getX() <= 200 and 300 <= click1.getY() <= 400:

        if lst[6] != '-':
            print("Error")
        
        else:
            img = Image(Point(150, 350), "{}.png".format(B))
            img.draw(win)

            lst[6] = 'O'

    elif 200 <= click1.getX() <= 300 and 300 <= click1.getY() <= 400:

        if lst[7] != '-':
            print("Error")
        
        else:
            img = Image(Point(250, 350), "{}.png".format(B))
            img.draw(win)

            lst[7] = 'O'

    elif 300 <= click1.getX() <= 400 and 300 <= click1.getY() <= 400:

        if lst[8] != '-':
            print("Error")
        
        else:
            img = Image(Point(350, 350), "{}.png".format(B))
            img.draw(win)

            lst[8] = 'O'

    else:

        pass

    check_O()

# -----------------------------------------------------------------------#    
    
def grid():
    global flag
    flag = 0
    
    line1 = Line(Point(200,100), Point(200,400))
    line2 = Line(Point(300,100), Point(300,400))
    line3 = Line(Point(100,200), Point(400,200))
    line4 = Line(Point(100,300), Point(400,300))

    line1.setWidth(2)
    line2.setWidth(2)
    line3.setWidth(2)
    line4.setWidth(2)

    time.sleep(0.1)
    line1.draw(win)

    time.sleep(0.1)
    line2.draw(win)

    time.sleep(0.1)
    line3.draw(win)

    time.sleep(0.1)
    line4.draw(win)

# --------------------------------------------------------------------#
# -----------------------program starts-------------------------------#
# --------------------------------------------------------------------#

win = GraphWin("Tic Tac Toe", 500, 500)

img = Image(Point(250, 250), "3t_bg.gif")
img.draw(win)

# header
title = Text(Point(250, -40), "tic tac toe ")
title.setSize(35)
title.setTextColor('white')
title.setFace('Botsmatic Outline')
title.draw(win)

for i in range(16):
    title.move(0, 5)
    time.sleep(0.005)

# --------------------------------------------------------------------#


play = Text(Point(250, 540), "PLAY")
play.setSize(35)
play.setTextColor('white')
play.setFace('Azonix')
play.setStyle('bold')
play.draw(win)

for i in range(18):
    play.move(0, -5)
    time.sleep(.01)
    
# --------------------------------------------------------------------#
ch = True
while ch is True:
    chk = win.getMouse()
    if 170 <= int(chk.getX()) <= 330 and 425 <= int(chk.getY()) <= 470:
        pt = Point(170, 470)
        pt1 = Point(330, 425)
        ch = False

        play_rect = Rectangle(pt, pt1)
        play_rect.setWidth(3)
        play_rect.setOutline('white')

        play_rect.draw(win)
        # winsound.PlaySound("click_1", winsound.SND_FILENAME)
        
        time.sleep(0.2)
        play_rect.undraw()
        time.sleep(0.2)

        for i in range(18):
            play.move(0, 5)
            time.sleep(0.01)
        
    else:
        pass
# -------------------------------------------------------------------#

# slider below computer

slide1 = Rectangle(Point(95, 465), Point(105, 500))
slide1.setOutline('white')
slide1.setFill('white')
slide1.move(0, 100)
slide1.setWidth(0)
slide1.draw(win)

letter1 = Text(Point(100, 550), 'C')
letter1.setSize(20)
letter1.setTextColor('white')
letter1.setFace('Black And White Display')
letter1.draw(win)

# slider below player

slide2 = Rectangle(Point(320, 465), Point(330, 500))
slide2.setOutline('white')
slide2.setFill('white')
slide2.move(0, 100)
slide2.setWidth(0)
slide2.draw(win)

letter2 = Text(Point(330, 550), 'P')
letter2.setSize(20)
letter2.setTextColor('white')
letter2.setFace('Black And White Display')
letter2.draw(win)

for i in range(20):
    slide1.move(0, -5)
    slide2.move(0, -5)
    
    letter1.move(0, -5)
    letter2.move(0, -5)
    
    time.sleep(0.001)
    
time.sleep(0.01)


word = "COMPUTER"
word2 = "PLAYER"

# word ---> w1 --> d1
# word2 --> w2 --> d2

a=0

for i in range(8):
    check = i
    for j in range(65,ord(word[i])):
        slide1.move(0, 5)      # move out slider below computer
        slide2.move(0, 5)      # move out slide below player
        d1 = Text(Point(a+100, 450), chr(j))

        if check < len(word2):
            d2 = Text(Point(a+330, 450), chr(j))
        
        d1.setSize(20)
        d2.setSize(20)
        
        d1.setFace('Black And White Display')
        d2.setFace('Black And White Display')
        
        d1.setTextColor('white')
        d2.setTextColor('white')
        
        d1.draw(win)
        
        if check < len(word2):
            d2.draw(win)

        time.sleep(0.01)
        
        d1.move(-600, 0)
        d2.move(600, 0)
        
    w1 = Text(Point(a+100, 450), word[i])
    w1.setSize(20)
    w1.setTextColor('white')
    w1.setFace('Black And White Display')
    w1.draw(win)

    if check < len(word2):
        w2 = Text(Point(330+a,450), word2[i])
        w2.setSize(20)
        w2.setTextColor('white')
        w2.setFace('Black And White Display')
        w2.draw(win)
    
    a+=13

slide1.undraw()
slide2.undraw()

letter1.undraw()
letter2.undraw()

# --------------------------------------------------------------------#
ch = True
while ch is True:
    chk = win.getMouse()
    if 85 <= int(chk.getX()) <= 205 and 435 <= int(chk.getY()) <= 470:
        
        ch = False

        boxc = Rectangle(Point(85, 470), Point(205, 435))
        boxc.setOutline('white')
        boxc.setWidth(3)
        boxc.draw(win)
        
        time.sleep(0.2)

        boxc.undraw()

        cimg = Image(Point(-250, 250), "back.png")
        cimg.draw(win)

        for i in range(50):
            cimg.move(10, 0)
            img.move(10, 0)
            title.move(10, 0)
            play.move(10, 0)
            
            time.sleep(0.01)

        exch = True
        while exch :
            
            computer()
            grid()

            lst = ['-','-','-','-','-','-','-','-','-']

            for i in range(5):

                if flag == 1:
                    break

                else:
                    
                    click1 = win.getMouse()
                    

                    try:
                            
                        if A == 'X':
                            
                            if 100 <= click1.getX() <= 200 and 100 <= click1.getY() <= 200:

                                if lst[0] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(150, 150), "{}.png".format(A))
                                    img.draw(win)

                                    lst[0] = 'X'

                            elif 200 <= click1.getX() <= 300 and 100 <= click1.getY() <= 200:

                                if lst[1] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(250, 150), "{}.png".format(A))
                                    img.draw(win)

                                    lst[1] = 'X'
                                
                            elif 300 <= click1.getX() <= 400 and 100 <= click1.getY() <= 200:

                                if lst[2] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(350, 150), "{}.png".format(A))
                                    img.draw(win)

                                    lst[2] = 'X'

                            elif 100 <= click1.getX() <= 200 and 200 <= click1.getY() <= 300:
                                
                                if lst[3] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(150, 250), "{}.png".format(A))
                                    img.draw(win)

                                    lst[3] = 'X'

                            elif 200 <= click1.getX() <= 300 and 200 <= click1.getY() <= 300:

                                if lst[4] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(250, 250), "{}.png".format(A))
                                    img.draw(win)

                                    lst[4] = 'X'

                            elif 300 <= click1.getX() <= 400 and 200 <= click1.getY() <= 300:

                                if lst[5] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(350, 250), "{}.png".format(A))
                                    img.draw(win)

                                    lst[5] = 'X'
                                
                            elif 100 <= click1.getX() <= 200 and 300 <= click1.getY() <= 400:

                                if lst[6] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(150, 350), "{}.png".format(A))
                                    img.draw(win)

                                    lst[6] = 'X'

                            elif 200 <= click1.getX() <= 300 and 300 <= click1.getY() <= 400:

                                if lst[7] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(250, 350), "{}.png".format(A))
                                    img.draw(win)

                                    lst[7] = 'X'

                            elif 300 <= click1.getX() <= 400 and 300 <= click1.getY() <= 400:

                                if lst[8] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(350, 350), "{}.png".format(A))
                                    img.draw(win)

                                    lst[8] = 'X'

                            else:
                                pass

                                    
                        time.sleep(0.1)
                        ai_for_X()
                        
                                
                    except:
                            
                        if lst1 == ['O']:
                            
                            if 100 <= click1.getX() <= 200 and 100 <= click1.getY() <= 200:

                                if lst[0] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(150, 150), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[0] = 'O'

                            elif 200 <= click1.getX() <= 300 and 100 <= click1.getY() <= 200:

                                if lst[1] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(250, 150), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[1] = 'O'

                            elif 300 <= click1.getX() <= 400 and 100 <= click1.getY() <= 200:

                                if lst[2] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(350, 150), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[2] = 'O'

                            elif 100 <= click1.getX() <= 200 and 200 <= click1.getY() <= 300:

                                if lst[3] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(150, 250), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[3] = 'O'

                            elif 200 <= click1.getX() <= 300 and 200 <= click1.getY() <= 300:

                                if lst[4] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(250, 250), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[4] = 'O'

                            elif 300 <= click1.getX() <= 400 and 200 <= click1.getY() <= 300:

                                if lst[5] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(350, 250), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[5] = 'O'
                                    
                            elif 100 <= click1.getX() <= 200 and 300 <= click1.getY() <= 400:

                                if lst[6] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(150, 350), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[6] = 'O'

                            elif 200 <= click1.getX() <= 300 and 300 <= click1.getY() <= 400:

                                if lst[7] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(250, 350), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[7] = 'O'

                            elif 300 <= click1.getX() <= 400 and 300 <= click1.getY() <= 400:

                                if lst[8] != '-':
                                    print("Error")
                                
                                else:
                                    img = Image(Point(350, 350), "{}.png".format(lst1[0]))
                                    img.draw(win)

                                    lst[8] = 'O'

                            else:
                                pass

                        time.sleep(0.1)
                        ai_for_O()

            if flag == 0:

                text = Text(Point(250, 450), "DRAW")
                text.setFace('Black And White Display')
                text.setTextColor(color_rgb(70, 71, 58))
                text.setSize(20)
                text.draw(win)

            exch = False

            replay = Text(Point(-50, 480), "replay ")
            replay.setSize(15)
            replay.setTextColor('white')
            replay.setFace('All the Way to the Sun')
            replay.draw(win)

            quit1 = Text(Point(560, 480), "quit ")
            quit1.setSize(15)
            quit1.setTextColor('white')
            quit1.setFace('All the Way to the Sun')
            quit1.draw(win)

            time.sleep(0.2)
                
            for i in range(20):   
                replay.move(5, 0)
                quit1.move(-5, 0)
                time.sleep(0.01)

                
            chec = True
            while chec:

                click = win.getMouse()

                if 15 <= click.getX() <= 87 and 470 <= click.getY() <= 490:
                    exch = True
                    chec = False
    
                    for i in range(3):
                        cimg.move(5, 0)
                        time.sleep(0.01)
                        cimg.move(-5, 0)
                        time.sleep(0.01)
                        cimg.move(-5, 0)
                        time.sleep(0.01)
                        cimg.move(5, 0)
                        time.sleep(0.01)

                elif 440 <= click.getX() <= 480 and 470 <= click.getY() <= 490:
                    exch = False
                    chec = False

                    close()
                    
                    win.close()
                    
                else:
                    pass





        
    elif 315 <= int(chk.getX()) <= 405 and 435 <= int(chk.getY()) <= 470:

        ch = False
        
        boxp = Rectangle(Point(315, 470), Point(405, 435))
        boxp.setOutline('white')
        boxp.setWidth(3)
        boxp.draw(win)

        time.sleep(0.2)

        boxp.undraw()

        cimg = Image(Point(750, 250), "back.png")
        cimg.draw(win)

        for i in range(50):
            cimg.move(-10, 0)
            img.move(-10, 0)
            title.move(-10, 0)
            play.move(-10, 0)
            
            time.sleep(0.01)

        exch = True
        while exch :

            player()
            grid()

            lst = ['-','-','-','-','-','-','-','-','-']
            
            for i in range(5):

                if flag == 1:
                    break

                else:
                    
                    
                    if A == 'X':

                        if flag == 1:
                            break

                        else:
                            
                            X()

                            if flag == 1:
                                break

                            else:
                            
                                if '-' in lst:
                                    O()
                                else:
                                    break
                            
                        
            if flag == 0:

                text = Text(Point(250, 450), "DRAW")
                text.setFace('Black And White Display')
                text.setTextColor(color_rgb(70, 71, 58))
                text.setSize(20)
                text.draw(win)

            exch = False

            replay = Text(Point(-50, 480), "replay ")
            replay.setSize(15)
            replay.setTextColor('white')
            replay.setFace('All the Way to the Sun')
            replay.draw(win)

            quit1 = Text(Point(560, 480), "quit ")
            quit1.setSize(15)
            quit1.setTextColor('white')
            quit1.setFace('All the Way to the Sun')
            quit1.draw(win)

            time.sleep(0.2)
                
            for i in range(20):   
                replay.move(5, 0)
                quit1.move(-5, 0)
                time.sleep(0.01)

                
            chec = True
            while chec:

                click = win.getMouse()

                if 15 <= click.getX() <= 87 and 470 <= click.getY() <= 490:
                    exch = True
                    chec = False

                    for i in range(3):
                        cimg.move(5, 0)
                        time.sleep(0.01)
                        cimg.move(-5, 0)
                        time.sleep(0.01)
                        cimg.move(-5, 0)
                        time.sleep(0.01)
                        cimg.move(5, 0)
                        time.sleep(0.01)

                elif 440 <= click.getX() <= 480 and 470 <= click.getY() <= 490:
                    exch = False
                    chec = False

                    close()
                    
                    win.close()

                else:
                    pass

        
    else:
        pass


# --------------------------------------------------------------------#
