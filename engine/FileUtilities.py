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

# Add string quotes when the string contains a comma
def csvQuote(s):
    if ',' in s:
        r = '"'
        for c in s:
            if c == '"':
                r = r + '""'
            else:
                r = r + c
        r = r + '"'
        return r
    return s

# Convert a line into a list of strings using commas to separate.  Allow items to be quoted
# using Microsoft CSV rules
def csvUnquote(s):
    r = []
    item = ""
    quoted = False
    q2 = False
    atStart = True
    for c in s:
        if q2:
            q2 = False
            if c == '"':
                item = item + '"'
            elif c == ",":
                r.append(item)
                item = ""
                atStart = True
                quoted = False
            else:
                quoted = False
        elif quoted:
            if c == '"':
                q2 = True
            else:
                item = item + c
        else:
            if c == ',':
                r.append(item)
                item = ""
                atStart = True
            elif atStart:
                atStart = False
                if c == '"':
                    quoted = True
                else:
                    item = item + c
            else:
                item = item + c
    if item != "" or atStart:
        r.append(item)
    return r