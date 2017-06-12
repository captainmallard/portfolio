'''
   Improving Resolution using Nearest Neighbor method.
   Copy, paste, and run in console.
   AUTHOR: Philip de Castro, 2017.
'''

import matplotlib.pyplot as plt #   python plotting library
import matplotlib.image as mpimg #  image viewing
import numpy as np #    arrays
#######################################################################################################################
fig1 = plt.figure(1) #  open first figure
img = mpimg.imread('pout.tiff') #   read in image to be resolved
imgplot = plt.imshow(img, cmap='gray') #    plot original image
fig1.suptitle('Image Before Nearest Neighbor')
#######################################################################################################################
zoomed_img = img.copy() #   make copy of original image. This is the image we will try to increase the resolution in to.
dimensions = np.shape(zoomed_img) # take dimensions of picture.
rows = dimensions[0]; columns = dimensions[1]
#######################################################################################################################
'''
This array will store the higher resolution photo. Every odd column and row is empty so that it can be filled in
using the nearest neighbor method.
'''
zoomed_array = np.zeros((2*rows, 2*columns))
'''
Fill every even row and column with the values from the original image.
'''
for i in range(rows): # iterate over rows of original image
    for j in range(columns): #  iterate over columns of original image
        zoomed_array[2*i, 2*j] = zoomed_img[i, j] # put values from original image in even number rows/columns
'''
Now we fill in the empty values of a column with the same value as the preceding column.
'''
for i in range(rows): # iterate over rows of original image
    for j in range(columns): #  iterate over columns of original image
        zoomed_array[2*i, 2*j+1] = zoomed_array[2*i, 2*j] # in the even rows and odd columns, put in the previous value
'''
Now we fill in the empty values of a row with the same values as the preceding row
'''
for i in range(2*columns): #    iterate over the columns of the larger image.
    for j in range(rows): # iterate over the rows of the original image.
        zoomed_array[2*j+1, i] = zoomed_array[2*j, i] # in the odd rows and all the columns, put in the previous value.
#######################################################################################################################
fig2 = plt.figure(2) #  plot new image
imgplot2 = plt.imshow(zoomed_array, cmap='gray')
fig2.suptitle('Photo After Nearest Neighbor')
'''
As we can see, the nearest neighbor method doesn't work very well...
'''

