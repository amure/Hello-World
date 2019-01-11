#!/usr/bin/env python3
import csv
import numpy as np
with open('duplicate_file.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]
print(rows) #输出所有数据
data=np.array(rows) #rows是数据类型是‘list',转化为数组类型好处理
print("out0=",type(data),data.shape)
print("out1=",data)
