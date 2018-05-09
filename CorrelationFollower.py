#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 09:29:14 2018

@author: barleo01
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

startPointA = (348, 191)
folderA = './project_data/a/'
templatesize = 30

startPointB = (439, 272)
folderB = './project_data/b/'

center = startPointA

for i in range (224, 324):
    newFrame = imread(folderA + '000' + str(i) + '.png')
    #newFrame = np.asarray(newFrame)
    
    newFrame = newFrame[:10,0:100,:]