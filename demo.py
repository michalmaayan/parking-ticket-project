"""
Running the demo with the classification.
Don't forget to change start_path in zone_csv_file method!!!
"""

import os
import xgboost
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import pandas as pd
from geopy.geocoders import Nominatim
import csv
import folium
from folium.plugins import HeatMap
from tkinter import messagebox
import webbrowser


TRAINING_PATH = r"filtered_csv_files\geoUnited2016.csv"

def classification_models(x_train, x_test, y_train):
    """
    running our classification model in order to predict the probability of
    getting a parking ticket.
    """
    classifiers = []
    model1 = xgboost.XGBClassifier()
    classifiers.append(model1)
    model2 = RandomForestClassifier()
    classifiers.append(model2)
    model3 = tree.DecisionTreeClassifier()
    classifiers.append(model3)
    y_pred = []
    for i, clf in enumerate(classifiers):
        clf.fit(x_train, y_train)
        y_pred.append(str(clf.predict(x_test)))
    if y_pred.count("[0]") > y_pred.count("[1]"):
        messagebox.showinfo('Message title',
                            "Park freely, your chances of getting a ticket are low!")
    else:
        messagebox.showinfo('Message title',
                            "Beware, your chances of getting a ticket are quite high...")
    print("done")

def from_zone_to_global_zone(zone):
    """
    Find the global zone which the inner zone is part of.
    :param zone: 10 minute time interval
    :return: the coordinate global zone
    """
    # zone between 7am to 9am
    if 42 <= zone < 54:
        return "1"
    # zone between 9am to 12pm
    elif 54 <= zone < 72:
        return "2"
    # zone between 12pm to 16pm
    elif 72 <= zone < 96:
        return "3"
    # zone between 16pm to 19pm
    elif 96 <= zone < 114:
        return "4"
    # zone between 19pm to 23pm
    elif 114 <= zone < 138:
        return "5"
    # zone between 23pm to 07am
    elif 138 <= zone or zone < 42:
        return "6"


def time_to_zone(time):
    """
    convert the given time to a ten interval time zone
    :param time: a string in HHMM
    :return: the zone as an int number
    """
    time = int(time)
    if time % 100 < 10:
        x = time // 100
        return x * 6 + 1
    if time % 100 < 20:
        x = time // 100
        return x * 6 + 2
    if time % 100 < 30:
        x = time // 100
        return x * 6 + 3
    if time % 100 < 40:
        x = time // 100
        return x * 6 + 4
    if time % 100 < 50:
        x = time // 100
        return x * 6 + 5
    x = time // 100
    return (x + 1) * 6


def address_to_coordinate(address):
    """
    replace street address to latitude and longitude
    """
    try:
        address = address.lower()
        geolocator = Nominatim(user_agent="Python/3.6 "
                                          "(michal.maayan+needleproject@mail.huji.ac.il) "
                                          "Parking Tickets Research")
        location = geolocator.geocode(address + " NYC")
        coordinate = (location.latitude, location.longitude)
        return coordinate
    # validate the user "address" input
    except Exception:
        messagebox.showinfo('Error', 'Invalid Street name, Enter a valid '
                                     'street name')
        pass

def zone_csv_file(day, global_zone):
    """
    return the path to the coordinate csv file, according to the user input
    """
    # in case the user chose Saturday or Sunday
    if day == 0 or day == 6:
        part_of_week = "weekend"
    else:
        part_of_week = "weekday"
    start_path = "zones_csv\\"
    path_name = start_path + part_of_week + "_zone_time" + global_zone + ".csv"
    return path_name


def html_visual(path_name, coordinate):
    """
    return the user an HTML linked to a hit-map represent the area of his
    parking according to the chosen time and day
    :param path_name:
    :param coordinate:
    :return:
    """
    START_ZOOM = 18  # MAX ZOOM=18 , MIN ZOOM = 1

    map = folium.Map(location=coordinate, zoom_start=START_ZOOM)
    folium.Marker(location=coordinate, popup='I am here').add_to(map)

    heat_df = pd.read_csv(path_name, dtype=object)

    # Ensure you're handing it floats
    heat_df['Latitude'] = heat_df['Latitude'].astype(float)
    heat_df['Longitude'] = heat_df['Longitude'].astype(float)

    heat_df = heat_df[['Latitude', 'Longitude']]
    heat_df = heat_df.dropna(axis=0, subset=['Latitude', 'Longitude'])

    # List comprehension to make out list of lists
    heat_data = [[row['Latitude'], row['Longitude']] for index, row in
                 heat_df.iterrows()]

    # Plot it on the map
    HeatMap(heat_data).add_to(map)

    # open the saved map in browser
    map.save('map.html')
    webbrowser.open('file://' + os.path.realpath("map.html"))
    print("map is ready")

def validate_time(time):
    """
    validate the user "time" input
    :return: True if time is valid and False otherwise
    """
    if len(time) != 4:
        return False
    if int(time)%100 > 59:
        return False
    if int(time)//100 > 23:
        return False
    return True

def create_csv(day, time, street):
    """
    creating a "test.csv" file from the user input
    """
    # validte user "day" input
    if int(day)<0 or int(day)>6:
        print("day2")
        messagebox.showinfo('Error', "Invalid day, Eneter a valid day digit"
                                     " (0-Sunday...6-Sutarday)")
        raise Exception("invalid day")
    # validte user "time" input
    if not validate_time(time):
        messagebox.showinfo('Error', "Invalid time, Eneter a valid time "
                                     "between 0000-2359")
        raise Exception("invalid time")
    zone = time_to_zone(time)
    coordinate = address_to_coordinate(street)
    global_zone = from_zone_to_global_zone(zone)
    path_name = zone_csv_file(day, global_zone)
    html_visual(path_name, coordinate)
    with open("demo.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        column_names = ["Day", "Zone", "Latitude", "Longitude", "Parking Violation"]
        writer.writerow(column_names)
        writer.writerow([day, zone, coordinate[0], coordinate[1], 0])


def run_demo(day, time, street_name):
    """
    This method is called from GUI.py
    :param day: user input
    :param time: user input
    :param street_name: user input
    :return: a hit map and a note about the chance to get a parking ticket
    """
    try:
        print("Have patience it might take a minute, we are learning from a "
              "database with 4 million rows:)")
        create_csv(day, time, street_name)
        training_data = pd.read_csv(TRAINING_PATH)
        x_train = training_data[["Day", "Zone", "Latitude", "Longitude"]]
        y_train = training_data['Parking Violation']
        testing_data = pd.read_csv(r"demo.csv")
        x_test = testing_data[["Day", "Zone", "Latitude", "Longitude"]]
        classification_models(x_train, x_test, y_train)
    except Exception:
        pass

