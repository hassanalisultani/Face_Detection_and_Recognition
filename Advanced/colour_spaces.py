import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)


# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)


# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


# 'matplotlib' reads the image as RGB, while 'open cv' reads the image as BGR
# plt.imshow(img)
# plt.show()


# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


# After converting to RGB, 'matplotlib' will shows the actual image
# plt.imshow(rgb)
# plt.show()


# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)


# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)


# RGB to BGR
rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('RGB --> BGR', rgb_bgr)

cv.waitKey(0)