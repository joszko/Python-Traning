import cv2

# load image
#
# second parameter:
# 1 - load color image,
# 0 - load grayscale image,
# -1 - color image with alpha channel (transparency etc).
img = cv2.imread("galaxy.jpg",0)

# check image dimensions
# print(img.shape)

# resizing image with maintaining the aspect ratio
resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# display image in a window titled 'Galaxy'
cv2.imshow('Galaxy', resized_image)
# cv2.waitKey(0) - pressing any key will close the window
# cv2.waitKey(2000) - timer 2000 milliseconds (2 seconds)
cv2.waitKey(0)
# specifying what will happen after the key is pressed
cv2.destroyAllWindows()

# save resized image
cv2.imwrite('Galaxy_resized.jpg',resized_image)
