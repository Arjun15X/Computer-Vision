import numpy as np  # Import Numpy
import cv2          # Import Open CV

# Import the cascades

face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')

#import the image you want to run the code on

img = cv2.imread('C:\\Users\\Arjun Sen\\Desktop\\subsurface.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)


for (x,y,w,h) in faces:                         # Scan for faces

    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex,ey,ew,eh) in eyes:                  # Scan for eyes in the faces detected
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

cv2.imshow('img',img)                           # Display a new window with rectangles drawn on eyes and faces
cv2.waitKey(0)
cv2.destroyAllWindows()