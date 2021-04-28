#0.0importy stuff
#rememeber you have to install these before you can import them
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl


#1.0 Data preparation
# remember you have to define how the excel should be set up. See word
# one open question is how the axis are defined, depending maybe also if I use cartopy or something els
#1.1 remember import the stuff above so the programm is able to read the excel files easier. so 0.0
#currently I have prepared a excel file which this program will access
#1.2 read the excel file.
df = pd.read_excel("D:\School\Master 2 Semester\Geodata Analysis and Modeling\Final Project\Excel Files\Test Excel Dataset.xlsx", sheet_name='Sheet1', engine= 'openpyxl')

#1.3 Search Median income, divide by 100 then multiply by 80, to get 80% value. Then Dividd that value by 100 and multiply by 30.
#this value is the maximum rent cost a property cna have to be noas.

df.drop()

#1.4 compare values generated at 1.3 with the colum with rent prices, and delete rows where rent exceeds the values of 1.3

#1.5 return, save newly created excel file.


#2.0map creation, probably with cartopy, if not maybe with contextily of geopandas