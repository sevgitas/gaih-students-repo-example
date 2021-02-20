# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 22:02:12 2021

@author: sevgi.tas
"""


import random as rnd       
a=[[0]*3 for i in range(3)]

for i in range(0,3):
    for j in range(0,3):
        a[i][j]=rnd.randint(1, 100)
for row in a:
  
      print(' '.join([str(x) for x in row]))