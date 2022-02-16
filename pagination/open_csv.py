import csv
import os
from pagination.settings import BUS_STATION_CSV
print(os.listdir())
list_for_context = []
with open(BUS_STATION_CSV, 'r', encoding='utf-8') as file:
    reader_dict = csv.DictReader(file)
    for row in reader_dict:
        list_for_context.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
list_30 = []
for i, station in enumerate(list_for_context):
    if i == 30:
        break
    else:
        list_30.append(station)






