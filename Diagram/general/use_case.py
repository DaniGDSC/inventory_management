import os
import graphviz
from graphviz import Digraph

# Directory to store the result
output_dir = 'result'

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize the Digraph
dot = Digraph('UseCaseDiagram', format='png')

# Set global graph attributes
dot.attr(rankdir='LR', size='15')
dot.attr('node', shape='ellipse', style='filled', color='lightblue2', fontname="Helvetica")

# Define the system boundary
with dot.subgraph(name='cluster_system') as c:
    c.attr(label='Inventory Management System', fontsize='20')
    c.attr(style='rounded,filled', color='lightgrey', fillcolor='white')

    # Define use cases
    # Warehouse Staff Use Cases
    c.node('UC1', 'Check-In Inventory')
    c.node('UC2', 'Check-Out Inventory')
    c.node('UC3', 'Transfer Inventory')

    # Manager Use Cases
    c.node('UC4', 'Approve Purchase Orders')
    c.node('UC5', 'Generate Reports')
    c.node('UC6', 'Set Reordering Thresholds')

    # Supplier Use Cases
    c.node('UC7', 'View Purchase Orders')
    c.node('UC8', 'Update Order Status')
    c.node('UC9', 'Communicate with Warehouse')

# Define actors
dot.attr('node', shape='plaintext')
dot.node('Actor1', 'Warehouse Staff')
dot.node('Actor2', 'Manager')
dot.node('Actor3', 'Supplier')

# Define associations
# Warehouse Staff associations
dot.edge('Actor1', 'UC1')
dot.edge('Actor1', 'UC2')
dot.edge('Actor1', 'UC3')

# Manager associations
dot.edge('Actor2', 'UC4')
dot.edge('Actor2', 'UC5')
dot.edge('Actor2', 'UC6')

# Supplier associations
dot.edge('Actor3', 'UC7')
dot.edge('Actor3', 'UC8')
dot.edge('Actor3', 'UC9')

# Specify the output file path inside the result folder
output_file_path = os.path.join('F:/inventory_management-1/Diagram/result', 'use_case_diagram')

# Render the diagram to the result folder
dot.render(output_file_path, view=False)

# Open and read the file if needed
with open(f'{output_file_path}.png', 'rb') as file:
    result = file.read()

# The diagram is now stored in the 'result' folder as 'use_case_diagram.png'
