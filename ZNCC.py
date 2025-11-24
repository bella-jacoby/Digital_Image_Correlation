import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# --- Load images ---
img = cv.imread('Sentinel-2-L2A/Full_09032024.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read — check path"

template = cv.imread('Sentinel-2-L2A/Template_01_09112020.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "template could not be read — check path"

# --- Template size ---
w, h = template.shape[::-1]
print(f"Template Dimensions: {w} x {h}")

# --- Apply Template Matching using TM_CCOEFF ---
method = cv.TM_CCOEFF
res = cv.matchTemplate(img, template, method)

# --- Find best match location (maximum correlation) ---
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

print(f"Best match at {top_left} with correlation {max_val:.4f}")

# --- Draw rectangle on a copy of the original image ---
img_display = img.copy()
cv.rectangle(img_display, top_left, bottom_right, 255, 1)  # white outline

# --- Visualization ---
plt.figure(figsize=(6,3))

plt.subplot(1,2,1)
plt.imshow(res, cmap='inferno', interpolation='nearest')
plt.title('Correlation Map (TM_CCOEFF)')
plt.xticks([]), plt.yticks([])

plt.subplot(1,2,2)
plt.imshow(img_display, cmap='gray', interpolation='nearest')
plt.title('Detected Region')
plt.xticks([]), plt.yticks([])

plt.tight_layout()
plt.show()
