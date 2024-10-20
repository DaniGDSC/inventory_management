import csv
from inventory_management import session, Category

with open('categories.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        category = Category(
            Name=row['Name'],
            Description=row['Description']
        )
        session.add(category)
    session.commit()
