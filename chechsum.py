#!/usr/bin/env python2
import hashlib,sys
def create_checksum(path):
    fp = open(path)
    checksum = hashlib.md5()
    while True:
        buffer = fp.read(8192)
        if not buffer:break
        checksum.update(buffer)
    fp.close()    
    checksum = checksum.digest()
    return checksum
if __name__ == '__main__':
        create_checksum(sys.argv[1])
