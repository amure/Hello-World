#!/usr/bin/env python3
# coding:utf-8
import pandas as pd
import os
import numpy as np
trainFile = "duplicate_file.csv" ##python3.6版本可读取，但是有的不行，
pwd = os.getcwd()
os.chdir(os.path.dirname(trainFile))
trainData = pd.read_csv(os.path.basename(trainFile))
os.chdir(pwd)
print(trainData) #输出数据
data=trainData.iloc[0:892,0:12] #读取所有数据
print("------------------out",data)
#pandas数据格式为DataFrame,转化为numpy数组格式，方便处理
print (data.as_matrix(columns=None))
print(data.shape)