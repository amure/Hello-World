#!/usr/bin/env python2
import os
import hashlib
xml = ''
def walk(path):
    global xml
    fl = os.listdir(path) # get what we have in the dir.
    for f in fl:
        if os.path.isdir(os.path.join(path,f)): # if is a dir.
            walk(os.path.join(path,f))
        else: # if is a file
            fp = open(os.path.join(path,f)) #open file. There is a big problem here. That is when you get a large file.
            c = fp.read() # get file content.
            m = hashlib.md5() # create a md5 object
            m.update(c) #encrypt the file
            xml += "<md5 name=\"%s\" md5=\"%s\" />\n" % (os.path.join(path,f),str(m.hexdigest())) # output to the md5 value to a string in xml format.
            fp.close() #close file
if __name__ == "__main__": 
    xml = ''
    walk(os.getcwd())
    print xml
