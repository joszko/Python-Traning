import cv2
import os

path = '.\\sample-images\\'
files = os.listdir(path)

for file in files:
    # cv2.imread requires full path to the file
    img = cv2.imread(path + file, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imwrite(path + file + '_resized.jpg', re)

