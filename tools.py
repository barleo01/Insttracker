""" 
Contains functions that are mainly used in all exercises of HW2
"""

# Imports
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


def ImgProcessing(img, index):
    red = img[:,:,0]
    blue = img[:,:,1] 
    green = img[:,:,2] 
    
    img = rgb2gray(img)
    #img = green
    #img = exposure.equalize_hist(img)
    
    # 1. FILTER
    #img = flt.gaussian(img)
    
    # CANNY EDGE DETECTION
    mask = feature.canny(img, sigma=0.3)#dtype=bool)    
    img = np.ones((img.shape[0],img.shape[1]))*255
    img[mask==True] = 0
    
    # 2. FILTER
    img = flt.gaussian(img, sigma=1)
    

    return img


def Match(Searchingzone, template):
    match = match_template(Searchingzone, template)
    #new center of object calculation
    ij = np.unravel_index(np.argmax(match), match.shape)
    
    #corr = template*template
      


    
    return ij