#pip install opencv-python
import cv2
from pathlib import Path
import os
#image = cv2.imread("untitled2.png", 0)
#count = cv2.countNonZero(image)
#print(count)
def blknes(myFrameImg) :
    """Percentage of blackness in an image
    1920*1080px full HD, by default frames are 1280*720px
    100%Black = 1280*720px
    0%Black = 0px"""
    imgSh = cv2.imread(myFrameImg)
    h, w, c= imgSh.shape # height, width, channel of image
    imageFr = cv2.imread(myFrameImg, 0)
    counterFr = cv2.countNonZero(imageFr)
    return -100*(counterFr-2073600)/2073600

mydir=Path(r'F:\Future MS\Scripts\New\New folder')
imgName=[i for i in os.listdir(mydir) if i.endswith(".png")]

print(imgName)

print([blknes(x) for x in imgName])
print(all(blknes(x) > 70 for x in imgName))
