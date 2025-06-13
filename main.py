from processing import *
from game import *

kyla = {"x":340, "y":130, "w":40, "h":100}

# Covert the variables of Zonan and the Guard to dictionaries

zonan={'x':100,'y':300,'w':65,'h':110}
zonan={'x':280,'y':130,'w':65,'h':110}
zonan={'x':540,'y':160,'w':65,'h':110}


guard={'x':570,'y':160,'w':75,'h':120}

def setup():
    size(900, 519)
    
    global bgImg, zonanImg, kylaImg, guardImg
   
    bgImg = loadImage("assets/background.png")
    kylaImg = loadImage("assets/kyla.png")
    zonanImg = loadImage("assets/zonan.png")    
    guardImg = loadImage("assets/guard.png")
    gameInit()
def draw():    
    background(bgImg)
    play(zonan,kyla,guard)
    image(kylaImg, kyla["x"], kyla["y"], kyla["w"], kyla["h"])
    
    # Display the images of Zonan and the Guard using dictionaries
    image(zonanImg,zonan['x'],zonan['y'],zonan['w'],zonan['h'])
    image(guardImg, guard['x'], guard['y'], guard['w'], guard['h'])
    
  
run()