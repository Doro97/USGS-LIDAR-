import rasterio as rio
from affine import Affine

colour_data = []
def generate_colour_data(width, height, imagiry_data, pixel2coord):
    """Extract color data from the .tiff file """
    for i in range(1, height):
        for j in range(1, width):
            colour_data.append(
                [
                    pixel2coord(j, i)[0],
                    pixel2coord(j, i)[1],
                    imagiry_data.read([1])[0][i - 1][j - 1],
                    
                ]
            )
#Code that will extract the width, height and transformation information of the .tiff file and pass it to the function 
# generate_colour_data which will populate the color data in a list in the following format: [longitude, latitude, Red, Green, Blue, Alpha]
with rio.open('C:\Users\user.DESKTOP-OMQ89VA\Documents\USGS-LIDAR-\data\iowa.tif') as imagery_data:
    T0 = imagery_data.transform
    T1 = T0 * Affine.translation(0.5, 0.5)
    pixel2coord = lambda c, r: (c, r) * T1
    width = imagery_data.width
    height = imagery_data.height
   
    generate_colour_data(width, height, imagery_data, pixel2coord)

