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

startPointA = (348, 191, 0)
folderA = './project_data/a/'

templatesize = 15 # one edge
searchingzone = 50


#imageoutput = './img_output/a/'

startPointB = (439, 272, 0)
folderB = './project_data/b/'

center = startPointA

imagename_first = 224#224
imagename_last = 323#323

Frame = imread(folderA + '000' + str(imagename_first) + '.png')

for i in range (imagename_first, imagename_last):
    
    #newFrame = np.asarray(newFrame)
    
    #create template
    template = Frame[center[0]-templatesize:center[0]+templatesize,
                        center[1]-templatesize:center[1]+templatesize,:]
    
    y = center[1]-searchingzone
    x = center[0]-searchingzone
    
    Frame = imread(folderA + '000' + str(i+1) + '.png')
    
    '''
    print((folderA + '000' + str(i+1) + '.png'))
    plt.imshow(Frame)
    plt.show()
    '''
    
    #fit template on next frame
    match = match_template(Frame[center[0]-searchingzone:center[0]+searchingzone,center[1]-searchingzone:center[1]+searchingzone,:], template)#, pad_input = True) 
    
    #new center of object calculation
    ij = np.unravel_index(np.argmax(match), match.shape)  
    center =(ij[0]+x+templatesize,ij[1]+y+templatesize,0)
    
    #nextFrame[ij[0],ij[1]] = (255,0,0)
    print(center)
    fig,ax = plt.subplots(1)
    ax.imshow(Frame)
    ax.add_patch(Circle((center[0],center[1]),5, linestyle='solid', edgecolor='r', facecolor='none'))
    plt.show()