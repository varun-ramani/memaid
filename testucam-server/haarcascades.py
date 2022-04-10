import cv2
# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)
cv2.imshow("Faces found", img)
cv2.waitKey(0)