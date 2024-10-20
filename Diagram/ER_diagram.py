import pydot
from graphviz import Digraph
import os

def create_er_diagram():
    # Create a new directed graph
    dot = Digraph('ER_Diagram', format='png')
    dot.attr(rankdir='LR', size='14')
    dot.attr('node', shape='rectangle')

    # Define entities with their attributes
    entities = {
        'User': ['UserID (PK)', 'Username', 'PasswordHash', 'Role', 'ContactInfo'],
        'Product': ['ProductID (PK)', 'Name', 'Description', 'CategoryID (FK)', 'SupplierID (FK)', 'QuantityInStock', 'ReorderLevel', 'LocationID (FK)'],
        'Category': ['CategoryID (PK)', 'Name', 'Description'],
        'Supplier': ['SupplierID (PK)', 'Name', 'ContactInfo', 'Address'],
        'PurchaseOrder': ['OrderID (PK)', 'SupplierID (FK)', 'ManagerID (FK)', 'OrderDate', 'Status', 'TotalAmount'],
        'OrderItem': ['OrderItemID (PK)', 'OrderID (FK)', 'ProductID (FK)', 'Quantity', 'UnitPrice'],
        'InventoryMovement': ['MovementID (PK)', 'ProductID (FK)', 'FromLocationID (FK)', 'ToLocationID (FK)', 'Quantity', 'MovementDate', 'MovementType', 'UserID (FK)'],
        'Location': ['LocationID (PK)', 'Aisle', 'Shelf', 'Bin'],
        'ReorderThreshold': ['ProductID (PK, FK)', 'ThresholdQuantity', 'ManagerID (FK)']
    }

    # Add entities to the graph
    for entity, attributes in entities.items():
        label = f'<<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">\n'
        label += f'<TR><TD BGCOLOR="lightblue"><B>{entity}</B></TD></TR>\n'
        for attr in attributes:
            label += f'<TR><TD ALIGN="LEFT">{attr}</TD></TR>\n'
        label += '</TABLE>>'

        dot.node(entity, label=label, shape='plaintext')

    # Define relationships
    relationships = [
        ('User', 'InventoryMovement', '1', 'N', 'UserID', 'UserID'),
        ('Product', 'InventoryMovement', '1', 'N', 'ProductID', 'ProductID'),
        ('Supplier', 'Product', '1', 'N', 'SupplierID', 'SupplierID'),
        ('Supplier', 'PurchaseOrder', '1', 'N', 'SupplierID', 'SupplierID'),
        ('User', 'PurchaseOrder', '1', 'N', 'UserID', 'ManagerID'),
        ('PurchaseOrder', 'OrderItem', '1', 'N', 'OrderID', 'OrderID'),
        ('Product', 'OrderItem', '1', 'N', 'ProductID', 'ProductID'),
        ('Category', 'Product', '1', 'N', 'CategoryID', 'CategoryID'),
        ('Location', 'Product', '1', 'N', 'LocationID', 'LocationID'),
        ('Product', 'ReorderThreshold', '1', '1', 'ProductID', 'ProductID'),
        ('User', 'ReorderThreshold', '1', 'N', 'UserID', 'ManagerID'),
    ]

    # Add relationships to the graph
    for parent, child, parent_card, child_card, parent_key, child_key in relationships:
        # Define edge label with cardinality
        label = f'{parent_card}:{child_card}'
        dot.edge(parent, child, label=label)

    # Specify the output file path inside the result folder
    output_file_path = os.path.join('F:/inventory_management-1/Diagram/result', 'ER_diagram')

    # Render the diagram to a file
    dot.render(output_file_path, view=False)

    # Open and read the file if needed
    with open(f'{output_file_path}.png', 'rb') as file:
        result = file.read()
    
if __name__ == "__main__":
    create_er_diagram()
