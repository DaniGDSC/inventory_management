import os
from graphviz import Digraph

def create_class_diagram():
    # Ensure the output directory exists
    output_dir = 'result'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a new directed graph
    dot = Digraph('ClassDiagram', format='png')
    dot.attr(rankdir='TB', size='15')
    dot.attr('node', shape='record', fontname='Google Sans')

    # Define classes with their attributes and methods
    classes = {
        'User': {
            'attributes': [
                '+ UserID: Integer',
                '+ Username: String',
                '+ PasswordHash: String',
                '+ Role: Enum',
                '+ ContactInfo: String'
            ],
            'methods': []
        },
        'Supplier': {
            'attributes': [
                '+ SupplierID: Integer',
                '+ Name: String',
                '+ ContactInfo: String',
                '+ Address: String'
            ],
            'methods': []
        },
        'Category': {
            'attributes': [
                '+ CategoryID: Integer',
                '+ Name: String',
                '+ Description: Text'
            ],
            'methods': []
        },
        'Location': {
            'attributes': [
                '+ LocationID: Integer',
                '+ Aisle: String',
                '+ Shelf: String',
                '+ Bin: String'
            ],
            'methods': []
        },
        'Product': {
            'attributes': [
                '+ ProductID: Integer',
                '+ Name: String',
                '+ Description: Text',
                '+ QuantityInStock: Integer',
                '+ ReorderLevel: Integer',
                '+ CategoryID: Integer',
                '+ SupplierID: Integer',
                '+ LocationID: Integer'
            ],
            'methods': []
        },
        'PurchaseOrder': {
            'attributes': [
                '+ OrderID: Integer',
                '+ OrderDate: Date',
                '+ Status: Enum',
                '+ TotalAmount: Decimal',
                '+ SupplierID: Integer',
                '+ ManagerID: Integer'
            ],
            'methods': []
        },
        'OrderItem': {
            'attributes': [
                '+ OrderItemID: Integer',
                '+ Quantity: Integer',
                '+ UnitPrice: Decimal',
                '+ OrderID: Integer',
                '+ ProductID: Integer'
            ],
            'methods': []
        },
        'InventoryMovement': {
            'attributes': [
                '+ MovementID: Integer',
                '+ Quantity: Integer',
                '+ MovementDate: DateTime',
                '+ MovementType: Enum',
                '+ ProductID: Integer',
                '+ FromLocationID: Integer',
                '+ ToLocationID: Integer',
                '+ UserID: Integer'
            ],
            'methods': []
        },
        'ReorderThreshold': {
            'attributes': [
                '+ ProductID: Integer',
                '+ ManagerID: Integer',
                '+ ThresholdQuantity: Integer'
            ],
            'methods': []
        }
    }

    # Add classes to the graph
    for class_name, class_content in classes.items():
        label = f'{{{class_name}'
        if class_content['attributes']:
            label += '|' + '\\l'.join(class_content['attributes']) + '\\l'
        if class_content['methods']:
            label += '|' + '\\l'.join(class_content['methods']) + '\\l'
        label += '}'
        dot.node(class_name, label=label)

    # Define relationships
    relationships = [
        # (From, To, Type, Label)
        ('Product', 'Category', 'association', ''),
        ('Product', 'Supplier', 'association', ''),
        ('Product', 'Location', 'association', ''),
        ('Product', 'OrderItem', 'association', ''),
        ('Product', 'InventoryMovement', 'association', ''),
        ('Product', 'ReorderThreshold', 'association', ''),
        ('User', 'InventoryMovement', 'association', ''),
        ('User', 'PurchaseOrder', 'association', ''),
        ('User', 'ReorderThreshold', 'association', ''),
        ('PurchaseOrder', 'Supplier', 'association', ''),
        ('PurchaseOrder', 'OrderItem', 'aggregation', ''),
        ('PurchaseOrder', 'User', 'association', 'Manager'),
        ('OrderItem', 'Product', 'association', ''),
        ('InventoryMovement', 'Location', 'association', ''),
    ]

    # Add relationships to the graph
    for from_class, to_class, rel_type, label in relationships:
        if rel_type == 'association':
            dot.edge(from_class, to_class, label=label)
        elif rel_type == 'aggregation':
            dot.edge(from_class, to_class, label=label, arrowhead='odiamond')
        elif rel_type == 'composition':
            dot.edge(from_class, to_class, label=label, arrowhead='diamond')
        elif rel_type == 'inheritance':
            dot.edge(from_class, to_class, label=label, arrowhead='empty')

    # Specify the output file path inside the result folder
    output_file_path = os.path.join(output_dir, 'class_diagram')

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
    create_class_diagram()
