# Digital Image Correlation Techniques Applied to Glacial Satellite Imagery of Athabasca Glacier in Alberta, Canada

This respository provides several methods for calculating displacement from time-series satellite imagery of Athabasca Glacier in Alberta, Canada. Several digital image correlation techinques are employed to a) provide a visual estimate of change and b) match specific surface features between images. This project was initited as part of a senior research project in the Earth Science department at Dartmouth College. 

Contents:
----------------
Pixel-Division.py 

ZNCC.py

Description: 
----------------
The Pixel-Division.py script takes the input of two greyscale png files and createes RGB matrices for each. It uses simple matrix operations to create a new image that visualizes the difference between pixels in each image. It then outputs a grid with averaged difference values. 

- Likeness Matrix = Image 1 Matrix / Image 2 Matrix -- A value of 1 represents perfect likeness. The further the value is from 1, the higher the pixel difference.
- Difference Matrix = Abs (1 - Likeness Matrix) -- Higher values represent higher difference.

The ZNCC.py script uses and OpenCV code (cv.TM_CCOEFF) to match a sample "chip" from Image 1 to an index location in Image 2 using a Zero Normalized Cross Correlation algorithm. This is a very simple script that inputs one image from a time series and one template "chip" from another image. Ideally, the chip should be contained within the first image. The file will output a copy of the first image with a square drawn over the index location that it has "matched" the chip to. 

Sources 
----------------
Pixel Division: https://homepages.inf.ed.ac.uk/rbf/HIPR2/pixdiv.htm

Zero Normalized Cross Correlation: https://docs.opencv.org/4.x/d4/dc6/tutorial_py_template_matching.html, https://robotacademy.net.au/lesson/template-matching/

Symmetric Least Squares Matching: https://www.ipb.uni-bonn.de/symmetric-least-squares-matching/index.html, https://engineering.purdue.edu/~bethel/lsm_1D.pdf

