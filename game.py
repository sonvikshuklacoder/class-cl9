from processing import *
from helper import *

gameStage=-2
dialogText=""
dialogIndex= 0
sayDialog=True
zonan=None

animations=[]
showPath=False
gameState=""
endCount=0

def setMarker(x,y):
    marker["x"]=x
    marker["y"]=y
    
def gameInit():
    global markerAnimation, marker, villagers, villagerImages, dialogs, dialogBoxImage,  mouseMarker, pathAni, mapImg
    
    marker={"x":280, "y":110, "w":70, "h":130}
    mouseMarker={"x":0, "y":0, "w":10, "h":10}
    

    markerAnimation=loadAnimation(["assets/marker/1.png",
                                    "assets/marker/2.png","assets/marker/3.png",
                                    "assets/marker/4.png","assets/marker/5.png",
                                    "assets/marker/6.png","assets/marker/7.png",
                                    "assets/marker/8.png","assets/marker/9.png", 
                                    "assets/marker/10.png"])
    
    villagerImages=loadAnimation(["assets/kyla.png",
                                  "assets/guard.png",
                                  "assets/zonan.png",])
    
    dialogs=[
        "Hi, I am Zonan! The saviour.\nSomething happened in the 'Kindom of Darkmire.'\nLet me ask Kyla and find out what happened.",
        "Kyla: Last night, some miscreants invaded the kingdom. \nThe guard can give you more clues about the robbery.",
        "Guard: A dark wizard stole our kingdom's gem of wishes \nand rode towards the magical jungle!"
        ]
    
    dialogBoxImage=loadImage("assets/dialogueBox.png")
    
    pathAni=loadAnimation(["assets/path/0.png",
                          "assets/path/1.png",
                          "assets/path/2.png",
                          "assets/path/3.png",
                          "assets/path/4.png",
                          "assets/path/5.png",
                          "assets/path/6.png",
                          "assets/path/7.png",
                          "assets/path/8.png",
                          "assets/path/9.png",
                          "assets/path/10.png",
                          "assets/path/11.png",
                          "assets/path/12.png",
                          "assets/path/13.png",
                          "assets/path/14.png",
                          "assets/path/15.png",
                          "assets/path/16.png",
                          "assets/path/17.png",
                          "assets/path/18.png",
                          "assets/path/19.png",
                          "assets/path/20.png",
                          "assets/path/21.png",
                          "assets/path/22.png",
                          "assets/path/23.png",
                          "assets/path/24.png",
                          "assets/path/25.png",
                          "assets/path/26.png",
                          "assets/path/27.png",
                          "assets/path/28.png",
                          "assets/path/29.png",
                          "assets/path/30.png",
                          "assets/path/31.png",
                          "assets/path/32.png",
                          "assets/path/33.png",
                          "assets/path/34.png"
                          ])
    
    mapImg=loadImage("assets/map.png")


def play(zonan, villager1, villager2):
    global gameStage, dialogText, dialogIndex, sayDialog, dialog, gameState, endCount
 
    villagers=[villager1,villager2]
    
    if zonan != None:
        if gameStage==-2 :
            setMarker(villagers[0]["x"]-60, villagers[0]["y"])
        if gameStage==-1 or (zonan["x"]==villagers[0]["x"]-60 and zonan["y"]==villagers[0]["y"]):
            gameStage=-1
            setMarker(villagers[1]["x"]-70, villagers[1]["y"]-10) #Change this to set final location of marker to jungle
        if gameStage==0 or (villagers[1]["y"]-70 and zonan["y"]==villagers[1]["y"]-10):
            gameStage=0
            
            #display final image here(image that must be show when game ends)    
            setMarker(1000, 10000)
            endCount=endCount +1
            if  dialogIndex>=len(dialogText) and endCount>200:
                zonan["x"]=1000
                zonan["y"]=1000
                
                if endCount>300 and gameState!="endAnimation":
                    villagers[0]["x"]=2000
                    villagers[1]["x"]=2000
                    gameState="endAnimation"
                    tempObj={"x":240, "y":130, "w":350, "h":280}
                    showAnimation(tempObj, pathAni, 295, showStaticPath)
        
        dialogText=dialogs[gameStage+2]
        dialog=dialogText[0: int(dialogIndex)]
        if(dialogIndex<len(dialogText)):
            dialogIndex+=1

        if sayDialog:
            image(dialogBoxImage,200,400, 700,120)
            fill(0)
            textSize(18)
            text(dialog, 300, 450)

        if gameStage+1 > -1: 
            display(villagers[gameStage+1], villagerImages[gameStage+1])
        
        image(villagerImages[gameStage+1], 110,370,200,300)

        if(dialogIndex>=len(dialogText)):
            display(marker, markerAnimation,1.5)

            mouseMarker["x"]=mouseX()
            mouseMarker["y"]=mouseY()
            if(isTouching(mouseMarker, marker)):
                fill(255)
                rect(marker["x"]-20, marker["y"]+62,75,20,5)
                marker_location_text= str(marker["x"])+", "+ str(marker["y"])
                fill(0)
                text(marker_location_text, marker["x"]-18, marker["y"]+80)

        

        if gameState=="endAnimation":
            fill(255, 255, 255,200)
            rect(0,0,900,519)
            image(mapImg, -((1196*519/640) -900) /2,0,1196*519/640, 640*519/640) 
    
        if showPath== True:
            image(pathAni[-1],240,130,350,280)
            fill(0,0,0)
            textSize(18)
            text("2", 385, 390)
            zonan["x"]=400
            zonan["y"]=290
            zonan["w"]=55
            zonan["h"]=90
        
        displayAnimations()
        
def showAnimation(animationObj, animation, time, callback=None, callbackObj=None):
    animations.append([animationObj,animation,time, callback, callbackObj])
    
def displayAnimations():
    for animationData in animations:
        animationObj=animationData[0]
        animation=animationData[1]
        time=animationData[2]
        if time>0:
            display(animationObj, animation, 2)
            animationData[2]=animationData[2]-1
        else:
            callback= animationData[3]
            callbackObj= animationData[4]
            if callback!= None:
                if callbackObj ==None:
                    callback()
                else:
                    callback(callbackObj)
                    
            animations.remove(animationData)

def showStaticPath():
    global showPath
    showPath=True