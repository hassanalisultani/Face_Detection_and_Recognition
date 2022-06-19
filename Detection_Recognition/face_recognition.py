from cv2 import imread
import cv2 as cv
import numpy as np

haar_cascade = cv.CascadeClassifier('Detection_Recognition/haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('Detection_Recognition/face_trained.yml')

img = imread('Faces/val/elton_john/1.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person in Gray', gray)

# Detect the face in the image
faces_det = haar_cascade.detectMultiScale(gray, 1.1, 3)

for (x,y,w,h) in faces_det:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'{people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Person', img)

cv.waitKey(0)