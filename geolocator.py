"""
Adding latitude and longitude to the parking ticket and the non violation files
"""
from geopy.geocoders import Nominatim
import time
import csv

# violation and non violation csv files
VIOLATION_PATH = r"filtered_csv_files\Parking_Violations2016.csv"
NO_VIOLATION_PATH = r"filtered_csv_files\no_parkingViolations2016.csv"
#output files
GEO_UNITED_PATH = r"filtered_csv_files\geoUnited2016.csv"
GEO_VIOLATION_PATH = "filtered_csv_files\geoViolation2016.csv"
GEO_NO_VIOLATION_PATH = "filtered_csv_files\geoNoViolation2016.csv"


# The process of converting street name to its latitude and longitude takes some time,
# like 4 hours, so we will keep the latitude and longitude we already found.
address_cache = {}

def address_to_coordinate(address):
    """
    replace street address to latitude and longitude
    :param address:
    :return:
    """
    address = address.lower()
    if address in address_cache:
        if address_cache[address] == None:
            raise ValueError('bad address from cache')
        return address_cache[address]
    #geopi request to wait one second per request
    time.sleep(1)
    geolocator = Nominatim(user_agent="Python/3.6 "
                                      "(michal.maayan+needleproject@mail.huji.ac.il) "
                                      "Parking Tickets Research")
    location = geolocator.geocode(address + " NYC")
    # for not looking a bad address again
    if location == None:
        address_cache[address] = None
        raise ValueError('bad address')
    coordinate = (location.latitude, location.longitude)
    address_cache[address] = coordinate
    return coordinate

def read_file(file_to_read, file_to_write):
    """
    Creates a new csv file based on the parking ticket violation csv file.
    There are some streets name's which are incorrect so we ignore them.
    :param file_to_read: the violation file we generated from the source csv
    file using "creating_csv_files.py"
    :param file_to_write: the new geo csv file with the corresponding latitude
    and longitude
    :return: number of lines in this file
    """
    with open(file_to_write, 'w', newline='') as filtered_file:
        column_names = ["Day", "Street Name", "Latitude", "Longitude",
                        "Violation Time", "Zone", "Parking Violation"]
        writer = csv.DictWriter(filtered_file, fieldnames=column_names,
                                extrasaction='ignore')
        writer.writeheader()
        num_lines = 0
        num_filtered_lines = 0
        with open(file_to_read) as original_file:
            reader = csv.DictReader(original_file)
            bad_address_counter = 0
            for row in reader:
                num_lines += 1
                try:
                    coordinate = address_to_coordinate(row["Street Name"])
                except Exception as err:
                    bad_address_counter+=1
                    print("Got exception: %s" % err)
                    print("Bad address: %s" % row["Street Name"])
                    print("num of bad addresses - ",bad_address_counter)
                    continue
                row["Latitude"] = coordinate[0]
                row["Longitude"] = coordinate[1]
                row["Day"] = row["Issue Date"]
                row["Parking Violation"] = row["Violation Description"]
                writer.writerow(row)
                num_filtered_lines += 1
                if num_lines % 100 == 0:
                    filtered_file.flush()
                    print("current num of lines:", num_lines)
                    print("current num of filtered lines:", num_filtered_lines)
    return num_filtered_lines

def add_to_file(file_to_read, file_to_write):
    """
    Adding to the geo file we created the lines with no violation
    :param file_to_read: the no violation file we created in the previous
    step, using - "creating_csv_files.py"
    :param file_to_write: the geo file
    :return: number of lines we added at this step
    """
    with open(file_to_write, 'a', newline='') as filtered_file:
        column_names = ["Day", "Street Name", "Latitude", "Longitude",
                        "Violation Time", "Zone", "Violation Description"]
        writer = csv.DictWriter(filtered_file, fieldnames=column_names,
                                extrasaction='ignore')
        num_lines = 0
        num_filtered_lines = 0
        with open(file_to_read) as original_file:
            reader = csv.DictReader(original_file)
            bad_address_counter = 0
            for row in reader:
                num_lines += 1
                try:
                    coordinate = address_to_coordinate(row["Street Name"])
                except Exception as err:
                    bad_address_counter+=1
                    print("Got exception: %s" % err)
                    print("Bad address: %s" % row["Street Name"])
                    print("num of bad address - ",bad_address_counter)
                    continue
                row["Latitude"] = coordinate[0]
                row["Longitude"] = coordinate[1]
                row["Day"] = row["Issue Date"]
                row["Parking Violation"] = row["Violation Description"]
                writer.writerow(row)
                num_filtered_lines += 1
                if num_lines % 100 == 0:
                    filtered_file.flush()
                    print("current num of lines:", num_lines)
                    print("current num of filtered lines:", num_filtered_lines)
    return num_filtered_lines

def main():
    """
    Read the violation and the non violation files and replace the street
    name with the corresponding geolocation. Creates a united file name
    "geo2016" or "geo2017" depend on the year of the input files.
    """
    then = time.time()
    counter1 = read_file(VIOLATION_PATH, GEO_UNITED_PATH)
    now = time.time()  # Time after it finished
    print("It took for violation: ", now - then, " seconds")
    print("now adding the no parking")
    counter2 = add_to_file(NO_VIOLATION_PATH, GEO_UNITED_PATH)
    now = time.time()  # Time after it finished
    print("total lines in the united geo file:", counter1+counter2)
    print("It took: ", now - then, " seconds")
    print("two separates files:")
    then = time.time()
    counter3 = read_file(VIOLATION_PATH, GEO_VIOLATION_PATH)
    print("total lines in the violation geo file:", counter3)
    now = time.time()  # Time after it finished
    print("It took for violation round 2: ", now - then, " seconds")
    print("now adding the no violation parking")
    counter4 = read_file(NO_VIOLATION_PATH, GEO_NO_VIOLATION_PATH)
    print("total lines in the No violation geo file:", counter4)
    now = time.time()  # Time after it finished
    print("It took for NO violation round 2: ", now - then, " seconds")

if __name__ == "__main__":
    main()