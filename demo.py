import xgboost
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
import pandas as pd
from geopy.geocoders import Nominatim
import csv
import folium
from folium.plugins import HeatMap

def classification_models(x_train, x_test, y_train, y_test):
    classifiers = []
    model1 = xgboost.XGBClassifier()
    classifiers.append(model1)
    model2 = RandomForestClassifier()
    classifiers.append(model2)
    model3 = tree.DecisionTreeClassifier()
    classifiers.append(model3)
    y_pred = []
    for i,clf in enumerate(classifiers):
        clf.fit(x_train, y_train)
        y_pred.append(str(clf.predict(x_test)))
    if y_pred.count("[0]")> y_pred.count("[1]"):
        print("Park freely, your chances of getting a ticket are low!")
    else:
        print("Beware, your chances of getting a ticket are quite high...")

def from_zone_to_global_zone(zone):
    """
    Find the global zone the inner zone is part of.
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
    covert the given time to a ten interval time zone
    :param time: a string in HHMM
    :return: the zone as an int number
    """
    time = int(time)
    if time%100 < 10:
        x = time//100
        return x*6 + 1
    if time%100 < 20:
        x = time//100
        return x*6 + 2
    if time%100 < 30:
        x = time//100
        return x*6 + 3
    if time%100 < 40:
        x = time//100
        return x*6 + 4
    if time%100 < 50:
        x = time//100
        return x*6 + 5
    x = time // 100
    return (x+1)*6

def address_to_coordinate(address):
    """
    replace street address to latitude and longitude
    """
    address = address.lower()
    geolocator = Nominatim(user_agent="Python/3.6 "
                                      "(michal.maayan+needleproject@mail.huji.ac.il) "
                                      "Parking Tickets Research")
    location = geolocator.geocode(address + " NYC")
    coordinate = (location.latitude, location.longitude)
    return coordinate

def zone_csv_file(day,global_zone):
    """
    return the path to the coordinate csv file, according to the user input
    """
    # in case the user chose Saturday or Sunday
    if day==0 or day==6:
        start_title = "weekend"
    else:
        start_title = "weekday"
    path_name = "zones_csv\\"+start_title+"_zone_time"+global_zone+".csv"
    return path_name

def html_vizual(path_name, coordinate):
    """
    return the usewr an HTML linked to a hit-map represent the area of his
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
    map.save('index.html')

def create_csv(day,time,street):
    """
    creating a "test.csv" file from the user input
    """
    zone = time_to_zone(time)
    coordinate = address_to_coordinate(street)
    global_zone = from_zone_to_global_zone(zone)
    path_name = zone_csv_file(day,global_zone)
    html_vizual(path_name, coordinate)
    with open("demo.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        column_names = ["Day", "Zone", "Latitude", "Longitude", "Parking Violation"]
        writer.writerow(column_names)
        writer.writerow([day, zone, coordinate[0], coordinate[1], 0])

def main():
    # training_data = pd.read_csv(
    #     r"filtered_csv_files\geoUnited2017.csv")
    # x_train = training_data[["Day", "Zone", "Latitude", "Longitude"]]
    # y_train = training_data['Parking Violation']

    print("hello, please enter the requested data one by one:")
    day = input("please enter the day as a digit (Sun-0, Mon-1, Tue-2, "
                "Wed-3, Thur-4, Fri-5, Sat-6): ")
    time = input("please enter the time in HHMM format: ")
    street_name = input("please enter the street name: ")
    print()
    create_csv(day, time, street_name)
    # print("Have patience it might take a minute, we are learning from a "
    #       "database with 4 million rows:)")
    # print()
    # testing_data = pd.read_csv(r"demo.csv")
    # x_test = testing_data[["Day", "Zone", "Latitude", "Longitude"]]
    # y_test = testing_data['Parking Violation']
    # classification_models(x_train, x_test, y_train, y_test)

if __name__ == "__main__":
    main()
