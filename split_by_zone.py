"""
Splitting the "parking violation geo csv" file we have created to 6
sections, where each section represents a time during the day.
We have split the data into 6 sections in weekday and 6 sections in weekend
The day is separated to these sections:
section 1 - between 7am to 9am
section 2 - between 9am to 12pm
section 3 - between 12pm to 16pm
section 4 - between 16pm to 19pm
section 5 - between 19pm to 23pm
section 6 - between 23pm to 07am
"""
import csv
import time
import sys
from pathlib import Path

def read_file(file_to_read, output_list):
    """
    Splitting the data for the zones files
    :param file_to_read: the geo file of all the parking violations
    :param output_list:
    :return:
    """
    with open(file_to_read) as original_file:
        reader = csv.DictReader(original_file)
        for row in reader:
            if row["Day"] != "0" and row["Day"] != "6":
                # zone between 7am to 9am
                if 42 <= int(row["Zone"]) < 54:
                    add_lines(output_list[0], row)
                # zone between 9am to 12pm
                elif 54 <= int(row["Zone"]) < 72:
                    add_lines(output_list[1], row)
                # zone between 12pm to 16pm
                elif 72 <= int(row["Zone"]) < 96:
                    add_lines(output_list[2], row)
                # zone between 16pm to 19pm
                elif 96 <= int(row["Zone"]) < 114:
                    add_lines(output_list[3], row)
                # zone between 19pm to 23pm
                elif 114 <= int(row["Zone"]) < 138:
                    add_lines(output_list[4], row)
                # zone between 23pm to 07am
                elif 138 <= int(row["Zone"]) or int(row["Zone"]) < 42:
                    add_lines(output_list[5], row)
            else:
                #weekend
                # zone between 7am to 9am
                if 42 <= int(row["Zone"]) < 54:
                    add_lines(output_list[6], row)
                # zone between 9am to 12pm
                elif 54 <= int(row["Zone"]) < 72:
                    add_lines(output_list[7], row)
                # zone between 12pm to 16pm
                elif 72 <= int(row["Zone"]) < 96:
                    add_lines(output_list[8], row)
                # zone between 16pm to 19pm
                elif 96 <= int(row["Zone"]) < 114:
                    add_lines(output_list[9], row)
                # zone between 19pm to 23pm
                elif 114 <= int(row["Zone"]) < 138:
                    add_lines(output_list[10], row)
                # zone between 23pm to 07am
                elif 138 <= int(row["Zone"]) or int(row["Zone"]) < 42:
                    add_lines(output_list[11], row)

def add_lines(output_file, row):
    """
    add the relevant line to its section file
    """
    column_names = ["Day", "Street Name", "Latitude", "Longitude",
                    "Violation Time", "Zone", "Parking Violation"]
    writer = csv.DictWriter(output_file,fieldnames=column_names, extrasaction='ignore')
    # row["Parking Violation"] = row["Violation Description"]
    writer.writerow(row)

def create_output_file(file_to_write):
    """
    Creating 6 sections csv files
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
    creating 12 sections files
    """
    # violation csv file with the streets coordinates
    geo_violation_path = Path(sys.argv[1])
    then1 = time.time()  # Time before the operations start
    # list of open files
    output_files = []
    # crating sections file for weekday - Monday, Tuesday, Wednesday, Thursday,
    # Friday
    for i in range(1,7):
        output_files.append(create_output_file("weekday_section_time" + str(
            i) + ".csv"))
    # crating sections file for weekend - Saturday, Sunday
    for i in range(1,7):
        output_files.append(create_output_file("weekend_section_time" + str(
            i) + ".csv"))
    read_file(geo_violation_path, output_files)
    for file_obj in output_files:
        file_obj.close()
    now = time.time()  # Time after it finished
    print("It took: ", now - then1, " seconds")

if __name__ == "__main__":
    main()