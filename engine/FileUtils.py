# -*- coding: utf-8 -*-

import g
from panda3d.core import Filename
#Anytime a file is loaded into the enviroment this is that code.
#fileSearch has been tested
def fileSearch(file, libDir = None, exts = []):

    f1 = Filename.expandFrom(file)
    if f1.exists():
# print "Local file"
        return f1

    for e in exts:
        f1.setExtension(e)
        if f1.exists():
            return f1
    if libDir is not None:
        f2 = Filename.expandFrom(g.pandaPath + "/" + libDir + "/" + file)
# print "In library"
# print f2
        if f2 is not None:
            return f2
        for e in exts:
            f2.setExtension(e)
            if f2.exists():
                return f2
    return None


# Read a CSV file and return a matrix of strings
def loadCSV(file):
    fileLoader = open(file, "r")
    contents = fileLoader.read().split("\n")
    arr = []
    for line in contents:
        arr.append(csvUnquote(line))
    fileLoader.close()
    return arr

# Write a matrix of strings as a CSV
def saveCSV(file, arr):
    lines = []
    for l in arr:
        line = ""
        first = True
        for cell in l:
            if not first:
                line = line + ","
                first = False
            line = line + csvQuote(cell)
        lines.add(line + "\n")
    saver = open(file,"file")
    saver.writelines(lines)
    saver.close()
    return

# Write out a dictionary in CSV form
def saveDict(file, dict, types = {}):
    lines = []
    for k,v in dict.iteritems():
        if k in types:
            v = types[k].encode(v)
        lines.add([k, v])
    saveCSV(file, lines)

def loadDict(file, types={}, defaults = {}):
    arr = loadCSV(file)
    res = {}
    for l in arr:
        if len(l) == 2:
            key = l[0]
            val = l[1]
            if key in types:
                val = types[key].decode(val)
            res[key] = val
    for k,v in defaults:
        if not (k in res):
            res[k] = v
    return res



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

# Convert a line into a list of strings using commas to separate. Allow items to be quoted
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



#f = fileSearch("panda", "Models")
#if f is not None:
# print "success"
