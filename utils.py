import csv
import datetime


def get_newly_date():
    t = []
    with open('data/covid19_time_series.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2] == 'Lat':
                t = row[len(row)-1]
    return datetime.datetime.strptime(t, '%m/%d/%y').date()