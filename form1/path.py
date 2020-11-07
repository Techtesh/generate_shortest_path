# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 11:58:47 2020

@author: Hitesh
"""
from geopy import distance
import mlrose
import numpy as np
#import tsp
#from .tsp1 import main

newdata=[]
newdata2=[]
def pathfinder(data):
     print(data)   
     #print(len(data))
     for i in range (0,len(data)):
         currdata=[]
         for j in range(0,len(data)):
             temp1=list(data[i][2])
             temp2=list(data[j][2])
             temp1[0]=eval(temp1[0])
             temp1[1]=eval(temp1[1])
             temp2[0]=eval(temp2[0])
             temp2[1]=eval(temp2[1])
             d=distance.distance(temp1,temp2).km
             #print(temp1,temp2,d)
             temp3=data[i][0]
             temp4=data[j][0]
             print(temp3,temp4,d)
             currdata.append(d)
             newdata.append((temp3,temp4,d))
         newdata2.append(currdata)
     print(newdata)
     print("#"*25)
     print(newdata2)
     return newdata2
     #fitness_dists = mlrose.TravellingSales(distances = newdata)
     #print(fitness_dists)
