import cv2 as cv
import numpy as np
import math
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,help="path to input image")
args = vars(ap.parse_args())
src = cv.imread(args["image"],0)
dst = cv.bitwise_not(src)
w, h= np.array(src.shape)
lines = cv.HoughLinesP(dst,1,np.pi/180,100,w/2,20)
size = np.array(lines.shape)

angle = 0;

if lines is not None:
	for i in range(0,len(lines)):
		l = lines[i][0]
		angle = angle + math.atan2(l[3]-l[1],l[2]-l[0])
		cv.line(src, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)

angle = angle*180/np.pi
print(angle/len(lines))
cv.imshow('src',src)
cv.imshow('test',dst)
cv.waitKey()