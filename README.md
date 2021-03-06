# parking-ticket-project
The project for A Needle in a Data Haystack course

Welcome to our project:) 

We recommend you use Windows, in was not tested on Linux.
There are two options :
1. run the demo
2. run the entire project step by step.

-----------------
Requirements:
-----------------
1. python3 64bit
2. git

-----------------
Installations:
-----------------
For both options you will need to do the following steps:
1. In the command line run git clone https://github.com/michalmaayan/parking-ticket-project.git
2. In the command line run cd parking-ticket-project
3. Create a suitable environment:
    1. python3 -m venv env
    2. env\Scripts\activate
    3. pip install -r requirements.txt
    *this step might take a while, but after this you are ready :)

-------------
Option 1:
-------------
If you would like to run the demo (GUI.py and demo.py), you will first have to download some files.

1. Download the "sections" folder (containing 12 csv files) and "geoUnited2016.csv" file from "step2" folder. These files could be download from here -
https://drive.google.com/drive/folders/1FWeMBnpsg4BhHWIuTUk4GRz7wVolIYzn?usp=sharing

2. In order to run the demo, you must run GUI.py by adding two arguments to the command line in the following format -
```
python GUI.py Path\To\sections_folder Path\To\geoUnited2016.csv
```
Or
* click on run in the toolbar
* edit configurations
* input both arguments to Parameters

Make sure to run GUI.py in the enviroment you created during the instalations

** Please Notice after a minute or two a heat-map will be displayed in your browser. After 5 more minutes you will also get a notification telling you whether the probability of getting a parking ticket at your chosen location is high or low.

*** If the gui shows 'Not Responding', don't be alarmed, The program is still running. If the map does'nt show up in your browser after a minute then you probably didn't enter the correct paths as arguments.

----------------
Option 2:
----------------
The project starts by reading a 2GB file.
This is why the csv files are in gitIgnore (also the one which are created during the project), the amount of files and there sizes.

The original file the project is based on can be downloaded from here (2016 and 2017 csv files)- https://www.kaggle.com/new-york-city/nyc-parking-tickets

Please notice that we have changed the original file names to "Violation_year.csv". For example from "Parking_Violations_Issued_-_Fiscal_Year_2017.csv" to "Violation_2017.csv"


Now you are ready to run the entire project, step by step -
The python files need to be run in this order:
1. creating_csv_files.py - creates 2 csv files. One containing rows with parking violations and one containing random rows without parking violations.
In order to run this program you will have to add one command line argument to the script in the following format -
```
python creating_csv_files.py.py Path\To\Violation_2016.csv
```
Where Path\To\Violation_2016.csv is for the file you have downloaded from "kaggle".
You should run this step twice on two different files (2016 and 2017).

After this step you should have 4 new csv files, 2 for each year.

2. geolocator.py - creates a united csv file from the files from the previous step, with and without parking violations. This file will include two new columns, latitude and longitude for each street.
In order to run this program you will have to add two command line arguments to the script in the following format -
```
python geolocator.py Path\To\Parking_Violations2016.csv Path\To\no_parkingViolations2016.csv
```
Where Path\To\Parking_Violations2016.csv Path\To\no_parkingViolations2016.csv are the paths for the files you have created in step 1.

After this step you should have 3 new csv files. Two are the same files from step 1 (containing parking violations and no parking violations), with the new columns of latitude and longitude. The 3rd file is a united file containing the first two files combined.
You should run this program twice for 2016 files and 2017 files (after this you will have 6 new files).


3. classification.py - we would like to test our data and predict the probability of receiving a parking ticket. In order to run this program you will have to add two command line arguments to the script in the following format -
```
python classification.py Path\To\geoUnited2016.csv Path\To\geoUnited2017.csv
```
Please notice that it might take up to 4 minutes for this program to finish running.

Now we would like to visualize the data. In order to visualize we have created 12 csv files, generated from the geo files we created at step 2.
There are 12 files because there are 6 sections and we split the week days into two groups - weekday(Mon-Fri) and weekend(Sat-Sun). So, this leads us to step 4.

4. split_by_zone.py - splitting the 10 minutes interval zones into 6 sections.
The sections are:
section 1 - between 7am to 9am
section 2 - between 9am to 12pm
section 3 - between 12pm to 16pm
section 4 - between 16pm to 19pm
section 5 - between 19pm to 23pm
section 6 - between 23pm to 07am
In order to run this program you will have to add one command line argument to the script in the following format -
```
python classification.py Path\To\geoViolation2017.csv
```
Where geoViolation2017.csv is one of the 3 files created during step2

Now you are able to run the demo and see a visualization of the data :)

5. running the demo by running the GUI-
In order to run the demo, by running GUI.py, you will have to add two command line arguments to the script in the following format -
```
python GUI.py Path\To\sections_folder Path\To\geoUnited2016.csv
```
At the previous step we created 12 csv section files with the following names "weekday_section_timeX" or "weekend_section_timeX" where 'X' is a digit between 1 to 6. The names of the files cannot be changed, but the directory you choose to save them in can be named as you like. "sections_folder" is the name of the folder which the files are saved in.
Moreover the geoUnited2016.csv is one of the files we have created at step 2
***Please Notice after a minute or two a heat-map will be displayed on your browser. After 5 more minutes you will also get a notification telling you whether the probability of getting a parking ticket at your chosen location is high or low.




