import cv2
import numpy as np

# Load image
img = cv2.imread('rose.jpg')   # Put your image in the same folder

# Convert BGR to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define color range (example: red)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Combine masks
mask = mask1 + mask2

# Apply mask
result = cv2.bitwise_and(img, img, mask=mask)

# Show original and result
cv2.imshow('Original', img)
cv2.imshow('Red Detection', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
