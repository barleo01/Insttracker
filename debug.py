#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:33:01 2018

@author: guy
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

nbreimage = 34

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
    imagename_last = 1322+nbreimage#1418
    filenamestart = '00'


for i in range(imagename_first, imagename_last):
    print(filenamestart + str(i) + '.png')
    Frame = imread(folder + filenamestart + str(i) + '.png')

    
    img = tls.ImgProcessing(Frame,1)

    print('SearchingZone')
    plt.imshow(img)
    plt.show()