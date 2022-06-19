from turtle import color
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


mask = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(gray, gray, mask=mask)
cv.imshow('Masked', masked)


# GRayscale Histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


# Color Histogram
mask_color = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked_color = cv.bitwise_and(img, img, mask=mask_color)
cv.imshow('Masked Image', masked_color)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask_color, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)