# -*- coding: utf-8 -*-

#Anytime a file is loaded into the enviroment this is that code.
def fileSearch(file, libDir = None, exts = []):

    f1 = Filename.expandFrom(file)
    if f1.exists():
#       print "Local file"
        return f1

    for e in exts:
        f1.setExtension(e)
        if f1.exists():
            return f1
    if libDir is not None:
        f2 = Filename.expandFrom(g.pandaPath + "/" + libDir + "/" + file)
#        print "In library"
#        print f2
        if (f2.exists()):
            return f2
        for e in exts:
            f2.setExtension(e)
            if f2.exists():
                return f2
    return None


#Any time a CSV is loaded into the enviroment this is that code.
def loadCSV(file):


    cdict = {}
    fileLoader = open(file,  "r")
    contents = fileLoader.read().split("\n")
    for line in contents:
            data = line.split(",")
            key = data[0].strip()
            name = data[1].strip()
            value = data[2].strip()
            cdict[key][name]= value
    fileLoader.close()
    result = {}
    for key, dict in cdict.iteritems():
        result[key] = Control(dict)
        return result

    print "File " + fileName + " not found."
    exit()

def saveCSV(file, dict):

    result = []
    for key1, value1 in dict.iteritems():
     result.append(key1 + "," + value1 + "\n")
    saver = open(fileName,"file")
    saver.write(model.name+"\n")
    saver.writelines(result)
    saver.close()
    return