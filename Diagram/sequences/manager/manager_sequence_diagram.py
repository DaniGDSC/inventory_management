import os
from graphviz import Digraph

# Function to generate a sequence diagram and save it as PNG
def manager_sequence_diagram(filename, interactions):
    # Ensure the output directory exists
    output_dir = 'manager'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a new directed graph (sequence diagram)
    dot = Digraph('manager_diagram', format='png')
    dot.attr(rankdir='TB', size='15')
    
    # Define actors and participants
    dot.node('M', 'Manager', shape='rect')
    dot.node('IS', 'Inventory System', shape='rect')
    dot.node('DB', 'Database', shape='rect')
    dot.node('S', 'Supplier', shape='rect')

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
def approve_purchase_order():
    interactions = [
        {'from': 'M', 'to': 'IS', 'label': 'Log in'},
        {'from': 'M', 'to': 'IS', 'label': 'View pending purchase orders'},
        {'from': 'IS', 'to': 'DB', 'label': 'Fetch pending orders'},
        {'from': 'DB', 'to': 'IS', 'label': 'Return pending orders'},
        {'from': 'M', 'to': 'IS', 'label': 'Approve purchase order'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update purchase order status'},
        {'from': 'DB', 'to': 'IS', 'label': 'Status updated'},
        {'from': 'IS', 'to': 'S', 'label': 'Notify supplier of approval'}
    ]
    manager_sequence_diagram('approve_purchase_order', interactions)

def generate_reports():
    interactions = [
        {'from': 'M', 'to': 'IS', 'label': 'Log in'},
        {'from': 'M', 'to': 'IS', 'label': 'Select "Generate Reports"'},
        {'from': 'IS', 'to': 'DB', 'label': 'Fetch data for reports'},
        {'from': 'DB', 'to': 'IS', 'label': 'Return report data'},
        {'from': 'IS', 'to': 'M', 'label': 'Display generated report'}
    ]
    manager_sequence_diagram('generate_reports', interactions)

def set_reordering_thresholds():
    interactions = [
        {'from': 'M', 'to': 'IS', 'label': 'Log in'},
        {'from': 'M', 'to': 'IS', 'label': 'Select "Set Reordering Thresholds"'},
        {'from': 'IS', 'to': 'M', 'label': 'Prompt for product details and threshold quantity'},
        {'from': 'M', 'to': 'IS', 'label': 'Submit threshold details'},
        {'from': 'IS', 'to': 'DB', 'label': 'Update product reordering thresholds in database'},
        {'from': 'DB', 'to': 'IS', 'label': 'Reordering threshold updated'},
        {'from': 'IS', 'to': 'M', 'label': 'Confirmation of threshold update'}
    ]
    manager_sequence_diagram('set_reordering_thresholds', interactions)

# Main function to generate all sequence diagrams
if __name__ == "__main__":
    approve_purchase_order()
    generate_reports()
    set_reordering_thresholds()
