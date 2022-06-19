from scipy.misc import face
import cv2 as cv
import numpy as np

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('Detection_Recognition/haar_face.xml')

faces_det = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f' Number of Faces in the image: {len(faces_det)}')

for (x,y,w,h) in faces_det:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Deteted Faces', img)


cv.waitKey(0)