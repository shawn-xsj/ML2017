
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')


import cv2 as cv
import numpy as np
imageA = cv.imread("/home/xsj/project_our/ML2017/ML2017/hw0/Q2/data/lena.png")
imageB = cv.imread("/home/xsj/project_our/ML2017/ML2017/hw0/Q2/data/lena_modified.png")
src = cv.subtract(imageA,imageB)
img_zero = np.zeros_like(src)
img_zero[:,:,0]=255
img_zero[:,:,1]=255
img_zero[:,:,2]=255
img_add = cv.bitwise_xor(src,img_zero)


cv.imshow('src1',src)
cv.imshow('src2',img_zero)
cv.imshow('dst',img_add)
cv.waitKey(0)
cv.destoryAllWindows()



