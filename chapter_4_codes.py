#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:33:06 2019

@author: jahid
"""
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
np.savetxt('newFile.csv',a,delimiter=',')
b=np.genfromtxt('newFile.csv',delimiter=',')
