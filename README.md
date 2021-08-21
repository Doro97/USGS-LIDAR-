# USGS-LIDAR

The objective of this project is to measure elevation of a field at many different points in order to provide a better understanding to AgriTech on how water flows through a field and which parts are likely to be flooded or too dry


This project aims at producing an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data.The code interfaces with USGS 3DEP and fetch data using their API. 


This project aims at producing an easy to use, reliable and well designed python module that domain experts and data scientists can use to fetch, visualise, and transform publicly available satellite and LIDAR data.The code interfaces with USGS 3DEP and fetches data using their API. 

The python package code has been adapted from https://pdal.io/tutorial/iowa-entwine.html


The tasks are divided as follows:

1. Data Fetching and Loading
2. Visualization of the Terrain
3. Data transformation


# Data Fetching and Loading
The data is read from the USGS 3DEP AWS Public Dataset using the PDAL package. PDAL enables composing of operations on point clouds into pipelines. Pipelines define the processing of data within PDAL. They describe how point cloud data are read; processed and written .The pipeline can be written in a declarative JSON syntax or constructed using an available API. The PDAL pipeline is divided into the following stages: Readers, Filters and Writers. To create the pipeline the following functions are used: readers.ept is used to fetch the data, filters. outlier to filter it for noise , filters.smrf to classify the data as ground or not ground and writer.gdal to write out a digital terrain model.
## Steps followed:
1. A file with the name iowa.json is created
2. readers.ept reads the point cloud data from the EPT resource on AWS. Give it a URL to the root of the resource in the filename option, and also give it a bounds object to define the window in which we should select data from.
3. The data selcted may have noise properly classified, so filters.range can be used to keep all data that does not have a Classification Dimensions value of 7.
4. After removing points that have noise classifications, reset all of the classification values in the point data. filters.assign takes the expression 
Classification [:]=0 and assigns the Classification for each point to 0.
6. The data on the AWS 3DEP Public Dataset are stored in Web Mercator coordinate system, which is not suitable for many operations.There is need to reproject them into an appropriate UTM coordinate system (EPSG:26915).
7. The Simple Morphological Filter (filters.smrf) classifies points as ground or not-ground.
8. After the SMRF filter has been executed, keep points that are actually classified as ground in our point stream by selecting for points with Classification[2:2]
9. Having filtered the point data, write a raster digital terrain model with writers.gdal. 
10. We can also write a LAZ file containing the same points that were used to make the elevation model in the section above
## Executing the pipeline
1. Save the PDAL pipeline in Pipeline to a file called iowa.json
2. Invoke the PDAL pipeline command 

# Visualization of the Terrain
The elevation files have been graphically displayed as a 3D render plot.

# Data Transformation
The data transformation steps included the following:

## Calculation of the Topographic wetness index (TWI) 
TWI is a useful model to estimate where water will accumulate in an area with elevation differences

## Standardized grid 
 A python code that takes elevation points output from the USGS LIDAR tool and interpolates them to a grid.

