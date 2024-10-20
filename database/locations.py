import csv
from inventory_management import session, Location

with open('locations.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        location = Location(
            Aisle=row['Aisle'],
            Shelf=row['Shelf'],
            Bin=row['Bin']
        )
        session.add(location)
    session.commit()
