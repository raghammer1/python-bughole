# # import numpy as np
# # import cv2

# # # Create a blank image with noise (simulating bugholes)
# # image = np.random.randint(150, 255, (100, 100), dtype=np.uint8)
# # for _ in range(10):  # Simulate bugholes
# #     x, y = np.random.randint(0, 100, size=2)
# #     cv2.circle(image, (x, y), 3, (30, 30, 30), -1)

# # cv2.imwrite("concrete_sample.jpg", image)
# import numpy as np
# import cv2

# # Create a blank grayscale image (40x40 pixels, gray background)
# image = np.full((40, 40), 200, dtype=np.uint8)

# # Add some rectangular bugholes (black areas)
# cv2.rectangle(image, (5, 5), (10, 10), (0, 0, 0), -1)  # Bughole 1
# cv2.rectangle(image, (20, 15), (30, 25), (0, 0, 0), -1)  # Bughole 2
# cv2.rectangle(image, (32, 5), (38, 12), (0, 0, 0), -1)  # Bughole 3

# # Save and display
# cv2.imwrite("grid_bughole_image.png", image)
# cv2.imshow("Bugholes", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
import numpy as np
import cv2

# Create a blank grayscale image (40x40 pixels, gray background)
image = np.full((200, 200), 200, dtype=np.uint8)

# Add some rectangular bugholes (black areas)
cv2.rectangle(image, (5, 5), (10, 10), (0, 0, 0), -1)  # Bughole 1
cv2.rectangle(image, (20, 15), (30, 25), (0, 0, 0), -1)  # Bughole 2
cv2.rectangle(image, (32, 5), (38, 12), (0, 0, 0), -1)  # Bughole 3

# Save the image in the current folder
cv2.imwrite("bughole_grid.png", image)

print("Bughole image saved as 'bughole_grid.png'")
