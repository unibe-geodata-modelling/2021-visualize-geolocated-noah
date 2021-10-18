#0.0 First the modules listed below must be installed and then imported (for this to work you need to be running python version 3.7)
import numpy as np
import xlrd
import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import pip
import fiona
import pyproj
import rtree
import shapely
import geopandas as gpd
import contextily as ctx

#1.0 Data preparation: To use this programm two excel files, of which example files can be downloaded from github, have to be prepared according to the read me

#1.1 To facilitate the reading of the user input data, the location of the prepared excel files must be set. This must changed according to where the user has stored their prepared excel files.
myworkspace="C:\FinnFeldmann\Excel Files"

#1.2 This step reads the excel file. If the example file name or sheet name have been change, then this must be adapted here as well.

df = pd.read_excel(myworkspace+"\Test Excel Dataset.xlsx", sheet_name='Sheet1', engine= 'openpyxl')

#1.3 Here the rentmax is defined, by multiplying the median income by .24, as per Finn Feldmanns NOAH formula, see also the read me

df["rentmax"]= df['Median Income (Monthly)'] *0.24 #calculates the maximum rent for the median mean and adds it as a new column caller rentmanx to the df

#1.4 compare values generated at 1.3 with the colum with rent prices, and delete rows where rent exceeds the values of 1.3

dfnew= df[df['Rent Price (Monthly)']<=df["rentmax"]] #this part creates a new dataframe (dfnew) which as a condition only includes rows where rent montly is smaller or equal to rentmax.

#1.5 save newly created NOAH only dataset to the second prepared Excel file Test NOAH Dataset

#option 1 (not recommended)

dfnew.to_excel(myworkspace+"\dfnew.xlsx")# saves it but only in the reopsitory location,

#option 2 (recommended and used for part 2) this variant you adapt the excel file Test NOAH Dataset according to the read me

dfnew.to_excel(myworkspace+"\Test NOAH Dataset.xlsx", sheet_name="Page 1")


#2.0map creation from the adapted excel file Test NOAH Dataset
#2.1 In case part 2 is not performed right after part 1 (i.e. part 1 is no longer in memory) then part 0.0 must be run again


#2.2 In case part 2 is not performed right after part 1 (i.e. part 1 is no longer in memory) then the adapted excel file Test NOAH Dataset must be reloaded into memory, in which case the code below must be run

dfnew = pd.read_excel(myworkspace+"\Test NOAH Dataset.xlsx", sheet_name="Page 1", engine= 'openpyxl')

#2.3 current dataframe has no geometry, so need to convert it so it can have a crs which is needed for geopandas to use the input data

gdf = gpd.GeoDataFrame(dfnew, geometry=gpd.points_from_xy(dfnew.Longitude,dfnew.Latitude))
gdf.crs

#after conversion a crs needs to be specified which is done in this step (the crs needed depends on the add_basemap provider)

gdf = gdf.set_crs(4326,allow_override=True)

#gdf = gdf.set_crs(3857,allow_override=True)
#this is currently old hat blow. Reviw once the tranfpration has been achieved
#2.3 Now with data loaded (which has to have its geolocation given in EPSG: 4326 i.e WGS84 )
#first check projection(didnt work as no crs)
gdf.crs
#If data not in the right projection, can reprojet to web map projectiosn
#dfnew_wm = dfnew.to_crs("EPSG:4326")

#2.4 plot first. Here the set dataframe is plotted against a blank backgroun

#gdf.boundary.plot()
gdf.plot()

#2.5 now try to add a basemap. This should add a automatically generated map to the backgruond to the plotted points
ax = gdf.plot(figsize=(9,9))
#ax = gdf.plot(figsize= (gdf.Longitude.max()+0.1,gdf.Latitude.max()+0.1))
#ax = gdf.plot()


ax.set_xlim([gdf.Longitude.min()-0.1,gdf.Longitude.max()+0.1])
ax.set_ylim([gdf.Latitude.min()-0.1,gdf.Latitude.max()+0.1])
ctx.add_basemap(ax, crs=gdf.crs, source=ctx.providers.OpenStreetMap.Mapnik)

plt.title("NOAH Housing", fontsize=20, color= 'green')

#With annotate I would like to add text to the various data points to show the rent prices of the locations
#this first example is how to manually add text to a location
plt.annotate(text= "cow", xy=(7.245303, 46.94853))


#this is the work in progress in how to itterate through all values. Mind that as I have used row names with parentheseis
#"Latitude" is currently a stand in for Rent price Monthly, which I would modify in the excel if this works out
for idx, row in gdf.iterrows():
    plt.annotate(text=row["Latitude"], xy=row["geometry"])


#while you can copy the produced fig, this would be a way to safe it directly.
fig.savefig("test.pdf", dpi=1000)





