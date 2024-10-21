import os
from graphviz import Digraph

def create_sequence_diagram():
    # Ensure the output directory exists
    output_dir = 'warehouse_staff'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create a new directed graph (sequence diagram)
    dot = Digraph('SequenceDiagram', format='png')
    dot.attr(rankdir='TB', size='15')

    # Define participants (actors and systems)
    dot.node('WS', 'WarehouseStaff')
    dot.node('IS', 'InventorySystem')
    dot.node('DB', 'Database')

    # Define interactions (messages)
    dot.edge('WS', 'IS', 'Log in')
    dot.edge('WS', 'IS', 'Select "Check-In Inventory"')
    dot.edge('IS', 'WS', 'Prompt for item details')
    dot.edge('WS', 'IS', 'Submit item details (Product, Quantity)')
    dot.edge('IS', 'DB', 'Update inventory')
    dot.edge('DB', 'IS', 'Inventory updated')
    dot.edge('IS', 'WS', 'Confirmation of inventory update')

    # Specify the output file path
    output_file_path = os.path.join(output_dir, 'sequence_diagram')

    try:
        # Render the diagram to a file
        dot.render(output_file_path, view=True)
        print(f"Diagram successfully created and saved at: {output_file_path}.png")
    except Exception as e:
        print(f"Error while rendering diagram: {e}")

if __name__ == "__main__":
    create_sequence_diagram()
