import csv
from inventory_management import session, Product

with open('products.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        product = Product(
            Name=row['Name'],
            Description=row['Description'],
            QuantityInStock=int(row['QuantityInStock']),
            ReorderLevel=int(row['ReorderLevel']),
            CategoryID=int(row['CategoryID']),
            SupplierID=int(row['SupplierID']),
            LocationID=int(row['LocationID'])
        )
        session.add(product)
    session.commit()
