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
1. creating_csv_files.py - create the csv fike with and without parking violation
2. geolocator.py - creates a united csv file from the file with and without the parking viation which we created in the previous step. This file will include the street latitude and longitude
3.