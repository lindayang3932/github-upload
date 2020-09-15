# # run()
import math
from tkinter import *
from math import pi, cos, sin
import random
import copy 
scoreslevel1=[]
level1scores= copy.deepcopy(scoreslevel1)
scoreslevel2=[]
level2scores= copy.deepcopy(scoreslevel2)
def init(data):
  data.factor= 8
  data.factorlevel2=8
  data.mode="homescreen"
  data.z= 3
  data.time= 0
  data.timelevel2=0
  data.theta1= 3/2
  data.theta2= 5/2
  data.width= 1000
  data.height=1000 
  data.factor1= 250
  data.factor2= 20
  data.factor1level2=250
  data.factor2level2=20
  data.scoreslevel1=[]
  data.scoreslevel2=[]
  data.wallswon=wallzwon(data)
  data.walls=wallz2(data)
  data.wallslevel2=wallzlevel2(data)
  data.hexagons= hexagon(data)
  data.hexagonslevel2=hexagonlevel2(data)
  data.hexagonhome= hexagonhome(data)
  data.hexagonhomered= hexagonhomered(data)
  data.hexagonhomeyellow= hexagonhomeyellow(data)
  data.hexagongameover= hexagongameover(data)
  data.hexagongameover2= hexagongameover2(data)
  data.colors=["red","orange","yellow","green","SkyBlue2","blue","purple","magenta"]
  data.directionright= True 
  data.directionleft= True
def mousePressed(event, data):
    if (data.mode == "homescreen"): homeScreenMousePressed(event, data)
    elif (data.mode== "game"):   gamemousePressed(event, data)
    elif (data.mode== "game2"):   game2mousePressed(event, data)
    elif (data.mode== "help"):       helpMousePressed(event, data)
    elif (data.mode=="gameover"):  gameoverMousePressed(event, data)
    elif (data.mode=="gameover2"):  gameover2MousePressed(event, data)
    elif (data.mode=="won"):  wonMousePressed(event, data)
    elif (data.mode=="won2"):  won2MousePressed(event, data)
    elif (data.mode=="scores"):scoresMousePressed(event, data)
    elif (data.mode=="levels"):levelsMousePressed(event, data)

def keyPressed(event, data):
    if (data.mode== "homescreen"): homeScreenKeyPressed(event, data)
    elif (data.mode== "game"):   gamekeyPressed(event, data)
    elif (data.mode== "game2"):   game2keyPressed(event, data)
    elif (data.mode== "help"):       helpKeyPressed(event, data)
    elif (data.mode=="gameover"):   gameoverKeyPressed(event, data)
    elif (data.mode=="gameover2"):   gameover2KeyPressed(event, data)
    elif (data.mode=="won"):   wonKeyPressed(event, data)
    elif (data.mode=="won2"):   won2KeyPressed(event, data)
    elif (data.mode=="scores"):scoresKeyPressed(event, data)
    elif (data.mode=="levels"):levelsKeyPressed(event, data)

def timerFired(data):
    if (data.mode == "homescreen"): homeScreenTimerFired(data)
    elif (data.mode == "game"):   gametimerFired(data)
    elif (data.mode == "game2"):   game2timerFired(data)
    elif (data.mode == "help"):       helpTimerFired(data)
    elif (data.mode== "gameover"):    gameoverTimerFired(data)
    elif (data.mode== "gameover2"):    gameover2TimerFired(data)
    elif (data.mode== "won"):    wonTimerFired(data)
    elif (data.mode== "won2"):    won2TimerFired(data)
    elif (data.mode=="scores"):scoresTimerFired(data)
    elif (data.mode=="levels"):levelsTimerFired(data)

def redrawAll(canvas, data):
    if (data.mode == "homescreen"): homeScreenRedrawAll(canvas, data)
    elif (data.mode == "game"):   gameredrawAll(canvas, data)
    elif (data.mode == "game2"):   game2redrawAll(canvas, data)
    elif (data.mode == "help"):       helpRedrawAll(canvas, data)
    elif (data.mode== "gameover"):   gameoverRedrawAll(canvas, data)
    elif (data.mode== "gameover2"):   gameover2RedrawAll(canvas, data)
    elif (data.mode== "won"):   wonRedrawAll(canvas, data)
    elif (data.mode== "won2"):   won2RedrawAll(canvas, data)
    elif (data.mode=="scores"):scoresRedrawAll(canvas, data)
    elif (data.mode=="levels"):levelsRedrawAll(canvas, data)
###############################
#######Scores    ##############
###############################
def scoresMousePressed(event, data):
  if (event.x<=150 and event.x>=30) and (event.y<=300 and event.y>=50):
    data.mode= "homescreen"


def scoresRedrawAll(canvas, data):
  scoreslevel1.sort()
  scoreslevel2.sort()
  for i in range(len(scoreslevel1)):
    canvas.create_text(300, 200+50*i,
          text=str(scoreslevel1[-1-i])+"%",font="verdana 26 ", fill="grey")
  for i in range(len(scoreslevel2)):
    canvas.create_text(600, 200+50*i,
          text=str(scoreslevel2[-1-i])+"%",font="verdana 26 ", fill="grey")
  canvas.create_text(300,150, text="LEVEL 1 SCORES", font="verdana 26 ", fill="grey")
  canvas.create_text(600,150, text="LEVEL 2 SCORES", font="verdana 26 ", fill="grey")
  data.image2= PhotoImage(file= "backbutton.gif")
  canvas.create_image(100,100, image=data.image2)
###############################
#######levels    ##############
###############################
def levelsMousePressed(event, data):
  if (event.x<=150 and event.x>=30) and (event.y<=300 and event.y>=50):
    data.mode= "homescreen"


def levelsRedrawAll(canvas, data):
  data.image2= PhotoImage(file= "backbutton.gif")
  canvas.create_image(100,100, image=data.image2)
  data.image3= PhotoImage(file= "levelsdescription.gif")
  canvas.create_image(500,400, image=data.image3)


################################
#######Home Screen##############
###############################
class hexagonzhome(object):
  def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3,theta1,theta2,factor1,factor2):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    self.x0= x0
    self.y0= y0
    self.x1=x1
    self.y1=y1
    self.x2= x2
    self.y2= y2
    self.x3= x3
    self.y3= y3
  def moveright(self):
    self.theta1+=1.3
    self.theta2+=1.3
  def moveleft(self):
    self.theta1-=0.5
    self.theta2-=0.5
  def movestop(self):
    self.theta1+=0
    self.theta2+=0
  def moverightincrements(self):
    self.theta1+=0.1
    self.theta2+=0.1
  def moveleftincrements(self):
    self.theta1-=0.1
    self.theta2-=0.1
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                          self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                          self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                          self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                           fill="black")
class hexagonzhomered(object):
  def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3,theta1,theta2,factor1,factor2):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    self.x0= x0
    self.y0= y0
    self.x1=x1
    self.y1=y1
    self.x2= x2
    self.y2= y2
    self.x3= x3
    self.y3= y3
  def moveright(self):
    self.theta1+=1.3
    self.theta2+=1.3
  def moveleft(self):
    self.theta1-=0.5
    self.theta2-=0.5
  def movestop(self):
    self.theta1+=0
    self.theta2+=0
  def moverightincrements(self):
    self.theta1+=0.1
    self.theta2+=0.1
  def moveleftincrements(self):
    self.theta1-=0.1
    self.theta2-=0.1
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                          self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                          self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                          self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                           fill="red")
class hexagonzhomeyellow(object):
  def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3,theta1,theta2,factor1,factor2):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    self.x0= x0
    self.y0= y0
    self.x1=x1
    self.y1=y1
    self.x2= x2
    self.y2= y2
    self.x3= x3
    self.y3= y3
  def moveright(self):
    self.theta1+=1.3
    self.theta2+=1.3
  def moveleft(self):
    self.theta1-=0.5
    self.theta2-=0.5
  def movestop(self):
    self.theta1+=0
    self.theta2+=0
  def moverightincrements(self):
    self.theta1+=0.1
    self.theta2+=0.1
  def moveleftincrements(self):
    self.theta1-=0.1
    self.theta2-=0.1
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                          self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                          self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                          self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                           fill="yellow")
def hexagonhomered(data):
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonzhomered(171,181,
                      171,181,
                      171,181,
                      171,181,i+data.theta1, i+data.theta2,50,1))
  return hexagons
def hexagonhomeyellow(data):
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonzhomeyellow(189,177,
                      189,177,
                      189,177,
                      189,177,i+data.theta1, i+data.theta2,50,1))
  return hexagons
def hexagonhome(data):
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonz(180,186,
                      180,186,
                      180,186,
                      180,186,i+data.theta1, i+data.theta2,50,1))
  return hexagons

def homeScreenMousePressed(event, data):
  if (event.x<=300 and event.x>=105) and (event.y<=540 and event.y>=350):
    data.mode= "help"
  if (event.x<=600 and event.x>=405) and (event.y<=540 and event.y>=350):
    data.mode= "levels"
  if (event.x<=900 and event.x>=705) and (event.y<=640 and event.y>=350):
    data.mode= "scores"
def homeScreenKeyPressed(event, data):
    if (event.keysym=="Return"):
      data.mode= "game"


def homeScreenTimerFired(data):
  for x in range(8):
      hexagonzhome.moveright(data.hexagonhome[x])
  for x in range(8):
      hexagonzhomered.moveleft(data.hexagonhomered[x])
  for x in range(8):
      hexagonzhomeyellow.moveleft(data.hexagonhomeyellow[x])
def image(canvas, data):
    data.image= PhotoImage(file="homescreen.gif")
    canvas.create_image(550,200, image= data.image)
def image2(canvas, data):
    data.image2= PhotoImage(file="hiii.gif")
    canvas.create_image(500,700, image= data.image2)
def homeScreenRedrawAll(canvas, data):
    data.image3= PhotoImage(file="button1.gif")
    canvas.create_image(200,450, image=data.image3)
    canvas.create_image(500,450, image= data.image3)
    canvas.create_image(800,450, image=data.image3)
    canvas.create_oval(150,400,250,500
                        , fill="black")
    canvas.create_oval(450,400,550,500
                        , fill="black")
    canvas.create_oval(750,400,850,500
                        , fill="black")
    data.image4= PhotoImage(file="help.gif")
    data.image5=PhotoImage(file="levels.gif")
    data.image6=PhotoImage(file="scores.gif")
    canvas.create_image(200, 450, image=data.image4)
    canvas.create_image(505, 452, image=data.image5)
    canvas.create_image(802, 450, image=data.image6)
    image(canvas,data)
    image2(canvas,data)
    for hexagon in data.hexagonhomeyellow:
      hexagon.draw(canvas)
    for hexagon in data.hexagonhomered:
      hexagon.draw(canvas)
    for hexagon in data.hexagonhome:
      hexagon.draw(canvas)
    canvas.create_oval(150,156,210,216
                        , fill="white")
    canvas.create_oval(157,163,203,209
                        , fill="black")
####################################
# help mode
####################################

def helpMousePressed(event, data):
  if (event.x<=150 and event.x>=30) and (event.y<=300 and event.y>=50):
    data.mode= "homescreen"

def helpKeyPressed(event, data):
    pass

def helpTimerFired(data):
    pass


def helpRedrawAll(canvas, data):
    data.image= PhotoImage(file="description.gif")
    data.image2= PhotoImage(file= "backbutton.gif")
    canvas.create_image(500,400, image=data.image)
    canvas.create_image(100,100, image=data.image2)
####################################
# wonlevel1 mode
####################################

def wonMousePressed(event, data):
    pass

def wonKeyPressed(event, data):
    if event.keysym=="r":
      data.mode="game2"

def wonTimerFired(data):
    pass


def wonRedrawAll(canvas, data):
    image(canvas,data)
    # image2(canvas,data)
    for hexagon in data.hexagongameover:
      hexagon.draw(canvas)
    canvas.create_oval(150,156,210,216
                        , fill="white")
    canvas.create_oval(157,163,203,209
                        , fill="black")
    canvas.create_text(500, 400,
          text="LEVEL ONE PASSED!",font="verdana 36 ", fill="grey")
    canvas.create_text(500, 500,
          text="PRESS R TO START LEVEL 2",font="verdana 36 ", fill="grey")
####################################
# wonlevel2 mode
####################################

class wallswon(object):
  def __init__(self, x0,y0,x1,y1,x2,y2,x3,y3, theta1,theta2,factor1,factor2, index):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    faraway= "False"
    self.x0=x0
    self.y0=y0 
    self.x1=x1
    self.y1=y1 
    self.x2=x2
    self.y2=y2 
    self.x3=x3
    self.y3=y3 
    self.index= index
    self.colorsinitial= ("red","orange", "yellow","green","SkyBlue2","blue","purple","magenta")
    
  def moveright(self):
    self.theta1+=1
    self.theta2+=1
  def moveleft(self):
    self.theta1-=1
    self.theta2-=1
  def movestop(self):
    self.theta1-=0
    self.theta2-=0

  def getbigger(self):
    self.factor1*=1.1
    self.factor2*=1.0
  def getbiggerlater(self):
    self.factor1*=1.1
    self.factor2*=1.1


  def drawcolor(self, canvas):

    canvas.create_text(500, 500,
                       text=currentcolor, font="Arial 26 bold")
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                            self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                            self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                            self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                             fill=self.colorsinitial[self.index])
def wallzwon(data):
  colors=["red","orange","yellow","green","SkyBlue2","blue","purple","magenta"]
  wall= []
  for i in range(8):
    wall.append(walls(500,400,
                      500,400,
                      500,400,
                      500,400,i+3/2, i+5/2,data.factor1,data.factor2,i))
  return wall
def won2MousePressed(event, data):
    pass

def won2KeyPressed(event, data):
    if event.keysym=="space":
        data.mode= "homescreen"

def levelsKeyPressed(event, data):
    pass
def scoresKeyPressed(event, data):
    pass	
	
def won2TimerFired(data):
  for wall in data.wallswon:
    wall.getbiggerlater()

def scoresTimerFired(data):
    pass	
def levelsTimerFired(data):
    pass		

def won2RedrawAll(canvas, data):
  for wall in data.wallswon:
    wall.draw(canvas)
  data.image= PhotoImage(file= "gameover.gif")
  canvas.create_image(500,400, image=data.image)
####################################
# game over
####################################
class hexagonzgameover(object):
  def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3,theta1,theta2,factor1,factor2):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    self.x0= x0
    self.y0= y0
    self.x1=x1
    self.y1=y1
    self.x2= x2
    self.y2= y2
    self.x3= x3
    self.y3= y3
  def moveright(self):
    self.theta1+=1.3
    self.theta2+=1.3
  def moveleft(self):
    self.theta1-=0.5
    self.theta2-=0.5
  def movestop(self):
    self.theta1+=0
    self.theta2+=0
  def moverightincrements(self):
    self.theta1+=0.1
    self.theta2+=0.1
  def moveleftincrements(self):
    self.theta1-=0.1
    self.theta2-=0.1
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                          self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                          self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                          self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                           fill="black")
def hexagongameover(data):
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonz(180,186,
                      180,186,
                      180,186,
                      180,186,i+data.theta1, i+data.theta2,50,1))
  return hexagons
def image(canvas, data):
    data.image= PhotoImage(file="homescreen.gif")
    canvas.create_image(550,200, image= data.image)


def gameoverMousePressed(event, data):
    pass

def gameoverKeyPressed(event, data):
    if event.keysym=="Return":
        init(data)

def gameoverTimerFired(data):
  for x in range(8):
    hexagonzgameover.moveright(data.hexagongameover[x])


def gameoverRedrawAll(canvas, data):
    image(canvas,data)
    # image2(canvas,data)
    data.image3= PhotoImage(file="gameoverlevel1.gif")
    data.image4=PhotoImage(file="last.gif")
    data.image5= PhotoImage(file="best.gif")
    data.image6= PhotoImage(file= "retry.gif")
    canvas.create_image(500,350, image= data.image3)
    canvas.create_image(300,450, image= data.image4)
    canvas.create_image(300,550, image= data.image5)
    canvas.create_image(500,700, image= data.image6)
    for hexagon in data.hexagongameover:
      hexagon.draw(canvas)
    canvas.create_oval(150,156,210,216
                        , fill="white")
    canvas.create_oval(157,163,203,209
                        , fill="black")
    canvas.create_text(570, 440,
          text=str(data.scoreslevel1[-1])+"%",font="verdana 72 ", fill="grey")
    canvas.create_text(570, 540,
          text=str(max(scoreslevel1))+"%",font="verdana 72 ", fill="grey")

####################################
# game over level2
####################################
class hexagonzgameover2(object):
  def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3,theta1,theta2,factor1,factor2):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    self.x0= x0
    self.y0= y0
    self.x1=x1
    self.y1=y1
    self.x2= x2
    self.y2= y2
    self.x3= x3
    self.y3= y3
  def moveright(self):
    self.theta1+=1.3
    self.theta2+=1.3
  def moveleft(self):
    self.theta1-=0.5
    self.theta2-=0.5
  def movestop(self):
    self.theta1+=0
    self.theta2+=0
  def moverightincrements(self):
    self.theta1+=0.1
    self.theta2+=0.1
  def moveleftincrements(self):
    self.theta1-=0.1
    self.theta2-=0.1
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                          self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                          self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                          self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                           fill="black")
def hexagongameover2(data):
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonz(180,186,
                      180,186,
                      180,186,
                      180,186,i+data.theta1, i+data.theta2,50,1))
  return hexagons
def image(canvas, data):
    data.image= PhotoImage(file="homescreen.gif")
    canvas.create_image(550,200, image= data.image)

def gameover2MousePressed(event, data):
    pass

def gameover2KeyPressed(event, data):
    if event.keysym=="Return":
      init(data)

def gameover2TimerFired(data):
  for x in range(8):
    hexagonzgameover2.moveright(data.hexagongameover2[x])


def gameover2RedrawAll(canvas, data):
    image(canvas,data)
    # image2(canvas,data)
    data.image4=PhotoImage(file="last.gif")
    data.image5= PhotoImage(file="best.gif")
    data.image6= PhotoImage(file= "retry.gif")
    canvas.create_image(300,450, image= data.image4)
    canvas.create_image(300,550, image= data.image5)
    canvas.create_image(500,700, image= data.image6)
    for hexagon in data.hexagongameover:
      hexagon.draw(canvas)
    canvas.create_oval(150,156,210,216
                        , fill="white")
    canvas.create_oval(157,163,203,209
                        , fill="black")
    canvas.create_text(570, 440,
          text=str(data.scoreslevel2[-1])+"%",font="verdana 72 ", fill="grey")
    canvas.create_text(570, 540,
          text=str(max(scoreslevel2))+"%",font="verdana 72 ", fill="grey")

###############################
#######GAME level 1############
###############################
class walls(object):
  def __init__(self, x0,y0,x1,y1,x2,y2,x3,y3, theta1,theta2,factor1,factor2, index):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    faraway= "False"
    self.x0=x0
    self.y0=y0 
    self.x1=x1
    self.y1=y1 
    self.x2=x2
    self.y2=y2 
    self.x3=x3
    self.y3=y3 
    self.index= index
    self.colorsinitial= ("red","orange", "yellow","green","SkyBlue2","blue","purple","magenta")
    self.colors=(random.choice(["red","red","red","red","red","red","red","red","red","red","white"]),random.choice(["orange","orange","orange","orange","orange","orange","orange","orange","white"]),
                  random.choice(["yellow","yellow","yellow","yellow","yellow","yellow", "yellow", "yellow", "yellow", "white"]),random.choice(["green","green","green","green","green","green","green","green","green","white"]),
                  random.choice(["SkyBlue2","SkyBlue2","SkyBlue2","SkyBlue2","SkyBlue2","SkyBlue2","SkyBlue2","SkyBlue2","white"]),random.choice(["blue","blue","blue","blue","blue","blue","blue","blue","blue","blue", "white"]),
                  random.choice(["purple","purple", "white", "purple","purple","purple","purple","purple","purple","purple"]),random.choice(["magenta","magenta", "magenta","magenta","magenta","magenta","magenta","magenta","white"]))
  def moveright(self):
    self.theta1+=1
    self.theta2+=1
  def moveleft(self):
    self.theta1-=1
    self.theta2-=1
  def movestop(self):
    self.theta1-=0
    self.theta2-=0

  def getbigger(self):
    self.factor1*=1.1
    self.factor2*=1.0
  def getbiggerlater(self):
    self.factor1*=1.1
    self.factor2*=1.1


  def drawcolor(self, canvas):

    canvas.create_text(500, 500,
                       text=currentcolor, font="Arial 26 bold")
  def draw(self, canvas):
    if self.index>=8:
      canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                            self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                            self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                            self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                             fill=self.colors[self.index%8])
    elif self.index<8:
      canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                            self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                            self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                            self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                             fill=self.colorsinitial[self.index%8])
class hexagonz(object):
  def __init__(self,x0,y0,x1,y1,x2,y2,x3,y3,theta1,theta2,factor1,factor2):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    self.x0= x0
    self.y0= y0
    self.x1=x1
    self.y1=y1
    self.x2= x2
    self.y2= y2
    self.x3= x3
    self.y3= y3
  def moveright(self):
    self.theta1+=1
    self.theta2+=1
  def moveleft(self):
    self.theta1-=1
    self.theta2-=1
  def movestop(self):
    self.theta1+=0
    self.theta2+=0
  def moverightincrements(self):
    self.theta1+=0.1
    self.theta2+=0.1
  def moveleftincrements(self):
    self.theta1-=0.1
    self.theta2-=0.1
  def draw(self, canvas):
    canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                          self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                          self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                          self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                           fill="black")
def wallz(data):
  colors=["red","orange","yellow","green","SkyBlue2","blue","purple","magenta"]
  wall= []
  i= random.randint(1,8)
  wall.append(walls(500,400,
                      500,400,
                      500,400,
                      500,400,i+3/2, i+5/2,data.factor1,data.factor2,i))
  return wall
def wallz2(data):
  colors=["red","orange","yellow","green","SkyBlue2","blue","purple","magenta"]
  wall= []
  for i in range(8):
    wall.append(walls(500,400,
                      500,400,
                      500,400,
                      500,400,i+3/2, i+5/2,data.factor1,data.factor2,i))
  return wall
def hexagon(data):
  colors=["red","orange","yellow","green","SkyBlue2","blue","purple","magenta"]
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonz(500,550,
                      500,550,
                      500,550,
                      500,550,i+data.theta1, i+data.theta2,50,1))
  return hexagons

def gamemousePressed(event, data):
  pass 

def gamekeyPressed(event, data):
  if event.keysym== "Right": 
    for x in range(len(data.walls)):
      walls.moveright(data.walls[x])
  if event.keysym== "Left":
    for y in range(len(data.walls)):
      walls.moveleft(data.walls[y])
  if event.keysym=="space":
    for x in range(8):  
        walls.catch_bottom_color(data.walls[x]) 
  if event.keysym== "Right": 
    data.directionright= False 
    for x in range(8):
      hexagonz.moveright(data.hexagons[x])
  if event.keysym== "Left":
    data.directionleft= False 
    for y in range(8):
      hexagonz.moveleft(data.hexagons[y])

def gametimerFired(data): 
  data.time+=1
  for wall in data.walls:
    wall.getbiggerlater()
    if wall.factor1>= 300:
      wall.factor2*= 1.1
      wall.factor1*= 1.1
    i= random.randint(1,8)
    if (abs(wall.factor2- wall.factor1)>= 250 and abs(wall.factor2- wall.factor1)<=300) and data.factor!=0:
      data.factor-=1
      data.walls.append(walls(500,400,
                          500,400,
                          500,400,
                          500,400,wall.theta1, wall.theta2, 80, 20,wall.index+8))
    if (abs(wall.factor2- wall.factor1)>= 100 and abs(wall.factor2- wall.factor1)<=110):
      data.walls.append(walls(500,400,
                          500,400,
                          500,400,
                          500,400,wall.theta1, wall.theta2, 80, 20,wall.index+8))
    if wall.factor2>=700:
      data.walls.remove(wall)
    if wall.index>=8:
      if wall.colors[wall.index%8]=="white":
          if((wall.theta1 -1.5)%8 == 0.0):
              for hexagon in data.hexagons:
                  if((hexagon.theta1 -1.5)%8 == 0.0):
                      if (hexagon.x0+hexagon.factor1*sin(hexagon.theta1*pi/4))<=(wall.x0+wall.factor1*sin(wall.theta1*pi/4)):
                          if (hexagon.x0+hexagon.factor1*sin(hexagon.theta1*pi/4))<=(wall.x3+wall.factor1*sin(wall.theta2*pi/4)):
                              if (hexagon.y0+hexagon.factor1*sin(hexagon.theta1*pi/4))<= (wall.y0+wall.factor1*sin(wall.theta1*pi/4)):
                                  if (hexagon.y0+hexagon.factor1*sin(hexagon.theta1*pi/4))<= (wall.y3+wall.factor1*sin(wall.theta1*pi/4)):
                                    if (hexagon.y0+hexagon.factor1*sin(hexagon.theta1*pi/4))>= (wall.y1+wall.factor2*sin(wall.theta1*pi/4)):
                                      data.mode= "gameover"
                                      data.time+=0
                                      data.scoreslevel1.append(data.time)
                                      scoreslevel1.append(data.time)
  if data.time== 105:
    data.mode= "won"
def gameredrawAll(canvas, data):
  for wall in data.walls:
    wall.draw(canvas)
  canvas.create_text(100, 100,
         text=str(data.time)+"%",font="verdana 36 ", fill="grey")
  canvas.create_text(100, 100,
         text=str(data.time)+"%",font="verdana 36 ", fill="grey")
  for hexagon in data.hexagons:
    hexagon.draw(canvas)
  if data.time== 101:
    data.walls= []
###############################
#######GAME level 2############
###############################
class wallslevel2(object):
  def __init__(self, x0,y0,x1,y1,x2,y2,x3,y3, theta1,theta2,factor1,factor2, index):
    self.theta1= theta1
    self.theta2= theta2
    self.factor1= factor1
    self.factor2= factor2
    faraway= "False"
    self.x0=x0
    self.y0=y0 
    self.x1=x1
    self.y1=y1 
    self.x2=x2
    self.y2=y2 
    self.x3=x3
    self.y3=y3 
    self.index= index
    self.colorsinitial= ("red","orange", "yellow","green","SkyBlue2","blue","purple","magenta")
    self.colors=(random.choice(["red","red","red","red","red","red","white"]),random.choice(["orange","orange","orange","orange","orange","white"]),
                  random.choice(["yellow","yellow", "yellow", "yellow", "yellow", "white"]),random.choice(["green","green","green","green","green","green","white"]),
                  random.choice(["SkyBlue2","SkyBlue2","SkyBlue2","SkyBlue2","white"]),random.choice(["blue","blue","blue","blue","blue", "white"]),
                  random.choice(["purple","white","purple","purple","purple","purple"]),random.choice(["magenta","magenta","magenta","magenta","white"]))
  def moveright(self):
    self.theta1+=1
    self.theta2+=1
  def moveleft(self):
    self.theta1-=1
    self.theta2-=1
  def movestop(self):
    self.theta1-=0
    self.theta2-=0

  def getbigger(self):
    self.factor1*=1.1
    self.factor2*=1.0
  def getbiggerlater(self):
    self.factor1*=1.1
    self.factor2*=1.1

  def draw(self, canvas):
    if self.index>=8:
      canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                            self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                            self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                            self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                             fill=self.colors[self.index%8])
    elif self.index<8:
      canvas.create_polygon(self.x0+self.factor1*cos(self.theta1*pi/4),self.y0+self.factor1*sin(self.theta1*pi/4),
                            self.x1+self.factor2*cos(self.theta1*pi/4),self.y1+self.factor2*sin(self.theta1*pi/4),
                            self.x2+self.factor2*cos(self.theta2*pi/4),self.y2+self.factor2*sin(self.theta2*pi/4),
                            self.x3+self.factor1*cos(self.theta2*pi/4),self.y3+self.factor1*sin(self.theta2*pi/4),
                             fill=self.colorsinitial[self.index%8])

def wallzlevel2(data):
  colors=["red","orange","yellow","green","SkyBlue2","blue","purple","magenta"]
  wall= []
  for i in range(8):
    wall.append(wallslevel2(500,400,
                      500,400,
                      500,400,
                      500,400,i+3/2, i+5/2,data.factor1level2,data.factor2level2,i))
  return wall

def hexagonlevel2(data):
  hexagons= []
  for i in range(8):
    hexagons.append(hexagonz(500,550,
                      500,550,
                      500,550,
                      500,550,i+data.theta1, i+data.theta2,50,1))
  return hexagons

def game2mousePressed(event, data):
  pass

def game2keyPressed(event, data):
  if event.keysym== "Right": 
    for x in range(len(data.wallslevel2)):
      walls.moveright(data.wallslevel2[x])
  if event.keysym== "Left":
    for y in range(len(data.wallslevel2)):
      walls.moveleft(data.wallslevel2[y])
def game2timerFired(data): 
  data.timelevel2+=1
  for wall in data.wallslevel2:
    wall.getbiggerlater()
    if wall.factor1>= 300:
      wall.factor2*= 1.1
      wall.factor1*= 1.1
    i= random.randint(1,8)
    if (abs(wall.factor2- wall.factor1)>= 250 and abs(wall.factor2- wall.factor1)<=300) and data.factorlevel2!=0:
      data.factorlevel2-=1
      data.wallslevel2.append(wallslevel2(500,400,
                          500,400,
                          500,400,
                          500,400,wall.theta1, wall.theta2, 80, 20,wall.index+8))
    if (abs(wall.factor2- wall.factor1)>= 100 and abs(wall.factor2- wall.factor1)<=110):
      data.wallslevel2.append(wallslevel2(500,400,
                          500,400,
                          500,400,
                          500,400,wall.theta1, wall.theta2, 80, 20,wall.index+8))
    if wall.factor2>=700:
      data.wallslevel2.remove(wall)
    if wall.index>=8:
      if wall.colors[wall.index%8]=="white":
          if((wall.theta1 -1.5)%8 == 0.0):
              for hexagon in data.hexagonslevel2:
                  if((hexagon.theta1 -1.5)%8 == 0.0):
                      if (hexagon.x0+hexagon.factor1*sin(hexagon.theta1*pi/4))<=(wall.x0+wall.factor1*sin(wall.theta1*pi/4)):
                          if (hexagon.x0+hexagon.factor1*sin(hexagon.theta1*pi/4))<=(wall.x3+wall.factor1*sin(wall.theta2*pi/4)):
                              if (hexagon.y0+hexagon.factor1*sin(hexagon.theta1*pi/4))<= (wall.y0+wall.factor1*sin(wall.theta1*pi/4)):
                                  if (hexagon.y0+hexagon.factor1*sin(hexagon.theta1*pi/4))<= (wall.y3+wall.factor1*sin(wall.theta1*pi/4)):
                                    if (hexagon.y0+hexagon.factor1*sin(hexagon.theta1*pi/4))>= (wall.y1+wall.factor2*sin(wall.theta1*pi/4)):
                                      data.mode= "gameover2"
                                      data.timelevel2+=0
                                      data.scoreslevel2.append(data.timelevel2)
                                      scoreslevel2.append(data.timelevel2)
  if data.timelevel2== 110:
    
    data.mode= "won2"
def game2redrawAll(canvas, data):
  for wall in data.wallslevel2:
    wall.draw(canvas)
  canvas.create_text(100, 100,
         text=str(data.timelevel2)+"%",font="verdana 36 ", fill="grey")
  for hexagon in data.hexagonslevel2:
    hexagon.draw(canvas)
  if data.timelevel2== 101:
    data.wallslevel2= []

####################################
# use the run function as-is
####################################

def run(width=1000, height=1000):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        # gamemousePressed(event, data)
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        # gamekeyPressed(event, data)
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        # gametimerFired(data)
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 200# milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run()







