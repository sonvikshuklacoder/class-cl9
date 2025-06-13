from processing import *

'''
################
Display Object
################

# To display the object
# This function will take three parameter
    1) Object
    2) image or list of images <optional>
    3) speed <optional>

display(object, image / animation)

# return. :  None
-------------------------------------------------------------------------------------
'''
def display(obj, animation =[], speed=1):

    if type(animation) == list:
        if len(animation) == 0:
            rect(obj["x"], obj["y"], obj["w"], obj["h"])
        else:
            index = 0
            if "counter" in obj:
                obj["counter"]  = obj["counter"] +  speed * 0.1
                index = int((obj["counter"]) % len(animation))
            else:
                obj["counter"] = 0

            image(animation[index], obj["x"], obj["y"], obj["w"], obj["h"])

    else:
        image(animation, obj["x"], obj["y"], obj["w"], obj["h"])


#-------------------------------------------------------------------------------------

'''
################
Load Animation
################

# To load multiple images
loadAnimation(imagesList)

# return : list of loaded images
-------------------------------------------------------------------------------------
'''

def loadAnimation(imagesList):
    animationList = []
    for image in imagesList:
        animationList.append(loadImage(image))
    return animationList


#-------------------------------------------------------------------------------------


'''
#######################
Check Touching With Objects
#######################

# To detect the touching between two objects
# This function will take two parameters objectA and objectB

isTouching(objectA, objectB)

# return : True or False
-------------------------------------------------------------------------------------
'''

def isTouching(objectA, objectB):

    if(objectA["x"] < objectB["x"] + objectB["w"] and
       objectA["x"] + objectA["w"] > objectB["x"] and
       objectA["y"] < objectB["y"] + objectB["h"] and
       objectA["h"] + objectA["y"] > objectB["y"]):
        return True

    return False

#-------------------------------------------------------------------------------------


'''
#######################
Collision With objects
#######################

# To detect the collision between two objects
# This function will take two parameters objectA and objectB

collide(objectA, objectB)

# return : True or False
-------------------------------------------------------------------------------------
'''

def collide(objectA, objectB):
    collided = False
    newobjectA = getNewObjectX(objectA)
    newobjectB = getNewObjectX(objectB)

    if isTouching(newobjectA, newobjectB):
        objectA["velX"] =0
        objectB["velX"] =0
        collided = True

    newobjectA = getNewObjectY(objectA)
    newobjectB = getNewObjectY(objectB)

    if isTouching(newobjectA, newobjectB):
        objectA["velY"] =0
        objectB["velY"] =0
        collided = True

    return collided

def getNewObjectX(obj):
    newObject = {"x": obj["x"] + obj["velX"], "y": obj["y"] ,"w": obj["w"], "h": obj["h"]}
    return newObject

def getNewObjectY(obj):
    newObject = {"x": obj["x"], "y": obj["y"] + obj["velY"] ,"w": obj["w"], "h": obj["h"]}
    return newObject


#-------------------------------------------------------------------------------------

