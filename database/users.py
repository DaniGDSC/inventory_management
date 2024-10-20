import csv
from inventory_management import session, User, RoleEnum

with open('users.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user = User(
            Username=row['Username'],
            PasswordHash=row['PasswordHash'],
            Role=RoleEnum(row['Role']),
            ContactInfo=row['ContactInfo']
        )
        session.add(user)
    session.commit()
