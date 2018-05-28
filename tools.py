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
import skimage as sk
from matplotlib.patches import Circle
import tools as tls

from scipy.signal import convolve2d as conv2
from skimage.segmentation import slic
from skimage.exposure import equalize_hist, equalize_adapthist


def ImgSegmentation(img,index):
    segments = slic(img, n_segments=500)

    plt.imshow(segments)
    plt.show()
    print('debug')
    

def ImgProcessing(img, index):
    
    #img = equalize_adapthist(img)
    
    #red = img[:,:,0]
    #blue = img[:,:,1] 
    #green = img[:,:,2] 
    
    img = rgb2gray(img)
    #img = green
    #img = exposure.equalize_hist(img)
    
    # 1. FILTER
    #img = flt.gaussian(img, sigma=1.2)
    
    # CANNY EDGE DETECTION
    mask = feature.canny(img, sigma=1)#dtype=bool)    
    #mask = np.logical_or(mask, feature.canny(blue, sigma=1))
    #mask = np.logical_or(mask, feature.canny(green, sigma=1))
    #img = np.ones((img.shape[0],img.shape[1]))*255
    img[mask==False] = 0
    img[mask==True] = 255
    
    # 2. FILTER
    
    #filt = np.ones((5, 5)) / 25
    #img = conv2(img, filt, 'same')
    
    img = flt.gaussian(img, sigma=1)
    

    return img


def Match(Searchingzone, template, index, xy):
   
    ListCorr = []
    
    templatebinary = np.full((template.shape[0], template.shape[1]), False)
    templatebinary[template>0.1] = True
    template = templatebinary
    
    Searchingzonebinary = np.full((Searchingzone.shape[0], Searchingzone.shape[1]), False)
    Searchingzonebinary[Searchingzone>0.1] = True
    Searchingzone = Searchingzonebinary
    
    best_score = 0
    score = 0
    ij = (0,0)
    
    if index==30:
        print('debug')
       
    for i in range(int(template.shape[0]/2), int(Searchingzone.shape[0]-template.shape[0]/2)):
        for j in range(int(template.shape[0]/2), int(Searchingzone.shape[0]-template.shape[0]/2)):
            x_l = int(i-template.shape[0]/2)
            x_r = int(i+template.shape[0]/2)
            y_h = int(j-template.shape[1]/2)
            y_l = int(j+template.shape[1]/2)
           
            Searchwindow = Searchingzone[x_l:x_r,y_h:y_l]
    
            
            #----------------------------------------------------------
            # SCORE
            #----------------------------------------------------------
            '''
            match = Searchwindow&template
            score = np.sum(match.flatten()) #number of pixels
            sizeSearchwindow = np.sum(Searchwindow.flatten())
            #match[template==True and Corr==True] = True
            score = score - sizeSearchwindow/7
            '''
            diff = sk.img_as_ubyte(template)/255-(sk.img_as_ubyte(Searchwindow)/255)*1.5
            sum_template = diff[diff==1].size
            sum_window = diff[diff==-1.5].size
            sum_both = diff[diff==-0.5].size
            sum_none = diff[diff==0].size
            
            '''
            both = np.full((Searchwindow.shape[0], Searchwindow.shape[1]), False)
            mask = template & Searchingzone
            both[template==True] = True
            sum_both = both[both==True].size
            '''
            
            score = sum_both- 0.8 *sum_window
            #---------------------------------------------------------
            
            if score>=best_score:
                best_score = score
                ij = (i-int(template.shape[0]/2),j-int(template.shape[0]/2))
            #ListCorr.append(match)
            
    print('score: ' + str(best_score))
       
    if index>0:
       print('diff')
       plt.imshow(diff)
       plt.show()
    
    if best_score<100:
        return xy
    return ij

def Match_(Searchingzone, template, index):
    match = match_template(Searchingzone, template)
    #new center of object calculation
    ij = np.unravel_index(np.argmax(match), match.shape)
    
    return ij