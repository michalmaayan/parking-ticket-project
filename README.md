# parking-ticket-project
The project for Big Data course

The original file names were:
    Parking_Violations_Issued_-_Fiscal_Y...gust_2013___June_2014_.csv
    Parking_Violations_Issued_-_Fiscal_Year_2015.csv
    Parking_Violations_Issued_-_Fiscal_Year_2016.csv
    Parking_Violations_Issued_-_Fiscal_Year_2017.csv

We have changed the names to "Violation_year.csv". For example from "Parking_Violations_Issued_-_Fiscal_Year_2017.csv" to "Violation_2017.csv"
These files are in gitIgnore because of there sizes. They can be downloaded from -
https://www.kaggle.com/new-york-city/nyc-parking-tickets


The python files need to be run in this order:
1. creating_csv_files.py - create the csv file with and without parking violation
In order to run this program you will need to change the path to your local csv path, in the variable "FILE_PATH"
2. geolocator.py - creates a united csv file from the file with and without the parking viation which we created in the previous step. This file will include the street latitude and longitude
In order to run this program you will need to change the pathes to your local csv pathes, for the violation and non violation csv files(you have created in the previous step) and for the output files.
3. classification.py - we would like to test our data and predict for a parking ticket possibility. In order to run this program you will need to change the pathes to your local csv pathes, for the test and train csv files (the united 2-16, 2-17 files you have created in the previous step). Please notic that it might take this program to finish off to 4 minutes.

Now we would like to visualize the data. In order to visualize we have created 12 csv files, generating from the geo files we created at step 2.
There are 12 files because there are 6 zones and we split the week days inot two groups - weekday(Mon-Fri) and weekend(Sat-Sun). So, this lead us to step 4.

4. split_by_zone.py - splitiing the 10 minutes interval zones to 6 global zones.
The global zones are:
zone 1 - between 7am to 9am
zone 2 - between 9am to 12pm
zone 3 - between 12pm to 16pm
zone 4 - between 16pm to 19pm
zone 5 - between 19pm to 23pm
zone 6 - between 23pm to 07am
In order to run this program you will need to change the path to your local
geo_violation csv path

Now you are able to run the visualziation :)

5.
--------------------

create the environment -
0. download the requirements.txt file
1. python -m venv env
2. env\Scripts\activate
3. pip freeze
* At this stage the environment should be empty.
4. pip install -r requirements.txt
*this step might take a while, but after this you are ready :)
