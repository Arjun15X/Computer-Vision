import cv2
face_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex,ey,ew,eh) in eyes:    # w and h are width and height of the area scanned for positive presence
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(250,90,40),2)      # x y z RGB channels for pixel brightness
        cv2.line(img, (ex, ey), ((ex + ew, ey + eh)), (0, 255, 255), 1)  # draw cross
        cv2.line(img, (ex + ew, ey), ((ex, ey + eh)), (0, 255, 255), 1)
        roi_gray2 = gray[ey:ey+eh, ex:ex+ew]                       # enable gray scale filters
        roi_color2 = img[ey:ey+eh, ex:ex+ew]                       # define color version
        circles = cv2.HoughCircles(roi_gray2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=9)
        print("Set scan range")
        print("Eye Scanned")
        print("Pupil Response:Positive")
        try:
            for i in circles[0,1]:

                cv2.circle(roi_color2,(i[0],i[1]),i[2],(255,255,255),2)
                print("drawing circle")
                print("Set scan range")
                print(i)
                # draw the center of the circle
                cv2.circle(roi_color2,(i[0],i[1]),2,(255,255,255),3)
        except Exception as e:

         cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 30:
        break

cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
