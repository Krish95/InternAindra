import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
#Using HAAR Cascade 
cascPath = "haarcascade_frontalface_alt.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
image_cp = cv2.imread(imagePath)
#Convert to gray scale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=6,
    minSize=(20,20)
)
#Blur the background and detect all faces
if len(faces)!=0:
    image_cp=cv2.GaussianBlur(image_cp,(23,23),30)
    for f in faces:
        x,y,w,h = f
        sub_face = image[y:y+h, x:x+w]
        image_cp[y:y+h, x:x+w] = sub_face
        
    cv2.imshow("Detected face", image_cp)
    cv2.waitKey(0)

