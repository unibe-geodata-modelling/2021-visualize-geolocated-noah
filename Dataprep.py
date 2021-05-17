#0.0importy stuff
#rememeber you have to install these before you can import them
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


#1.0 Data preparation
# remember you have to define how the excel should be set up. See word
#if 1.5 option 2 is selected, which is likely a second excel needs ot be set up, where the data is to be written in. or a second sheet should be added to the original file.
# one open question is how the axis are defined, depending maybe also if I use cartopy or something els
#1.1 remember import the stuff above so the programm is able to read the excel files easier. so 0.0
#currently I have prepared a excel file which this program will access
#1.2 read the excel file.
df = pd.read_excel("D:\School\Master 2 Semester\Geodata Analysis and Modeling\Final Project\Excel Files\Test Excel Dataset.xlsx", sheet_name='Sheet1', engine= 'openpyxl')

#1.3 Search Median income, divide by 100 then multiply by 80, to get 80% value. Then Dividd that value by 100 and multiply by 30.(or multiply by.24)
#this value is the maximum rent cost a property cna have to be noas.

df["rentmax"]= df['Median Income (Monthly)'] *0.24 #calculates the maximum rent for the median mean and adds it as a new column caller rentmanx to the df




#1.4 compare values generated at 1.3 with the colum with rent prices, and delete rows where rent exceeds the values of 1.3
dfnew= df[df['Rent Price (Monthly)']<=df["rentmax"]] #this part created new dataframe (dfnew) which as a condition only includes rows where rent montly is smaller or equalt to rentmax.

#1.5 return, save newly created excel file.

#option 1
dfnew.to_excel("dfnew.xlsx")# saves it but only in the reopsitory location, ideally I would like to specify where to save it$
#optionally precreate a ecel file an write to sheet

#option 2 this variant you need to make an excel in advance and give path and sheet name. Thne the data will be written to the sheet of the preixisting excel file
dfnew.to_excel("D:\School\Master 2 Semester\Geodata Analysis and Modeling\Final Project\Excel Files\Cowabunga.xlsx", sheet_name="Bananogram")




#2.0map creation, probably with cartopy, if not maybe with contextily of geopandas
#2.1 import things, that might need, here in addition to step 0.0.
#2.1 I have decided to first try with contextily as the normal background map seemed better for my aplicatin than with cartopy
#2.1 therefore these imports are taken from excercies introduction as I will do something similar
import pip
import fiona
import pyproj
import rtree
import shapely
import geopandas as gpd
import contextily as ctx
#2.2 First need to import the excel output of step 1.If step one was just performed then this file will still be in memory
#2.2 If not the code below can be read. this is both if step 1 was done before this session, or if the file needent be prepared and could be used directly.pathway needs to be given.
dfnew = pd.read_excel("D:\School\Master 2 Semester\Geodata Analysis and Modeling\Final Project\Excel Files\Cowabunga.xlsx", sheet_name="Bananogram", engine= 'openpyxl')
#2.3 current dataframe has no geometry, so need to convert it so it can have a crs.
gdf = geopandas.GeoDataFrame(dfnew, geometry=geopandas.points_from_xy(dfnew.Longitude,dfnew.Latitude))

#after conversion can specify the crs. Some variant of this
nodesgdf= nodesgdf.set_crs(2056,allow_override=True)


#this is currently old hat blow. Reviw once the tranfpration has been achieved
#2.3 Now with data loaded (which has to have its geolocation given in EPSG: 4326 i.e WGS84 )
#first check projection(didnt work as no crs)
dfnew.crs
#If data not in the right projection, can reprojet to web map projectiosn
dfnew_wm = dfnew.to_crs("EPSG:4326")

#2.4 somehow find out how to tell python my used proejction systme EPSG: 4326 and where it can find the coordinate data form the excel data


