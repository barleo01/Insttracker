"""
Given a point in an image and a starting point, 
returns the cluster in which starting point belong.

@author: Maxime Piergiovanni
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.cluster import KMeans


startPointA = (348, 191)
folderA = './project_data/a/'
templatesize = 30 # edge size


startPointA = (432, 177)

#img = np.asarray(plt.imread(folderA + '000224.png'))
img = np.asarray(plt.imread(folderA + '000283.png'))

template = img[startPointA[1] - templatesize:startPointA[1] + templatesize, 
               startPointA[0] - templatesize:startPointA[0] + templatesize, :]

def showKMeans(img):
    #putting numpy array in shape so that x,y is in it
    data = np.copy(img)
    h,w,_ = np.shape(img)
      
    data = np.reshape(data,(h*w,3))
    #segmentation
    kmeans = KMeans(n_clusters = 2).fit(data) 
    #db = DBSCAN(eps=30).fit(data)
    labels = np.reshape(kmeans.labels_, (h,w))
    #mask that only sets only pixels of same cluster as point
    clusterFilter = np.vectorize( lambda x: 1. if x == labels[h//2, w//2] else 0.)
    mask = clusterFilter(labels)
    plt.subplot('131')
    plt.imshow(img)
    plt.subplot('132')
    plt.imshow(labels, cmap='gray')
    plt.subplot('133')
    plt.imshow(mask, cmap='gray')
    plt.show()
    
def maskKMeans(img):
    #putting numpy array in shape so that x,y is in it
    data = np.copy(img)
    h,w,_ = np.shape(img)
      
    data = np.reshape(data,(h*w,3))
    #segmentation
    kmeans = KMeans(n_clusters = 2).fit(data) 
    #db = DBSCAN(eps=30).fit(data)
    labels = np.reshape(kmeans.labels_, (h,w))
    #mask that only sets only pixels of same cluster as point
    clusterFilter = np.vectorize( lambda x: 1. if x == labels[h//2, w//2] else 0.)
    mask = clusterFilter(labels)
    return mask
    
showKMeans(template)
