import csv
from datetime import datetime
from inventory_management import session, InventoryMovement, MovementTypeEnum

with open('inventory_movements.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        inventory_movement = InventoryMovement(
            Quantity=int(row['Quantity']),
            MovementDate=datetime.strptime(row['MovementDate'], '%Y-%m-%d %H:%M:%S'),
            MovementType=MovementTypeEnum(row['MovementType']),
            ProductID=int(row['ProductID']),
            FromLocationID=int(row['FromLocationID']) if row['FromLocationID'] else None,
            ToLocationID=int(row['ToLocationID']) if row['ToLocationID'] else None,
            UserID=int(row['UserID'])
        )
        session.add(inventory_movement)
    session.commit()
