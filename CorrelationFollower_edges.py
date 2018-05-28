#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 09:29:14 2018

@author: barleo01
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import filters as flt
from skimage.io import imread
from skimage import feature
from skimage import exposure
from skimage.feature import match_template
from matplotlib.patches import Circle
import tools as tls

nbreimage = 50
Set = 'B'


if Set=='A':
    center = (348, 191, 0)
    ij = (348, 191)
    folder = './project_data/a/'
    imagename_first = 224#224
    imagename_last = 224+nbreimage#323
    filenamestart = '000'
else:
    center = (439, 272, 0)
    ij = (439, 272)
    folder = './project_data/b/'
    imagename_first = 1322
    imagename_last = 1322+nbreimage#1418
    filenamestart = '00'

centerorgin = center
templatesize = 30 # edge size
searchingsize = 70 # edge size
Frame = imread(folder + filenamestart + str(imagename_first) + '.png')
index = 1


for i in range (imagename_first, imagename_last):
    
    print(str(index) + ' : ' + filenamestart + str(i) + '.png')
    
    #newFrame = np.asarray(newFrame)
    
    #create template
    template = Frame[center[1]-templatesize:center[1]+templatesize,
                     center[0]-templatesize:center[0]+templatesize,:]
    
    y = center[1]-searchingsize
    x = center[0]-searchingsize

    
    #read a new frame
    Frame = imread(folder + filenamestart + str(i) + '.png')
    SearchingZone = Frame[center[1]-searchingsize:center[1]+searchingsize,
                          center[0]-searchingsize:center[0]+searchingsize,:]
    
    #processing
    template = tls.ImgProcessing(template, index)
    SearchingZone = tls.ImgProcessing(SearchingZone, index)
    
    #fit template on next frame
    ij = tls.Match(SearchingZone, template, index, ij)#, pad_input = True) 
 

    #i, j = ij[::-1]
    center =(ij[0]+x+templatesize,ij[1]+y+templatesize,0)
    
    #nextFrame[ij[0],ij[1]] = (255,0,0)
    print('Center: '+ str(center))
    fig,ax = plt.subplots(1)
    ax.imshow(Frame)
    ax.add_patch(Circle((center[0],center[1]),5, linestyle='solid', edgecolor='r', facecolor='none'))
    ax.add_patch(Circle((centerorgin[0],centerorgin[1]),5, linestyle='solid', edgecolor='b', facecolor='none'))
    plt.show()
    
    index += 1