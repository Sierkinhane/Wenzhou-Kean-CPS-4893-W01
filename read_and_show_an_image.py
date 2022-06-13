import cv2

# read an image
image = cv2.imread("images/logo_cn.png")

# show the image
cv2.imshow('a window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()