"""
Splitting the "parking violation geo csv" file we have created to 6 global zones
(here a zone is a part of the day) in weekday and 6 global zones in weekend
The day is separated to these global zones:
zone 1 - between 7am to 9am
zone 2 - between 9am to 12pm
zone 3 - between 12pm to 16pm
zone 4 - between 16pm to 19pm
zone 5 - between 19pm to 23pm
zone 6 - between 23pm to 07am
"""
import csv
import time

# violation csv file with the streets coordinates
GEO_VIOLATION_PATH = r"filtered_csv_files\geoViolation2017.csv"

def read_file(file_to_read, output_list):
    """
    Splitting the data for the zones files
    :param file_to_read: the geo file of all the parking violations
    :param output_list:
    :return:
    """
    num_lines_zone1 = 0
    num_lines_zone2 = 0
    num_lines_zone3 = 0
    num_lines_zone4 = 0
    num_lines_zone5 = 0
    num_lines_zone6 = 0
    num_lines_zone7 = 0
    num_lines_zone8 = 0
    num_lines_zone9 = 0
    num_lines_zone10 = 0
    num_lines_zone11 = 0
    num_lines_zone12 = 0
    with open(file_to_read) as original_file:
        reader = csv.DictReader(original_file)
        for row in reader:
            if row["Day"] != "0" and row["Day"] != "6":
                # zone between 7am to 9am
                if 42 <= int(row["Zone"]) < 54:
                    add_lines(output_list[0], row)
                    num_lines_zone1+=1
                # zone between 9am to 12pm
                elif 54 <= int(row["Zone"]) < 72:
                    add_lines(output_list[1], row)
                    num_lines_zone2 += 1
                # zone between 12pm to 16pm
                elif 72 <= int(row["Zone"]) < 96:
                    add_lines(output_list[2], row)
                    num_lines_zone3 += 1
                # zone between 16pm to 19pm
                elif 96 <= int(row["Zone"]) < 114:
                    add_lines(output_list[3], row)
                    num_lines_zone4 += 1
                # zone between 19pm to 23pm
                elif 114 <= int(row["Zone"]) < 138:
                    add_lines(output_list[4], row)
                    num_lines_zone5 += 1
                # zone between 23pm to 07am
                elif 138 <= int(row["Zone"]) or int(row["Zone"]) < 42:
                    add_lines(output_list[5], row)
                    num_lines_zone6 += 1
            else:
                #weekend
                # zone between 7am to 9am
                if 42 <= int(row["Zone"]) < 54:
                    add_lines(output_list[6], row)
                    num_lines_zone7 += 1
                # zone between 9am to 12pm
                elif 54 <= int(row["Zone"]) < 72:
                    add_lines(output_list[7], row)
                    num_lines_zone8 += 1
                # zone between 12pm to 16pm
                elif 72 <= int(row["Zone"]) < 96:
                    add_lines(output_list[8], row)
                    num_lines_zone9 += 1
                # zone between 16pm to 19pm
                elif 96 <= int(row["Zone"]) < 114:
                    add_lines(output_list[9], row)
                    num_lines_zone10 += 1
                # zone between 19pm to 23pm
                elif 114 <= int(row["Zone"]) < 138:
                    add_lines(output_list[10], row)
                    num_lines_zone11 += 1
                # zone between 23pm to 07am
                elif 138 <= int(row["Zone"]) or int(row["Zone"]) < 42:
                    add_lines(output_list[11], row)
                    num_lines_zone12 += 1

        print("current num of lines zone1:", num_lines_zone1)
        print("current num of lines zone2:", num_lines_zone2)
        print("current num of lines zone3:", num_lines_zone3)
        print("current num of lines zone4:", num_lines_zone4)
        print("current num of lines zone5:", num_lines_zone5)
        print("current num of lines zone6:", num_lines_zone6)
        print("current num of lines zone7:", num_lines_zone7)
        print("current num of lines zone8:", num_lines_zone8)
        print("current num of lines zone9:", num_lines_zone9)
        print("current num of lines zone10:", num_lines_zone10)
        print("current num of lines zone11:", num_lines_zone11)
        print("current num of lines zone12:", num_lines_zone12)


def add_lines(output_file, row):
    """
    add the relevant line to its zone file
    """
    column_names = ["Day", "Street Name", "Latitude", "Longitude",
                    "Violation Time", "Zone", "Parking Violation"]
    writer = csv.DictWriter(output_file,fieldnames=column_names, extrasaction='ignore')
    # row["Parking Violation"] = row["Violation Description"]
    writer.writerow(row)

def create_output_file(file_to_write):
    """
    Creating 6 zones csv files
    :param file_to_write:
    :return: the file we have created
    """
    filtered_file = open(file_to_write, 'w', newline="")
    column_names = ["Day", "Street Name", "Latitude", "Longitude",
                    "Violation Time", "Zone", "Parking Violation"]
    writer = csv.DictWriter(filtered_file, fieldnames=column_names,
                            extrasaction='ignore')
    writer.writeheader()
    return filtered_file

def main():
    """
    creating 12 zones files
    """
    then1 = time.time()  # Time before the operations start
    # list of open files
    output_files = []
    # crating zones file for weekday - Monday, Tuesday, Wednesday, Thursday,
    # Friday
    for i in range(1,7):
        output_files.append(create_output_file("weekday_zone_time" + str(i) + ".csv"))
    # crating zones file for weekend - Saturday, Sunday
    for i in range(1,7):
        output_files.append(create_output_file("weekend_zone_time" + str(i) + ".csv"))
    read_file(GEO_VIOLATION_PATH, output_files)
    for file_obj in output_files:
        file_obj.close()
    now = time.time()  # Time after it finished
    print("It took: ", now - then1, " seconds")


if __name__ == "__main__":
    main()