"""
המטרה של הקוד הזה הינו לפרסר את קובץ האקסל הראשי שהורדנו לקובץ אקסל שרלוונטי עבורנו.
לכן נסנן רק את השורות שרלוונטיות עבורנו (דוח עבור parking ticket ) וכן נתאים את הזמנים ביום לzoneים ואת הימים למספר.
"""
import csv
import re
import datetime
import random

# src csv local path
FILE_PATH = r"src_data\Violations2017.csv"

def time_to_zone(time):
    #todo ךרשום שעוד מידע בקובץ pdf
    """
    A util function which replace the time which in HHMM format to the zone it
    belongs to.
    For example - 00:09 is corresponding to zone 1 and 23:09 is corresponding
    to zone 139.
    :param time: time in HHMM format
    :return: the zone corresponding to the time
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

def date_to_day(date):
    """
    A util function which replace the given date to its corresponding day
    in the week.
    :param date: the original date of the parking ticket
    :return: Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.
    """
    month, day, year = (int(x) for x in re.split('/|-',date))
    ans = datetime.date(year, month, day)
    return ans.strftime("%w")

def time_to_HHMM(given_time):
    """
    A util function which replace from am\pm format to HHMM format
    :param given_time: time in am\pm
    :return: the original time in HHMM format
    """
    if given_time[-1].lower() == "p":
        new_h = int(given_time[0:2]) + 12
        return str(new_h)+given_time[2:4]
    x = given_time[:-1]
    return x

def read_file(file_to_read, file_to_write, street_names):
    """
    Read the original file and filtered from it only the lines containing a
    parking ticket violation.
    :param file_to_read: the original csv file
    :param file_to_write: the name of the generated file with the parking
    violation
    :param street_names: the purpose of this set is to allow us to create a
    random file without violations.
    :return: num of lines in the output csv file
    (creates and not return) -  a set of all the streets relevant to our
    research and an output file in the form we need for the research
    """
    num_lines = 0
    num_filtered_lines = 0
    with open(file_to_write, 'w', newline='') as filtered_file:
        column_names = ["Issue Date", "Street Name",
                        "Violation Time", "Zone", "Violation Description"]
        writer = csv.DictWriter(filtered_file, fieldnames=column_names, extrasaction='ignore')
        writer.writeheader()
        with open(file_to_read) as original_file:
            reader = csv.DictReader(original_file)
            for row in reader:
                num_lines+=1
                if "No Parking" in row["Violation Description"]:
                    # the original time is in am\pm format
                    new_time = time_to_HHMM(row["Violation Time"])
                    row["Violation Time"] = new_time
                    # divided time to zones. further details in the "todo
                    # להוסיף את השם של הקובץ todo"
                    #  pdf file
                    row["Zone"] = time_to_zone(new_time)
                    row["Violation Description"] = 1 # parking violation
                    # the original day described by its date
                    row["Issue Date"] = date_to_day(row["Issue Date"])
                    writer.writerow(row)
                    num_filtered_lines+=1
                    street_names.add(row["Street Name"])
    return num_filtered_lines

def generate_time():
    """
    A util function generate a random time in HHMM format, where there is more
    probability to get a time between 0700-1900 (because the probability to get
    a parking ticket in this range of time is higher
    :return: a random time in HHMM format
    """
    hour_list = []
    for i in range(1, 24):
        hour_list.append(i)
        # make the hours between 7Am - 7PM appear with higher probability
        if 7 <= i <= 19:
            hour_list.append(i)
            hour_list.append(i)
    hours = random.choice(hour_list)
    rtime = int(random.random() * 86400)
    old_hours = int(rtime / 3600)
    minutes = int((rtime - old_hours * 3600) / 60)
    time_string = '%02d%02d' % (hours, minutes)
    return str(time_string)

def add_lines(file_name, street_names, num_lines):
    """
    Insert random information to the "no violation" file
    :param file_name: "no violation" file
    :param street_names: a set of streets name we collected from the original csv file
    :param num_lines: we would like to have the same number of lines in both
    csv - the one with parking ticket violation and the one without.
    :return: (create, not return) random lines to the "no violation" file.
    """
    # adding to csv in this order: Issue Date,Street Name,Violation Time, Violation Description
    with open(file_name, 'a', newline='') as f:
        writer = csv.writer(f)
        for _ in range(num_lines):
            street_name = random.choice(street_names)
            random_time = generate_time()
            zone = time_to_zone(random_time)
            random_day = random.randint(0, 6)
            description = 0 #no parking violation
            writer.writerow([random_day, street_name, random_time, zone,
                             description])

def create_file(filename):
    """
    :param filename: the file need to be parsered
    :return: we will create two files, one with the parking ticket violation
    and one we will generate from without violations.
    """
    street_names = set()
    output_file = "Parking_"+filename[9:]
    # generate the file with the violations
    num_lines = read_file(filename, output_file, street_names)

    # using another csv file to create the one without the violation
    temp_file = "no_parking"+filename[9:]
    with open(temp_file, 'w', newline='') as filtered_file:
        column_names = ["Issue Date", "Street Name", "Violation Time", "Zone",
                        "Violation Description"]
        writer = csv.DictWriter(filtered_file, fieldnames=column_names,
                                extrasaction='ignore')
        writer.writeheader()
        # adding random "without a parking ticket violations" lines
        add_lines(temp_file, list(street_names), num_lines)

def main():
    """
    Parsing the given csv file we downloaded from "Kaggle"
    """
    create_file(FILE_PATH)

if __name__ == "__main__":
    main()