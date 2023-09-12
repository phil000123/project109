import cv2
import numpy as np
import pyautogui

# Capture a screenshot using PyAutoGUI
screenshot = pyautogui.screenshot()

# Convert the PIL image to an OpenCV compatible NumPy array
screenshot_cv = np.array(screenshot)

# Save the screenshot directly to disk using cv2.imwrite()
cv2.imwrite("screenshot.png", screenshot_cv)

# Load the image in OpenCV format
loaded_image = cv2.imread("screenshot.png")

# Display the loaded image (optional)
cv2.imshow("Loaded Image", loaded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
