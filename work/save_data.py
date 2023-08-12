

import csv

def write_data(data):
    with open('Fcis_data.csv', 'w', newline='',encoding="utf-8") as file:
        writer = csv.writer(file)
        for key, value in data.items():
            writer.writerow([key, value])