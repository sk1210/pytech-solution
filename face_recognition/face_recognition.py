import cv2 , os
import numpy as np

def detectFace(img):
    faces = faceCascade.detectMultiScale(img, 1.3 , minSize = (200,200) )
    x,y,w,h = faces[0]
    faceImg = img [ y:y+h , x:x+w ]
    faceImg = cv2.resize(faceImg ,(500,500))
    return faceImg

# load trained XML file
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

recognizerLBP = cv2.createEigenFaceRecognizer()
recognizerEigenFace = cv2.createLBPHFaceRecognizer()
recognizerFisher =  cv2.createFisherFaceRecognizer()

recognizerLBP.load("trainedFacesLBP.xml")
recognizerEigenFace.load("trainedFacesEigen.xml")
recognizerFisher.load("trainedFacesFisher.xml")

img = cv2.imread("test6.jpg")
gray = cv2.cvtColor(img  , cv2.COLOR_BGR2GRAY )
gray = cv2.resize(gray ,(0,0), fx = .2 ,fy = .2)


faceImg = detectFace(gray)
predLBP = recognizerLBP.predict(faceImg)
predEigen = recognizerEigenFace.predict(faceImg)
predFisher= recognizerFisher.predict(faceImg)

print "LBP RESULT : " ,predLBP
print "Eigen RESULT : " ,predEigen
print "Fisher RESULT : " ,predFisher


#cv2.destroyAllWindows()
