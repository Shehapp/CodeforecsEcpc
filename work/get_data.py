
import csv

get_user = {}

def read_data():
    with open('Fcis_data.csv', 'r', newline='',encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            get_user[row[0]] = row[1]
    return get_user