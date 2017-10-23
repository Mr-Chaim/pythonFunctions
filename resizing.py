import os
import cv2

def resizingFile(imgPath, width, height):

    img = cv2.read(imgPath)
    resizedPath = ((imgPath[:-4])+ '_' + str(width) + 'x' + str(height) + '.png')
    resizeImg = cv2.resize(img, [width,height], interpolation= cv2.INTER_AREA)
    cv2.imwrite(resizePath, resizeImg)

