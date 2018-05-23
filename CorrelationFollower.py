#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 09:29:14 2018

@author: barleo01
"""

import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.feature import match_template
from matplotlib.patches import Circle
import tools as tls

Set = 'A'

if Set=='A':
    center = (348, 191, 0)
    folder = './project_data/a/'
    imagename_first = 224#224
    imagename_last = 323#323
    filenamestart = '000'
else:
    center = (439, 272, 0)
    folder = './project_data/b/'
    imagename_first = 1322
    imagename_last = 1418#1418
    filenamestart = '00'

centerorgin = center
templatesize = 20 # one edge
searchingzone = 70
Frame = imread(folder + filenamestart + str(imagename_first) + '.png')
index = 1

for i in range (imagename_first, imagename_last):
    
    print(index)
    index += 1
    #newFrame = np.asarray(newFrame)
    
    #create template
    template = Frame[center[1]-templatesize:center[1]+templatesize,
                        center[0]-templatesize:center[0]+templatesize,:]
    
    
    y = center[1]-searchingzone
    x = center[0]-searchingzone
    
    #read a new frame
    Frame = imread(folder + filenamestart + str(i) + '.png')
    SearchingZone = Frame[center[1]-searchingzone:center[1]+searchingzone,
                          center[0]-searchingzone:center[0]+searchingzone]
    
    #fit template on next frame
    match = match_template(SearchingZone, template)#, pad_input = True) 
    
    '''
    print('Template')
    plt.imshow(template)
    plt.show()
    
    print('SearchingZone')
    plt.imshow(SearchingZone)
    plt.show()
    
    print('Match')
    plt.imshow(match[:,:,0])
    plt.show()
    '''
    
    #new center of object calculation
    ij = np.unravel_index(np.argmax(match), match.shape)  
    #i, j = ij[::-1]
    center =(ij[0]+x+templatesize,ij[1]+y+templatesize,0)
    
    #nextFrame[ij[0],ij[1]] = (255,0,0)
    print('Center: '+ str(center))
    fig,ax = plt.subplots(1)
    ax.imshow(Frame)
    ax.add_patch(Circle((center[0],center[1]),5, linestyle='solid', edgecolor='r', facecolor='none'))
    ax.add_patch(Circle((centerorgin[0],centerorgin[1]),5, linestyle='solid', edgecolor='b', facecolor='none'))
    plt.show()