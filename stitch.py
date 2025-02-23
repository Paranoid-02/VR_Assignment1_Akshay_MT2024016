from panorama import Panorama
import imutils
import cv2
import glob

# Get all images in order using glob
images = [cv2.imread(img) for img in sorted(glob.glob(input("Enter the pattern for image files (e.g., 'images/*.jpg'): ")))]
no_of_images = len(images)

if no_of_images < 2:
    raise ValueError("At least 2 images are required for stitching")

# Resize all images to maintain aspect ratio
images = [imutils.resize(img, width=600, height=600) for img in images]

# Initialize panorama
panorama = Panorama()

# Stitch first two images
result, matched_points = panorama.image_stitch([images[-2], images[-1]], match_status=True)

# Stitch remaining images from right to left
for i in range(no_of_images - 2):
    result, matched_points = panorama.image_stitch([images[no_of_images - i - 3], result], match_status=True)

# Display results
cv2.imshow("Keypoint Matches", matched_points)
cv2.imshow("Panorama", result)

# Save results
cv2.imwrite("output/matched_points.jpg", matched_points)
cv2.imwrite("output/panorama_image.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

