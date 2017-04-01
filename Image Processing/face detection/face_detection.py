import cv2

face_cascade = cv2.CascadeClassifier('./Files/haarcascade_frontalface_default.xml')

img = cv2.imread('./files/news.jpg')

# face detection is working better in grayscale,
# so we're creating a new variable with the image
# converted to gray
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detecting the face
faces = face_cascade.detectMultiScale(gray_img,
                                      scaleFactor=1.1,
                                      minNeighbors=5)

# for the parameters in the faces variable
# drawing a rectangle around detected face
for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow('face',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()