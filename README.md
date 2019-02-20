# parking-ticket-project
The project for A Needle in a Data Haystack course

Welcome to our project:)
There are two options : 1. run the demo 2. run all the project step by step.

-------------
Option 1:
-------------
If you would like to run the demo (GUI.py and demo.py), you will first have to create a suitable environment and download some files.

1. create the environment -
    1. python -m venv env
    2. env\Scripts\activate
    3. pip install -r requirements.txt
    *this step might take a while, but after this you are ready :)

2. Download the "sections" folder (contains 12 csv files) and "geoUnited2016.csv" file from "step2" folder. These files could be download from here -
https://drive.google.com/drive/folders/1FWeMBnpsg4BhHWIuTUk4GRz7wVolIYzn?usp=sharing

3. At demo.py change "START_PATH" and "TRAINING_PATH". (surrounded by #)
"START_PATH" - is the directory in it you saved the files from "sections" folder (not include a specific file name).
"TRAINING_PATH" - is the directory in it you saved the "geoUnited2016.csv" file (the file itself).

4. Now you are ready to run the demo by running "GUI.py"

----------------
Option 2:
----------------
The project starts by reading a 2 Giga file.
This is why the csv files (also the one which are created during the project) are in gitIgnore (because the amount of files and there sizes).

The original file the project is based on can be downloaded from here (2016 and 2017 csv files)- https://www.kaggle.com/new-york-city/nyc-parking-tickets

We have changed the original file names to "Violation_year.csv". For example from "Parking_Violations_Issued_-_Fiscal_Year_2017.csv" to "Violation_2017.csv"


The python files need to be run in this order:
1. creating_csv_files.py - create the csv file with and without parking violation.
In order to run this program you will need to change the path to your local csv path, in the variable "FILE_PATH" (the file you downloaded from "kaggle")
You should run this program twice on two different files.

2. geolocator.py - creates a united csv file from the file with and without the parking viation which we created in the previous step. This file will include the street latitude and longitude
In order to run this program you will need to change the pathes to your local csv pathes, for the violation and non violation csv files(you have created in the previous step) and for the output files.
You should run this program twice for 2016 files and 2017 files.

3. classification.py - we would like to test our data and predict for a parking ticket possibility. In order to run this program you will need to change the pathes to your local csv pathes, for the test and train csv files (the united 2016, 2017 files you have created in the previous step). Please notic that it might take this program to finish off to 4 minutes.

Now we would like to visualize the data. In order to visualize we have created 12 csv files, generating from the geo files we created at step 2.
There are 12 files because there are 6 sections and we split the week days inot two groups - weekday(Mon-Fri) and weekend(Sat-Sun). So, this lead us to step 4.

4. split_by_zone.py - splitiing the 10 minutes interval zones to 6 sections.
The sections are:
section 1 - between 7am to 9am
section 2 - between 9am to 12pm
section 3 - between 12pm to 16pm
section 4 - between 16pm to 19pm
section 5 - between 19pm to 23pm
section 6 - between 23pm to 07am
In order to run this program you will need to change the path to your local geo_violation csv path (which is one of the 3 files created at step 2)

Now you are able to run the demo and see visualziation of the data :)

5. ruuning the demo by running the GUI-
    5.1 - In demo.py file you need to change the parameter "START_PATH" to your local path directory. At the previous step we create 12 csv section files with the following name "weekday_section_timeX" or "weekend_section_timeX" where 'X' is a digit between 1 to 6. This has to be the name of those files, but the directory you choose to save them its free to your choice, so please just change the beginning of the path, by changing "START_PATH" constant. Moreover you will need to change TRAINING_PATH to the geoUnited2016.csv file we create at step 2
    5.2 - Now, In order to run the GUI, run GUI.py and follow the instruction.
    This will open you a heat-map showing the probabilty of getting a parking ticket. After 5 minutes you will also get a notice if the probabilty getting a parking ticket ay your chosen place during all week is high or low.


