import csv
from inventory_management import session, ReorderThreshold

with open('reorder_thresholds.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        reorder_threshold = ReorderThreshold(
            ProductID=row['ProductID'],
            ManagerID=row['ManagerID'],
            ThresholdQuantity=row['ThresholdQuantity']
        )
        session.add(reorder_threshold)
    session.commit()
