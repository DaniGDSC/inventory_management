import os
from graphviz import Digraph

# Function to generate a sequence diagram and save it as PNG
def staff_sequence_diagram(filename, interactions):
    # Ensure the output directory exists
    output_dir = 'warehouse_staff'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a new directed graph (sequence diagram)
    dot = Digraph('staff_diagram', format='png')
    dot.attr(rankdir='TB', size='8,5')
    
    # Define actors and participants
    dot.node('WS', 'Warehouse Staff', shape='rect')
    dot.node('IS', 'Inventory System', shape='rect')
    dot.node('DB', 'Database', shape='rect')

    # Add interactions (arrows between the actors and system)
    for interaction in interactions:
        dot.edge(interaction['from'], interaction['to'], label=interaction['label'])

    # Output file path
    output_file = os.path.join(output_dir, f"{filename}.png")
    
    try:
        # Render the diagram to a file
        dot.render(output_file, view=False)
        print(f"Sequence diagram saved as: {output_file}")
    except Exception as e:
        print(f"Error while rendering diagram: {e}")

# Define interactions for each use case
def check_in_inventory():
    interactions = [
        {'from': 'WS', 'to': 'IS', 'label': 'Log in'},
        {'from': 'WS', 'to': 'IS', 'label': 'Select "Check-In Inventory"'},
        {'from': 'IS', 'to': 'WS', 'label': 'Prompt for item details'},
        {'from': 'WS', 'to': 'IS', 'label': 'Submit item details (Product, Quantity)'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update inventory'},
        {'from': 'DB', 'to': 'IS', 'label': 'Inventory updated'},
        {'from': 'IS', 'to': 'WS', 'label': 'Confirmation of inventory update'}
    ]
    staff_sequence_diagram('check_in_inventory', interactions)

def check_out_inventory():
    interactions = [
        {'from': 'WS', 'to': 'IS', 'label': 'Log in'},
        {'from': 'WS', 'to': 'IS', 'label': 'Select "Check-Out Inventory"'},
        {'from': 'IS', 'to': 'WS', 'label': 'Prompt for item details (Product, Quantity)'},
        {'from': 'WS', 'to': 'IS', 'label': 'Submit item details'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update inventory (reduce quantity)'},
        {'from': 'DB', 'to': 'IS', 'label': 'Inventory updated'},
        {'from': 'IS', 'to': 'WS', 'label': 'Confirmation of inventory check-out'}
    ]
    staff_sequence_diagram('check_out_inventory', interactions)

def transfer_inventory():
    interactions = [
        {'from': 'WS', 'to': 'IS', 'label': 'Log in'},
        {'from': 'WS', 'to': 'IS', 'label': 'Select "Transfer Inventory"'},
        {'from': 'IS', 'to': 'WS', 'label': 'Prompt for product details and locations'},
        {'from': 'WS', 'to': 'IS', 'label': 'Submit transfer details'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update product location in database'},
        {'from': 'DB', 'to': 'IS', 'label': 'Location updated'},
        {'from': 'IS', 'to': 'WS', 'label': 'Confirmation of inventory transfer'}
    ]
    staff_sequence_diagram('transfer_inventory', interactions)

def view_inventory_levels():
    interactions = [
        {'from': 'WS', 'to': 'IS', 'label': 'Log in'},
        {'from': 'WS', 'to': 'IS', 'label': 'Select "View Inventory Levels"'},
        {'from': 'IS', 'to': 'DB', 'label': 'Fetch inventory levels'},
        {'from': 'DB', 'to': 'IS', 'label': 'Return stock levels'},
        {'from': 'IS', 'to': 'WS', 'label': 'Display inventory levels'}
    ]
    staff_sequence_diagram('view_inventory_levels', interactions)

def receive_returned_items():
    interactions = [
        {'from': 'WS', 'to': 'IS', 'label': 'Log in'},
        {'from': 'WS', 'to': 'IS', 'label': 'Select "Receive Returned Items"'},
        {'from': 'IS', 'to': 'WS', 'label': 'Prompt for return details'},
        {'from': 'WS', 'to': 'IS', 'label': 'Submit return details'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update inventory'},
        {'from': 'DB', 'to': 'IS', 'label': 'Inventory updated'},
        {'from': 'IS', 'to': 'WS', 'label': 'Confirmation of return processing'}
    ]
    staff_sequence_diagram('receive_returned_items', interactions)

# Main function to generate all sequence diagrams
if __name__ == "__main__":
    check_in_inventory()
    check_out_inventory()
    transfer_inventory()
    view_inventory_levels()
    receive_returned_items()
