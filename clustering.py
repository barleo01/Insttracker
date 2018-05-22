"""
Given a point in an image and a starting point, 
returns the cluster in which starting point belong.

@author: Maxime Piergiovanni
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

startPointA = (348, 191, 0)
folderA = './project_data/a/'

img = np.asarray(plt.imread(folderA + '000224.png'))

#Adding a red rectangle
ax = plt.subplot('111')
h, w = 10,10
rect = plt.Rectangle((startPointA[0]-w/2,startPointA[1]-h/2), w, h, edgecolor = 'r', facecolor='none')
ax.add_patch(rect)

#putting numpy array in shape so that x,y is in it
data = np.copy(img)
h,w,_ = np.shape(img)

indices = np.reshape([(i,j) for i in range(h) for j in range(w)],(h,w,2))

data = np.concatenate((data, indices), axis = 2)
print(np.linalg.norm(data[363,197] - data[373,202]))
data = np.reshape(data, (h*w,5))
print(np.shape(data))

#segmentation
db = DBSCAN(eps=30).fit(data)
labels = np.reshape(db.labels_, (h,w))

plt.imshow(labels)
plt.show()

