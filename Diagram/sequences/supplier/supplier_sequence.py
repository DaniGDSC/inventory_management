import os
from graphviz import Digraph

# Function to generate a sequence diagram and save it as PNG
def supplier_sequence_diagram(filename, interactions):
    # Ensure the output directory exists
    output_dir = 'supplier'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a new directed graph (sequence diagram)
    dot = Digraph('supplier_diagram', format='png')
    dot.attr(rankdir='TB', size='15')
    
    # Define actors and participants
    dot.node('S', 'Supplier', shape='rect')
    dot.node('IS', 'Inventory System', shape='rect')
    dot.node('DB', 'Database', shape='rect')
    dot.node('WS', 'Warehouse Staff', shape='rect')

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
def view_purchase_orders():
    interactions = [
        {'from': 'S', 'to': 'IS', 'label': 'Log in'},
        {'from': 'S', 'to': 'IS', 'label': 'Select "View Purchase Orders"'},
        {'from': 'IS', 'to': 'DB', 'label': 'Fetch outstanding orders'},
        {'from': 'DB', 'to': 'IS', 'label': 'Return purchase order details'},
        {'from': 'IS', 'to': 'S', 'label': 'Display purchase orders'}
    ]
    supplier_sequence_diagram('view_purchase_orders', interactions)

def update_order_status():
    interactions = [
        {'from': 'S', 'to': 'IS', 'label': 'Log in'},
        {'from': 'S', 'to': 'IS', 'label': 'Select "Update Order Status"'},
        {'from': 'IS', 'to': 'S', 'label': 'Prompt for order and status details'},
        {'from': 'S', 'to': 'IS', 'label': 'Submit order status update'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update order status in database'},
        {'from': 'DB', 'to': 'IS', 'label': 'Order status updated'},
        {'from': 'IS', 'to': 'S', 'label': 'Confirmation of status update'}
    ]
    supplier_sequence_diagram('update_order_status', interactions)

def communicate_with_warehouse():
    interactions = [
        {'from': 'S', 'to': 'IS', 'label': 'Log in'},
        {'from': 'S', 'to': 'IS', 'label': 'Select "Communicate with Warehouse"'},
        {'from': 'IS', 'to': 'WS', 'label': 'Send communication to warehouse staff'},
        {'from': 'WS', 'to': 'IS', 'label': 'Respond to supplier'},
        {'from': 'IS', 'to': 'S', 'label': 'Display warehouse staff response'}
    ]
    supplier_sequence_diagram('communicate_with_warehouse', interactions)

# Main function to generate all sequence diagrams
if __name__ == "__main__":
    view_purchase_orders()
    update_order_status()
    communicate_with_warehouse()
