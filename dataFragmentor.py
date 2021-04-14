import sys
import os
import numpy as np
from PIL import Image

class DataFragmentor:
    def __init__(self, imgPath, grid, outPath="croppedImage"):
        self.img = Image.open(imgPath)
        self.gridShape = grid
        self.outPath = outPath
    
    def sliceImg(self):
        if not os.path.exists(self.outPath):
            os.makedirs(self.outPath)
        imgWidth, imgHeight = self.img.size
        width = int(imgWidth / self.gridShape[0])
        height = int(imgHeight / self.gridShape[1])
        for i in range(0,self.gridShape[0]):
            r = i * width
            for j in range(0,self.gridShape[1]):
                c = j * height
                box = (r, c, r+width, c+height)
                cropped = self.img.crop(box)
                try:
                    outputPath = "{}/C{}_R{}.jpg".format(self.outPath, i, j)
                    cropped.save(outputPath)
                except:
                    pass


if __name__ == "__main__":
    filePath = None
    grid = (3,3)
    if len(sys.argv) == 2:
        filePath = sys.argv[1]
    elif len(sys.argv) == 4:
        filePath = sys.argv[1]
        grid = (sys.argv[2], sys.argv[3])
    else:
        print("Invalid arguments!")
        pass

    dataFrag = DataFragmentor(filePath, grid)
    dataFrag.sliceImg()
    print("Slicing complete")
