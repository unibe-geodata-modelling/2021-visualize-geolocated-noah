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



#2.0map creation, probably with cartopy, if not maybe with contextily of geopandas