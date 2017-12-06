# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 07:28:15 2017

@author: KDStanhope

This does a simple job.
"""
import osgeo.gdal as gdal
import os
import glob
import sys


for items in glob.glob(os.path.join('.', '*.tif')):
    # For loop iterates over tiffs in the current directory.
    dataset = gdal.Open(items)
    # each item is opened
    padfTransform = dataset.GetGeoTransform()
    # GetGeoTransform() is from the gdal library.
    # it gives us the pixel dimensions and the centre coord
    # of the top left pixel as a list

    dataset = None
    
    pixelOffsetX = padfTransform[1]/2
    pixelOffsetY = padfTransform[5]/2
    # Becasuse the coord is at the centre of the pixel
    # we need to move this point by HALF the pixel size
    # so that is it on the corner, not the centre.
    # padfTransform[1] is the pixel width
    # padfTransform[5] is the pixel height
    
    X=padfTransform[0]+pixelOffsetX  
    Y=padfTransform[3]+pixelOffsetY
    # padfTransform[0] is the upper left pixel x coord
    # padfTransform[3] is the upper left pixel y coord
    

    worldFile = open(os.path.splitext(items)[0] + '.tfw', 'wt')
    # creates a tfw file with the same name as tiff
    worldFile.write("%0.8f\n" % padfTransform[1]) 
    worldFile.write("%0.8f\n" % padfTransform[2])
    worldFile.write("%0.8f\n" % padfTransform[4])
    worldFile.write("%0.8f\n" % padfTransform[5])
    worldFile.write("%0.8f\n" % X)
    worldFile.write("%0.8f\n" % Y)
    # writes all the data we got above
    worldFile.close()
    # Closed the file 
    print(str(items) + "...Done")
    # prints "[tiff file name] ... Done" so it looks like its doing something. 
