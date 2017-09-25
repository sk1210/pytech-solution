""" Simple face detection example using Haar Cascades """


import cv2

#load pretrained face detection cllassifier
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# load image
img  = cv2.imread("test_img.jpg")

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply face detection on grayscale image ,
# It returns a list of rectangle of each face
# (x,y) -> top Left corner of each Face
# (w,h) -> width and height of each Face
faces = face_cascade.detectMultiScale(gray,1.3,5)

# draw rectangle around each face on input image
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# Display Result
cv2.imshow("img",img)
k = cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()

# Visit -> www.pytech-solution.blogspot.com
# Code  - > githu
