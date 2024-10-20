import csv
from inventory_management import session, Supplier

with open('suppliers.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        supplier = Supplier(
            Name=row['Name'],
            ContactInfo=row['ContactInfo'],
            Address=row['Address']
        )
        session.add(supplier)
    session.commit()
