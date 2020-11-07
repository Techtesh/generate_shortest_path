# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 14:12:24 2020

@author: Hitesh
"""


from sys import maxsize 
from itertools import permutations
V = 4
 
# implementation of traveling Salesman Problem 
def travellingSalesmanProblem(graph, s=0): 
    c=0
    # store all vertex apart from source vertex 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
    
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize 
    next_permutation=permutations(vertex)
    for i in next_permutation:
        #print(i)
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        if min_path<current_pathweight:
            c=i
        min_path = min(min_path, current_pathweight) 
    #print(type(c))
    
    
    return c 
 
 
# Driver Code for testing algo only 
if __name__ == "__main__": 
 
    # matrix representation of graph 
    graph = [[0.0, 557.559,17.228,45.994],
          [557.559,0,540.366,512.649],
          [17.228,540.366,0.0,29.756],
          [5.994,512.649,29.756,0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
