import g

from Control import *
from StaticNumerics import *
from Interp import *
from Signal import *
import os.path

scriptColors = {
"black": color24(0,0,0),
"blue": color24(0,0,255),
"red": color24(255,0, 0),
"green": color24(0,255,0),
"darkBlue": color24(0,0,139),
"gray": color24(128, 128, 128),
"lightGray": color24(200, 200, 200),
"darkGray": color24(60, 60, 60),
"darkGreen": color24(0,100,0),
"darkRed": color24(139,0,0),
"white": color24(255,255,255),
"yellow": color24(255, 255, 0),
"gold": color24(255,215,0),
"silver": color24(192,192,192),
"navyBlue": color24(0,0,128),
"purple": color24(128,0,128),
"brown": color24(165,42,42)
}
def loadPoseFile(fileName):
    poses = {}
    #should use the g.pandaPath ? -Michael reed s10
    file = findCSV(fileName)
    if file is not None:
        fileLoader = open(file,  "r")
        contents = fileLoader.read().split("\n")
        for line in contents[1:]:
            data = line.split(",")
            if len(data) >= 5:
                    poseName = data[0].strip()
                    jointName = data[1].strip()
                    jointHpr = SHPR(float(data[2].lstrip("(")),  float(data[3]),  float(data[4].rstrip(")")))
                    if not poses.has_key(poseName):
                        poses[poseName] = {}
                    poses[poseName][jointName] = jointHpr
        fileLoader.close()
        result = {}
        for pose, dict in poses.iteritems():
            result[pose] = Control(dict)
        return result

    print "File " + fileName + " not found."
    exit()

def loadScript(fileName):
    f = findCSV(fileName)

    interpolants = {}
    if f is not None:
        fileLoader = open(f,  "r")
        contents = fileLoader.read().split("\n")
        columnNames = contents[0].split(",")
        poseFiles={}
        types = contents[1].split(",")
        for i in range(len(types)):
            file = types[i].split(" ")
            if len(file) > 1 and columnNames[i] is not "":
              poseFiles[i] = file[1].strip()
              # print "Using pose file " + poseFiles[i]
            else:
              poseFiles[i] = ""
        poses={}
        timings = {}
        for name in contents[0].split(",")[1:]:
            timings[name.strip()] = 0
        for i in range(1, len(types)):
          if poseFiles[i] is not "":
                # print "Loaded pose file " + poseFiles[i]
                poses[i] = loadPoseFile(poseFiles[i])           # load the file
                # print "Poses Loaded: "
                #for k in poses[i].keys():
                #  print k
        for line in contents[2:]:
            data = line.split(",")
            for i in range(1, len(data)):
                type = types[i].strip()
                columnName = columnNames[i].strip()
                time = float(data[0].strip())
                eventName = data[i].strip()
                if eventName != "":
                    if columnName not in interpolants:
                        if type == "Number":
                            interpolants[columnName] = atS(float(eventName))
                        elif type == "HPR":
                            nums = eventName.strip("\"").split(" ")
                            val = SHPR(float(nums[0]),float(nums[1]),float(nums[2]))
                            interpolants[columnName] = atS(val)
                        elif type == "P3":
                            nums = eventName.strip("\"").split(" ")
                            val = SP3(float(nums[0]),float(nums[1]),float(nums[2]))
                            interpolants[columnName] = atS(val)
                        elif type == "P2":
                            nums = eventName.strip("\"").split(" ")
                            val = SP2(float(nums[0]),float(nums[1]))
                            interpolants[columnName] = atS(val)    
                        elif type.split(" ")[0] == "Pose":
                            if poses[i].has_key(eventName):
                              interpolants[columnName] = atS(poses[i][eventName])
                            else:
                              print "Unknown pose: "+eventName
                              print "Available Poses:"
                              for k in poses[i].keys():
                                print k
                              exit()
                        elif type == "Color":
                            interpolants[columnName] = atS(scriptColors[eventName])
                        elif type == "Event":
                            interpolants[columnName] = []
                    if type == "Number":
                        interpolants[columnName] = interpolants[columnName] + toS(time-timings[columnName],float(eventName))
                    elif type == "P3":
                        nums = eventName.strip("\"").split(" ")
                        val = SP3(float(nums[0]),float(nums[1]),float(nums[2]))
                        interpolants[columnName] = interpolants[columnName] + toS(time-timings[columnName],val)
                    elif type == "HPR":
                        nums = eventName.strip("\"").split(" ")
                        val = SHPR(float(nums[0]),float(nums[1]),float(nums[2]))
                        interpolants[columnName] = interpolants[columnName] + toS(time-timings[columnName],val)
                    elif type == "P2":
                        nums = eventName.strip("\"").split(" ")
                        val = SP2(float(nums[0]),float(nums[1]),)
                        interpolants[columnName] = interpolants[columnName] + toS(time-timings[columnName],val)
                    elif type.split(" ")[0] == "Pose":
                        interpolants[columnName] = interpolants[columnName] + toS(time-timings[columnName],poses[i][eventName])
                    elif type == "Color":
                        interpolants[columnName] = interpolants[columnName] + toS(time-timings[columnName], scriptColors[eventName])
                    elif type == "Event":
                        interpolants[columnName].append((time, eventName))
                    timings[columnName] = time
        fileLoader.close()
        for i in range(len(types)):
            if types[i] == "Event":
                interpolants[columnNames[i]] = events(interpolants[columnNames[i]])
        return interpolants
    else:
        print "File " + fileName + " not found."
    exit()

def findCSV(file):
    f = Filename.expandFrom(file)
    if (f.exists()):
        # print "Local file: " + str(f)
        return f.toOsSpecific()
    f = Filename.expandFrom(g.pandaPath + "/Scripts/" + file)
    if (f.exists()):
        # print "Loaded from library:" + str(f)
        # print f.toOsSpecific()
        return f.toOsSpecific()
    print "CSV " + file + " not found."
    return None