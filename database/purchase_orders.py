import csv
from datetime import datetime
from inventory_management import session, PurchaseOrder, PurchaseOrderStatusEnum

with open('purchase_orders.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        purchase_order = PurchaseOrder(
            OrderDate=datetime.strptime(row['OrderDate'], '%Y-%m-%d').date(),
            Status=PurchaseOrderStatusEnum(row['Status']),
            TotalAmount=float(row['TotalAmount']),
            SupplierID=int(row['SupplierID']),
            ManagerID=int(row['ManagerID'])
        )
        session.add(purchase_order)
    session.commit()
