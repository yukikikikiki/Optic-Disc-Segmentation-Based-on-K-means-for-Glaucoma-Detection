from PIL import Image
from matplotlib.pyplot import *
from matplotlib.pyplot import show
from matplotlib.pyplot import imshow
from numpy import *
from scipy.cluster.vq import *
from scipy.misc import imresize

steps=1000
im =array(Image.open('./data/crop/0.jpg'))
mask = array(Image.open('./data/crop/0_mask.jpg'))
dx=int(im.shape[0]/steps)
dy=int(im.shape[1]/steps)

features=[]
for x in range(steps):
    for y in range(steps):
        R=mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,0])
        G=mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,1])
        B=mean(im[x*dx:(x+1)*dx,y*dy:(y+1)*dy,2])
        features.append([R,G,B])
features=array(features,'f')

centroids,variance=kmeans(features,2)
code, distance =vq(features,centroids)

codeim=code.reshape(steps,steps)


figure
suptitle('Figure 0')
subplot(1,2,1)
imshow(mask)
subplot(1,2,2)
imshow(codeim)


acc=0
count=0
rows,cols=codeim.shape 
for i in range(rows):
    for j in range(cols):
        if(mask[i,j] == codeim[i,j]):
            acc=acc+1
            count=count+1
        else:
            count=count+1

print('Acc: {:.6f}'.format(acc/count))

