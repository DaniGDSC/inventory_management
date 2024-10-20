import os
import re
from graphviz import Digraph

def create_er_diagram():
    # Ensure the result directory exists
    output_dir = 'F:/inventory_management-1/Diagram/result'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a new directed graph
    dot = Digraph('ER_Diagram', format='png')
    dot.attr(rankdir='LR', size='15')
    dot.attr('node', shape='plaintext')

    # Define entities with their attributes
    entities = {
        'User': ['<b>UserID</b> (PK)', 'Username', 'PasswordHash', 'Role', 'ContactInfo'],
        'Product': ['<b>ProductID</b> (PK)', 'Name', 'Description', '<i>CategoryID</i> (FK)', '<i>SupplierID</i> (FK)', 'QuantityInStock', 'ReorderLevel', '<i>LocationID</i> (FK)'],
        'Category': ['<b>CategoryID</b> (PK)', 'Name', 'Description'],
        'Supplier': ['<b>SupplierID</b> (PK)', 'Name', 'ContactInfo', 'Address'],
        'PurchaseOrder': ['<b>OrderID</b> (PK)', '<i>SupplierID</i> (FK)', '<i>ManagerID</i> (FK)', 'OrderDate', 'Status', 'TotalAmount'],
        'OrderItem': ['<b>OrderItemID</b> (PK)', '<i>OrderID</i> (FK)', '<i>ProductID</i> (FK)', 'Quantity', 'UnitPrice'],
        'InventoryMovement': ['<b>MovementID</b> (PK)', '<i>ProductID</i> (FK)', '<i>FromLocationID</i> (FK)', '<i>ToLocationID</i> (FK)', 'Quantity', 'MovementDate', 'MovementType', '<i>UserID</i> (FK)'],
        'Location': ['<b>LocationID</b> (PK)', 'Aisle', 'Shelf', 'Bin'],
        'ReorderThreshold': ['<b>ProductID</b> (PK, FK)', 'ThresholdQuantity', '<i>ManagerID</i> (FK)']
    }

    # Function to generate valid PORT names
    def make_port_name(attr):
        # Remove HTML tags
        port_name = re.sub(r'<[^>]*>', '', attr)
        # Remove non-alphanumeric characters and replace with underscores
        port_name = re.sub(r'\W+', '_', port_name)
        # Ensure the port name doesn't start with a digit
        if re.match(r'^\d', port_name):
            port_name = '_' + port_name
        return port_name.strip('_')

    # Add entities to the graph
    for entity, attributes in entities.items():
        label = '<<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">'
        label += f'<TR><TD BGCOLOR="lightblue" ALIGN="CENTER"><B>{entity}</B></TD></TR>'
        for attr in attributes:
            port_name = make_port_name(attr)
            label += f'<TR><TD ALIGN="LEFT" PORT="{port_name}">{attr}</TD></TR>'
        label += '</TABLE>>'

        dot.node(entity, label=label)

    # Define relationships with cardinality indicators
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

    # Add relationships to the graph with cardinality labels
    for parent, child, parent_card, child_card, parent_key, child_key in relationships:
        if parent_card == '1' and child_card == '1':
            label = '1:1'
        elif parent_card == '1' and child_card == 'N':
            label = '1:N'
        elif parent_card == 'N' and child_card == 'N':
            label = 'N:N'
        else:
            label = f'{parent_card}:{child_card}'

        # Customize edge styles based on cardinality
        if label == '1:N':
            arrowhead = 'crow'
            arrowsize = '1'
        elif label == 'N:N':
            arrowhead = 'crow'
            arrowsize = '1'
        elif label == '1:1':
            arrowhead = 'none'
            arrowsize = '0'
        else:
            arrowhead = 'normal'
            arrowsize = '1'

        dot.edge(parent, child, label=label, arrowhead=arrowhead, arrowsize=arrowsize, fontsize='10')

    # Specify the output file path inside the result folder
    output_file_path = os.path.join(output_dir, 'ER_diagram')

    try:
        # Render the diagram to a file
        dot.render(output_file_path, view=False)
        print(f"Diagram successfully created and saved at: {output_file_path}.png")
    except Exception as e:
        print(f"Error while rendering diagram: {e}")
    
    # Open and read the file if needed
    try:
        with open(f'{output_file_path}.png', 'rb') as file:
            pass
        print("File successfully read.")
    except FileNotFoundError:
        print("The file was not found. Check the rendering step.")
    except Exception as e:
        print(f"Error while reading the file: {e}")

if __name__ == "__main__":
    create_er_diagram()
