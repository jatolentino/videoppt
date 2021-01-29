import os
mydir='F:\Future MS\Scripts'
arr=[i for i in os.listdir(mydir) if i.endswith(".mp4")]
videoNamesPdf=[i.replace('.mp4', '.pdf') for i in arr]
print(arr)
print(len(arr))
print(arr[0])
print(mydir.split("\\")[-1])
print(videoNamesPdf)
