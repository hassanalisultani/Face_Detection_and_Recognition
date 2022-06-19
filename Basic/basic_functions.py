import cv2 as cv
import numpy as np

# Rescaling Function
def rescaleFrame(frame, scale=0.75):
    # Works for Images, Videos & Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Reading Image
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

img_resized = rescaleFrame(img, scale=0.5)    # (1) for resized Image
cv.imshow('Resized Image', img_resized)    # (2) for resized Image

cv.waitKey(0)

# Reading Video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    if isTrue:
        frame_resized = rescaleFrame(frame)     # (1) for resized video
        cv.imshow('Dog', frame)
        cv.imshow('Video Resized', frame_resized)   # (2) for resized video
        if cv.waitKey(20) & 0xFF==ord('d'):
            break
    else:
        break

capture.release()
cv.destroyAllWindows()

# Draw
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[0:blank.shape[1]//2, 0:blank.shape[0]//2] = 0,0,255 # Red Box

blank[0:blank.shape[1]//2, blank.shape[0]//2:blank.shape[0]] = 255,0,0 # Blue Box

blank[blank.shape[1]//2:blank.shape[1], 0:blank.shape[0]//2] = 255,255,255 # White Box

blank[blank.shape[1]//2:blank.shape[1], blank.shape[0]//2:blank.shape[0]] = 0,255,0 # Green Box

cv.imshow('Colors & Shapes', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (blank.shape[1]//4, blank.shape[0]//4), (blank.shape[1]*3//4, blank.shape[0]*3//4), (0,0,0), thickness=5)
cv.imshow('Colors & Shapes', blank)

# 3. Draw a Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//6, (125,125,125), thickness=-1)
# Border for Circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//6, (0,0,0), thickness=3)
cv.imshow('Colors & Shapes', blank)

# 4. Draw Lines
cv.line(blank, (0, blank.shape[0]//2), (blank.shape[1]//2, blank.shape[0]), (30,30,30), thickness=5)
cv.line(blank, (blank.shape[1]//2, blank.shape[0]), (blank.shape[1], blank.shape[0]//2), (50,50,50), thickness=5)
cv.imshow('Colors & Shapes', blank)

# 5. Write Text
cv.putText(blank, 'HAFIZ HASSAN', (blank.shape[1]//4, blank.shape[0]//6), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), thickness=3)
cv.imshow('Colors & Shapes', blank)

cv.waitKey(0)