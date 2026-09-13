import cv2

# 1. Check OpenCV version
print(cv2.__version__) 

# 2. Read the image it means we are importing the image along with the path
image = cv2.imread("opencv/pk.jpg")

# 3. Check what type of data the image is 
print(type(image))

# 4. Check image dimensions 
print(image.shape)

# 5. Convert color image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 6. Check grayscale dimensions
print(gray.shape)

# 7. Display original and grayscale images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

# 8. Wait for a key
cv2.waitKey(0)

# 9. Close all OpenCV windows
cv2.destroyAllWindows()

    