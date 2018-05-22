# -*- coding: utf-8 -*-
"""
Created on Thu May 17 08:55:09 2018

@author: maxpi
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imsave



def compute_mean_std(images):
    mean = np.mean(images,0)
    sig = np.std(images, 0)
    return mean, sig[:,:,0], sig[:,:,1], sig[:,:,2]

path = "./project_data/a/"
#read from path all images
images = [plt.imread(path + file) for file in os.listdir(path)]

mean, r, g, b = compute_mean_std(images)

sub_images = [image - mean for image in images]

if not os.path.isdir('./project_data/res'):
    os.mkdir('./project_data/res')

for i, im in enumerate(sub_images):
    imsave("./project_data/res/{0}.png".format(i), im)

imsave("./project_data/res/mean.png", mean)


plt.subplot('111')
plt.imshow(sub_images[0], vmin=0, vmax=1)
#plt.subplot('222')
#plt.imshow(r)
#plt.subplot('223')
#plt.imshow(g)
#plt.subplot('224')
plt.show()