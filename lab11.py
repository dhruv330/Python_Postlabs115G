import numpy as np
from PIL import Image

# Load image
img = Image.open('img.jpg')

# Convert to NumPy array
img_array = np.array(img)

# Get dimensions and shape
height, width = img.size  # PIL uses (width, height)
print("Image Dimensions:")
print(f"Height: {img_array.shape[0]}, Width: {img_array.shape[1]}")
print("Shape of Image:", img_array.shape)

# Minimum pixel value in Blue channel
min_blue = img_array[:, :, 2].min()   # channel order = R,G,B
print("Minimum Pixel Value at Blue Channel:", min_blue)

import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt

# Load image
img = Image.open('img.jpg')

# Add black padding (top, right, bottom, left)
padded_img = ImageOps.expand(img, border=50, fill='black')

# Show original and padded image
plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(padded_img)
plt.title("Padded Image (Black Border)")
plt.axis("off")

plt.show()

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Load image
img = Image.open('img.jpg')
img_array = np.array(img)

# Extract R, G, B channels
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

# Plot the channels
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(R, cmap='Reds')
plt.title("Red Channel")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(G, cmap='Greens')
plt.title("Green Channel")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(B, cmap='Blues')
plt.title("Blue Channel")
plt.axis("off")

plt.tight_layout()
plt.show()
