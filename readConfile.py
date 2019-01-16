def parse_File(filename):
    tmp = []
    fh = open(filename)
    line = fh.readline()
    flag = 0
    while line:
        if "tablename" in line and "__employee__" in line:
            count = 0
            flag  = 1
        if flag == 1:
            count += 1
            if count == 4 and "level" in line:
                value = line.split(r'"')[1]
                tmp.append(value)
        line = fh.readline()
    return tmp
 
 
if __name__ == '__main__':
    print parse_File('data.conf')