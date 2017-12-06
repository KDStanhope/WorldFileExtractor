# WorldFileExtractor
Makes a TiffWorld file Using Headers From Existing GeoTiff.

<b>WorldFileExtractor.py</b> and <b>WorldFileExtractor_Commented.py</b> do exactly the same thing

<b>Just Download WorldFileExtractor.py and run it in a folder with a bunch of GeoTiffs to extract a .tfw file :) </b>

Works with python 3.6!
Not tested on 2.7 but it should work. 

<i>Sometimes you just need a tiff world file when all you have is a GeoTiff. </i>

This makes them. 
Simply pop this in the same folder as all of your GeoTiffs and run. 
Or execute from commandline... again, just make sure its in the same folder as all your tiffs.

This needs the GDAL libraries which I found a little tough to get on a Windows 10 machine with Python 3.4+
For those who can't seem to install the GDAL-2.2 libs for python you can easily grab a .whl thanks to <b>Christoph Gohlke</b> who keeps "Unofficial Windows Binaries for Python Extension Packages" over at https://www.lfd.uci.edu/~gohlke/pythonlibs/ all you need to do is download <b>gdal-2.2.3-cp36-cp36m-win32.whl</b> (Note the win32) and install it using pip:

<code>pip install gdal-2.2.3-cp36-cp36m-win32.whl</code>

The other option is to do it manually or using the OSGeo4W web installer.  

<b>Added a version called WorldFileExtractor_Commented.py that fully explains what is going for those interested in learning </b>
