""" 
Group project "Instrument Tracker" done during course
"Introduction to Signal and Image Processing" at Unibe

Authors :
    Leonard Barras
    Maxime Piergiovanni
"""


from skimage.io import imread
import tools as tls

Set = 'B'


if Set=='A':
    center = (348, 191, 0)
    ij = (348, 191)
    folder = './project_data/a/'
    imagename_first = 224#224
    imagename_last = 323
    filenamestart = '000'
else:
    center = (439, 272, 0)
    ij = (439, 272)
    folder = './project_data/b/'
    imagename_first = 1322
    imagename_last = 1418
    filenamestart = '00'

centerorgin = center
templatesize = 30 # edge size
searchingsize = 70 # edge size
Frame = imread(folder + filenamestart + str(imagename_first) + '.png')
index = 1

listCenters = []

for i in range (imagename_first, imagename_last+1):
    
    print(filenamestart + str(i) + '.png')
    
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
    template = tls.ImgCannyGaussian(template)
    SearchingZone = tls.ImgCannyGaussian(SearchingZone)
    
    try: #We may be drifting out of the frame here, in this case we can't update our center
        #fit template on next frame
        ij = tls.Match(SearchingZone, template, index, ij)#, pad_input = True) 
    
        center =(ij[0]+x+templatesize,ij[1]+y+templatesize,0)
        listCenters.append(("{0}{1}.png".format(filenamestart, i),center[0],center[1]))
    except ValueError:
        print("You seem to be out of bonds")
        listCenters.append(("{0}{1}.png".format(filenamestart, i),"null","null"))

    
    print(center)


tls.write_results(listCenters, "results{0}.txt".format(Set))