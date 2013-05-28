
#~Kendric 5-29-08
from Panda import *

import os.path
import g

# Rather than create a GUI for these we'll just edit
# the following lines to select the model and file
##############################
#fileName = 'c:/pose.csv'
fileName = g.pandaPath + '/Scripts/sonic.csv'
model = sonic()
##############################

# DLight(HPR = HPR(time, .3,  0))

# Python (non-reactive) variables
jointList = []   # List of joint names
jointDict = {}   # initialize the pose to all 0's
poseList = ["default"]
poseDict = {"default":jointDict}
for i,j in model.d.joints:
    jointDict[i] = SHPR(0,0,0)
    jointList.append(i)

# Reactive variables
pose = var(Control(jointDict))
lastPose = var(Control(jointDict))
selected = var(jointList[0])  # Start with the first joint in the list
poseName = var("default")     # Always have a pose named default
lastPoseName = var("default")
msg = var("No pose file loaded")  # A general message

# GUI elements

# Sliders to set H, P, and R
hslider = Slider(position = P2(1,.9), min=-pi,max = pi, init = 0, label = "H")
pslider = Slider(position = P2(1,.8), min=-pi,max = pi, init = 0, label = "P")
rslider = Slider(position = P2(1,.7), min=-pi,max = pi, init = 0, label = "R")

# Sliders to select the height and size of the displayed model
lightangle = slider(position = P2(1,.5), min=0, max=2*pi, init = 0, label = "Light")
zoom = Slider(position = P2(1,.4),min=0,max=10,init=5, label = "Zoom")

# Messages
text(msg, position = P2(-1, .9))


# A pulldown to select the joint
jointMenu = menu(jointList, position=P2(-1.1,.7), size = .5)
text("Joint: ", position = P2(-1.25, .7))
# Pose selection / entry
poseMenu = Menu(poseList, position=P2(-1.1,.6), size = .5)
text("New pose: ", position = P2(-1.2, .5))
poseBox = textBox(position=P2(-.9,.5))

# Second pose selection

poseInterp = Slider(position = P2(-1.1,.3), min=0,max = 1, init = 0)
text(poseName, position = P2(-1.2, .2))
text(lastPoseName, position = P2(-1, .2))

# Buttons to load / save the file containing the poses
saveButton = button("Save File", position = P2(-1.1, .0), size = .5)
loadButton = button("Load File", position = P2(-1.1, -.1), size = .5)

world.color = choose(poseInterp.value == 0, darkGray, gray)

def save(w, x):
    d = savePose()
    result = []
    for poseName,pose in poseDict.iteritems():
        for joint,hpr in pose.iteritems():
            result.append(poseName + "," + joint + "," + str(hpr.h) + ", "
                            + str(hpr.p) + ", " + str(hpr.r) + "\n")
    saver = open(fileName,"w")
    saver.write(model.name+"\n")
    saver.writelines(result)
    saver.close()
    msg.set("Pose " + fileName + " written to disk")
    return

def load(w, x):
    msg.set("Loading poses from " + fileName)
    loadedJoints = {}
    loadedPoses = {}
    for j in jointList:
        loadedJoints[j] = SHPR(0,0,0)  # Default joint positions
    if os.path.isfile(fileName):
        fileLoader = open(fileName,  "r")
        contents = fileLoader.read().split("\n")
        if contents[0] != model.name:
            msg.set("WARNING! File for a different model!")
        for line in contents[1:]:
            data = line.split(",")
            if len(data) >= 5:
                #if you accidentally hit load, and the file hasn't been saved with the current model
                #It'll EXPLODE VIOLENTLY!
                if data[1].strip() in jointList:
                    poseName = data[0].strip()
                    jointName = data[1].strip()
                    jointHpr = SHPR(float(data[2].lstrip("(")),  float(data[3]),  float(data[4].rstrip(")")))
                    print jointName + " = " + str(jointHpr)
                    if poseName not in loadedPoses:
                        loadedPoses[poseName] = {}
                    loadedPoses[poseName][jointName] = jointHpr
                    if poseName not in poseList:
                        poseMenu.addItem(poseName)
        fileLoader.close()
    pose.set(Control(loadedJoints))
    controlJoint(selected.get(), loadedJoints)
    global poseDict
    poseDict = loadedPoses
    return

def newJoint(w,joint):
    d = savePose()
    controlJoint(joint, d)
    selected.set(joint)

def controlJoint(joint, d):
    newHPR = d[joint]
    hslider.set(newHPR.h)
    pslider.set(newHPR.p)
    rslider.set(newHPR.r)
    d[joint] = SHPR(0,0,0)  # The HPR of the selected joint is always (0,0,0)
    pose.set(Control(d))

def savePose():
    d = pose.get().dict.copy()
    oldJoint = selected.get()
    d[oldJoint] = SHPR(hslider.value.now(), pslider.value.now(), rslider.value.now())
    print oldJoint, d[oldJoint]
    return d

controlJoint(jointList[0], jointDict)

angle = getX(lbuttonPull)*pi+pi
pitch = getX(rbuttonPull)*pi
camera.position = P3(sin(angle)*zoom.value, cos(angle)*zoom.value,-getY(lbuttonPull))
camera.hpr = HPR(-angle+pi,0,0)
directionalLight(color = white, hpr = HPR(lightangle, 0 ,0))
ambientLight(color = color(.5, .5, .5))

pose1 = addVal(selected, HPR(hslider.value, pslider.value, rslider.value), pose)
model.control = choose(poseName == lastPoseName,
                    pose1,
                    lerp(poseInterp.value, pose1, lastPose))
model.hpr = HPR(0, pitch, 0)
react(jointMenu, newJoint)
react(saveButton, save)
react(loadButton, load)




def storePose(w,thisPose):
    #thisPose = poseBox.text.now()
    # print "saving pose " + thisPose
    if thisPose not in poseList:
        #poseList.append(thisPose)
        poseMenu.addItem(thisPose)
        # print poseList
    poseDict[thisPose] = savePose()
    poseDict[poseName.get()] = poseDict[thisPose]
    lastPose.set(Control(poseDict[thisPose]))
    poseName.set(thisPose)

def retrievePose(w,thisPose):
    #thisPose = poseMenu.select
    storePose(w, poseName.get())
    # print "loading pose " + thisPose
    if thisPose not in poseList:
        msg.set("pose not found")
        return
    jointDict = poseDict[thisPose]
    lastPose.set(pose.get())
    pose.set(Control(jointDict))
    controlJoint(selected.get(), jointDict)
    lastPoseName.set(poseName.get())
    poseName.set(thisPose)
    poseInterp.set(0)  # to avoid accidentally editing a pose thats
                       # an interpolant

react(poseBox, storePose)
react(poseMenu.select, retrievePose)

start()