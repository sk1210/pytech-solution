import cv2 , os
import numpy as np

#-------FUNCTIONS ------------------#
def detectFace(img):
    faces = faceCascade.detectMultiScale(img, 1.3 , minSize = (200,200) )
    x,y,w,h = faces[0]
    faceImg = img [ y:y+h , x:x+w ]
    return faceImg

# load trained XML file
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

# We will be using LBPH 
recognizerLBP = cv2.createEigenFaceRecognizer()
#recognizerEigenFace = cv2.createLBPHFaceRecognizer()
#recognizerFisher =  cv2.createFisherFaceRecognizer()

# load all face images
allImgPath = "imgs"
faceImgs = []
faceLabels = []

for label in os.listdir(allImgPath):
    imgPath = os.path.join(allImgPath,label)

    # load imgs of each subject

    for name in os.listdir(imgPath):
        img = cv2.imread(os.path.join(imgPath , name))
        gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray ,(0,0), fx = .2 ,fy = .2)
        faceImg =  detectFace(gray)
        faceImg = cv2.resize(faceImg ,(500,500))
        faceImgs.append(faceImg)
        faceLabels.append(int(label))
        #cv2.imshow("img" , faceImg )
        #cv2.waitKey(10)

# ------------------------------------Start Training-------------------------------------#

recognizerLBP.train(faceImgs, np.array(faceLabels))
#recognizerEigenFace.train(faceImgs, np.array(faceLabels))
#recognizerFisher.train(faceImgs, np.array(faceLabels))


recognizerLBP.save("trainedFacesLBP.xml")
#recognizerEigenFace.save("trainedFacesEigen.xml")
#recognizerFisher.save("trainedFacesFisher.xml")

print ("Training finished ")
