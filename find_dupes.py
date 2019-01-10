#!/usr/bin/env python2
from checksum import create_checksum
from diskwalk import diskwalk
from os.path import getsize
import sys

def findDupes(path):
    record = {}
    dup = {}
    d = diskwalk(path)
    files = d.paths()
    for file in files:
        compound_key = (getsize(file),create_checksum(file))
        if compound_key in record:
            dup[file] = record[compound_key]
        else:
            record[compound_key]=file
    return dup

if __name__ == '__main__':
    for file in findDupes(sys.argv[1]).items():
        print "The duplicate file is %s" %file[0]
        print "The original file is %s\n" %file[1]
