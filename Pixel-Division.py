from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math

# Get RGB Matrix 
def get_rgb_matrix_1(image_path_1):
  img = Image.open(image_path_1).convert('RGB')
  img = img.convert("L")
  rgb_matrix_1 = np.array(img)
  return rgb_matrix_1
def get_rgb_matrix_2(image_path_2):
  img = Image.open(image_path_2).convert('RGB')
  img = img.convert("L")
  rgb_matrix_2 = np.array(img)
  return rgb_matrix_2

# Set Image Paths
image_path_1 = 'Sentinel-2-L2A/Greyscale_01_09112020.png'
rgb_matrix_1 = get_rgb_matrix_1(image_path_1) 
image_path_2 = 'Sentinel-2-L2A/Greyscale_01_09032024.png'
rgb_matrix_2 = get_rgb_matrix_2(image_path_2)

#Print Image Dimensions
h = rgb_matrix_1.shape[0] #height of the image
w = rgb_matrix_1.shape[1] #width of the image
print("\n Rows:", rgb_matrix_1.shape[0])
print("\n Columns:", rgb_matrix_1.shape[1])
#print("Channels:", rgb_matrix_1.shape[2], "[R, G, B]")

# Create a list of the two images' RGB matrices
images = (rgb_matrix_1, rgb_matrix_2)
print("\n Matrix Shape =", rgb_matrix_1.shape)

image1 = images[0]
image2 = images[1]


# Create two new Sample_1 and Sample_2 matrices, with dimensions A x B, from each image matrix.
Sample_1 = image1[:,:]
Sample_2 = image2[:,:]  
print(Sample_1)
print(Sample_2)
   
# Create a new likeness_matrix (A x B) with the values of matrix 1 / matrix 2. 1 
likeness_matrix = np.array(Sample_1) / np.array(Sample_2)
print(likeness_matrix)
# A value of 1 represents perfect likeness. The further the value is from 1, the higher the pixel difference between images. 

# Create a new difference_matrix (A x B) with the absolute values of 1 - the likeness_matrix.
difference_matrix = np.array(abs(1-likeness_matrix))
print("PIX_NORM: \n", difference_matrix)
# Higher values represent higher difference. 

# Plot the new difference_matrix (A x B) using a colormap.
plt.imshow(difference_matrix, cmap='inferno') # Use cmap='gray' for grayscale images
plt.show()
# Lighter colors represent higher differences in pixel value. 


# Create a 25x25px grid with averaged difference values. 
#Crop difference_matrix to dimensions divisible by 25px. 
difference_matrix_crop = difference_matrix[0:200,0:350]
#Create new matrix with difference_matrix_crop values averaged over 25x25px cells.
avg_difference_matrix = []
row_averages = []
for i in range(0,200,25):
  for j in range(0,350,25):
    cell_avg = np.mean(difference_matrix_crop[i:i+25, j:j+25])
    print(cell_avg, i, i+25, j, j+25)
    row_averages.append(cell_avg)
  avg_difference_matrix.append(row_averages)
  row_averages = []
    
  
#Convert new matrix to a numpy array and view. 
averages = np.array(avg_difference_matrix)
print("\n Average Values =", averages)
print("\n averages shape =", averages.shape)
#New matrix has 112 values (from 8 rows and 14 columns). 

# Create new matrix with average values in proper gridspaces and plot. 
#np.array(averages[0:7])

plt.imshow(averages, cmap='inferno') # Use cmap='gray' for grayscale images
plt.show()