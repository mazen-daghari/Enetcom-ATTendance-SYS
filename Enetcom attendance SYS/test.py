import winsound
import cv2

img = cv2.imread("w.png")

# Display the image
cv2.imshow('Image', img)

winsound.PlaySound("denied.wav", 0)
winsound.PlaySound("alarm.wav", 0)