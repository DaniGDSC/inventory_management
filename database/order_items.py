import csv
from inventory_management import session, OrderItem

with open('order_items.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        order_item = OrderItem(
            Quantity=int(row['Quantity']),
            UnitPrice=float(row['UnitPrice']),
            OrderID=int(row['OrderID']),
            ProductID=int(row['ProductID'])
        )
        session.add(order_item)
    session.commit()
