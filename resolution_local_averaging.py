'''
    Improving Resolution using Local Averages Method
    Copy, paste, and run in console.
    AUTHOR: Philip de Castro, 2017
'''
import matplotlib.pyplot as plt #   python plotting library
import matplotlib.image as mpimg #  image viewing
import numpy as np #    arrays
import math
#######################################################################################################################
fig1 = plt.figure(1) #  open first figure
img = mpimg.imread('pout.tiff') #   read in image to be resolved
imgplot = plt.imshow(img, cmap='gray') #    plot original image
fig1.suptitle('Image Before Local Averaging')
#######################################################################################################################
zoomed_img = img.copy() #   make copy of original image. This is the image we will try to increase the resolution in to.
dimensions = np.shape(zoomed_img) # take dimensions of picture.
rows = dimensions[0]; columns = dimensions[1] # define rows and columns values.
#######################################################################################################################
'''
This array will store the higher resolution image.
'''
zoomed_array = np.zeros((2*rows, 2*columns))
for i in range(rows):
    for j in range(columns): #  fill ZOOMED_ARRAY so that the values of the original image
        #   are in the even rows and columns.
        zoomed_array[2*i, 2*j] = zoomed_img[i, j]
'''
We loop over ZOOMED_ARRAY to fill in the missing values across rows using Local Averaging.
This missing value in a is determined by taking the average of the previous and next pixel.
If at the end of a row, it just takes the previous value.
'''
for i in range(rows):
    for j in range(columns):
        if j == columns-1: #    if at the last column
            zoomed_array[2*i, 2*j + 1] = zoomed_img[i, j] # copy value from previous columns
        else: # otherwise take the average of the surrounding two pixels.
            zoomed_array[2*i, 2*j+1] = math.floor((zoomed_array[2*i, 2*j] + zoomed_array[2*i, 2*(j+1)])/2)
'''
We loop over ZOOMED_ARRAY to fill the missing values down columns using Local Averaging.
'''
for i in range(2*columns):
    for j in range(rows):
        if j == rows-1: #   if at the last row
            zoomed_array[2*j+1, i] = zoomed_array[2*j, i] # just copy value from previous row
        else: # otherwise, take the average of the surrounding two pixels.
            zoomed_array[2*j+1, i] = math.floor((zoomed_array[2*j, i] + zoomed_array[2*(j+1), i])/2)
#######################################################################################################################
fig2 = plt.figure(2) #  display the new image
imgplot2 = plt.imshow(zoomed_array, cmap='gray')
fig2.suptitle('Image After Local Averaging')
'''
As we can see, Local Averaging is only marginally better.
'''