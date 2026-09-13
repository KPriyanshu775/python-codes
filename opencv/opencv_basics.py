import cv2

print(cv2.__version__)
image = cv2.imread("opencv/pk.jpg")
print(type(image))
print(image.shape)

cv2.imshow("my image", image)
cv2.waitKey(0)
