import os
mydir='F:\Future MS\Scripts'
arr=[i for i in os.listdir(mydir) if i.endswith(".mp4")]
videoNamesPdf=[i.replace('.mp4', '.pdf') for i in arr]
