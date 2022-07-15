import numpy
import cv2 as RanzCam
cam = RanzCam.VideoCapture(0)
while cam.isOpened():
    rec, rs = cam.read()
    RanzCam.imshow("RanzCam", rs)