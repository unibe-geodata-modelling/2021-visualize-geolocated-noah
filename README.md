# 2021-visualize-geolocated-noah

__What the purpose of the program is:__ 

The purpose of this program is, as the name suggests, to visualize NOAH datapoints that have been geolocated. NOAH is an acronym for Naturally Occurring Affordable Housing, a designation for housing that fulfills certain affordability criteria. Finn Feldmann has proposed such numerical criteria both as an interpretation of current (2021) literature on NOAH, and also specifically for Switzerland which will be used as the basis for this program. While this conceptual framework has been prepared for Switzerland in the case of this program, which is more openly aimed at a global use, global values will be used rather than the locally adapted figures (specifically the program will use a 30% of income value not the adapted 25% of income value). The idea is that NOAH represents a way to easily detect housing that is affordable regardless of who provides the housing, and this program builds on this intent by allowing a user to visualize the dataset in a map, so that the spatial component of where housing that qualifies as NOAH is located becomes evident. 

__NOAH numerical criteria used by the program, adapted from Finn Feldmann`s proposed definition:__ 

To abridge the numerical definition mentioned above, here is the numerical criteria used by the program: 

•	Households must earn 80% or less of the median income to be low income.
•	The rental housing must not exceed 30% of the Household income to be considered affordable.
•	This means the medium income * 0.24= the maximum allowed rent for a rental unit to be still considered a NOAH housing unit. 

__What the program does in short:__
The program 2021 visualize geolocated noah is a program with two main functions into which the code is split. 

1: The first function of the program is to take housing datasets, saved as an excel file and process them so that only the housing datasets which qualify as NOAH remain, which then will be saved to a new excel file.
2: The second function is, that this program will take the newly created excel file containing NOAH housing only, and then plot those datapoints on a map so that the user can see the spatial distribution of the datapoints. The global map will scale to the datapoints so no matter where the NOAH housing units are located an appropriate map segment will be selected.

What is needed to run the program: 
•	Python 3.7
•	Excel

Step by Step instructions how to use the program: (keep in mind the code contains similar instructions as well) 
1.	For the first step, make sure that python version 3.7 is installed, as other tested versions did not allow the required modules to be installed.
2.	Download from github the provided example excel files, to see how the data should be imputed. 
3.	For the first excel, Test Excel Dataset
4.	 
5.	In Colum A the user must add in names to refer to individual rental housing units 
6.	In Colum B the median income of the region must be added
7.	In Colum C the monthly rent price of the housing unit must be added
8.	In Colum D and E the respective Longitude and Latitude values of the housing units must be added. The values must stem from the EPSG: 4326 projection also known as World Geodetic System 1984
9.	To manually find the coordinates of the users housing units in this projection system this link may be of service https://epsg.io/4326
10.	As a note, impute data is not limited to five rows, the user may expand this list as needed
11.	As a second note, if the user changes the name of the file, or sheet name it will have to be changed in the program as well for it to work.
12.	The Second Excel, Test NOAH Dataset, only the file name and sheet name have to correspond with the program (by default these will match), as the contents will be overwritten. 
13.	The Second Excel file must upon running of part 1 of the program contain at least three NOAH housing units or else step two cannot run
14.	An exemplary step 1 result can be seen below, where of the five input housing units, only three qualify as NOAH and thus are saved in the second excel file. In addition, there is a new column that now shows the maximum rent the housing unit could have to still be considered NOAH housing.
15.	 
16.	For Step two these datapoints are plotted to a background map of the surrounding region, as can be seen with the example below. 
17.	 ![Figure_1](https://user-images.githubusercontent.com/79707125/137979655-3438ce91-4bca-49af-a3b1-b0f456701c13.png)

