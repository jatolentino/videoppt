#pip install opencv-python
import cv2
from pathlib import Path
import os

def blknes(myFrameImg) :
    """Percentage of blackness in an image
    100%Black = 2073600px
    100%Black = 0px"""
    imageFr = cv2.imread(myFrameImg, 0)
    counterFr = cv2.countNonZero(imageFr)
    return -100*(counterFr-2073600)/2073600

mydir=Path(r'F:\Future MS\Scripts\New\New folder')
imgName=[i for i in os.listdir(mydir) if i.endswith(".png")]

print(imgName)

print([blknes(x) for x in imgName])
print(all(blknes(x) > 70 for x in imgName))
