# -*- coding: utf-8 -*-
"""
Created on Thu Dec 04 07:15:06 2017

@author: KDStanhope

This does a simple job.
"""
import osgeo.gdal as gdal
import os
import glob
import sys


for items in glob.glob(os.path.join('.', '*.tif')):
    dataset = gdal.Open(items)
    padfTransform = dataset.GetGeoTransform()

    dataset = None
    
    pixelOffsetX = padfTransform[1]/2
    pixelOffsetY = padfTransform[5]/2
    
    X=padfTransform[0]+pixelOffsetX  
    Y=padfTransform[3]+pixelOffsetY

    worldFile = open(os.path.splitext(items)[0] + '.tfw', 'wt')
    worldFile.write("%0.8f\n" % padfTransform[1]) 
    worldFile.write("%0.8f\n" % padfTransform[2])
    worldFile.write("%0.8f\n" % padfTransform[4])
    worldFile.write("%0.8f\n" % padfTransform[5])
    worldFile.write("%0.8f\n" % X)
    worldFile.write("%0.8f\n" % Y)
    worldFile.close()
    print(str(items) + "...Done")
