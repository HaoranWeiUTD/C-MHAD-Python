import os
import xlrd
import pandas
from matplotlib import pyplot as plt
import numpy as np
import pdb


dataset = "/home/haoran/actiondetection/Transition"
subject = 1

subdir = dataset+"/Subject"+str(subject)
LabelPath = xlrd.open_workbook(subdir+"/ActionOfInterestTraSubject"+str(subject)+".xlsx")


sheet = LabelPath.sheet_by_index(0)
min = 2
max = 3
for l in range(sheet.nrows-1): 
    val = sheet.cell_value(l+1, 3)-sheet.cell_value(l+1, 2)
    if val < min:
        min = val
    if val > max:
        max = val
print("The Minimum action duration of this Subject is: "+str(min)+" seconds")
print("The Maximum action duration of this Subject is: "+str(max)+" seconds")


Idirpath = subdir + "/InertialData/inertial_sub"+str(subject)+"_tr1.csv"
df = pandas.read_csv(Idirpath)
MissFrames = 6005-len(df.index)
df = df.iloc[2:,1:]
df = df.astype(float)
dfmean = df.mean(axis=0)
df = df.div(dfmean,axis=1)
df = df.to_numpy()
acc = pow((pow(df[:,0],2)+pow(df[:,1],2)+pow(df[:,2],2)),0.5)
gyr = pow((pow(df[:,3],2)+pow(df[:,4],2)+pow(df[:,5],2)),0.5)
acc = np.asarray(acc)
gyr = np.asarray(gyr)    
df = np.concatenate((df, acc[:, np.newaxis],gyr[:, np.newaxis]), axis=1)
df_normed = (df-df.min(axis=0)) / (df.max(axis=0)-df.min(axis=0))
print(df_normed)
plt.plot(df_normed)
plt.savefig('InertialSignal.png')