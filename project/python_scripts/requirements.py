# python script to extract the module versions used in the project and save 
# them to a requirements.txt file.


# Importing the modules without aliasing
import re
import pandas
import numpy
import matplotlib
import seaborn
import os
import requests
import tensorflow

# zipfile and os not included as included in base installation of python
# os module is used use to get the project directory, but it is not included in the 
# requirements.txt file

# Read the source file to extract imports
modules = []
with open(__file__, "r") as file:
    lines = file.readlines()
    for line in lines:
        # Use regex to match import statements without aliasing
        match = re.match(r"^import\s+(\w+)$", line.strip())
        if match:
            module_name = match.group(1)
            # Avoid adding the `re` module to the list
            if module_name != "os":
                modules.append(module_name)

# Get the project directory
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Path to requirements.txt
requirements_path = os.path.join(project_dir, 'requirements.txt')

# Check if requirements.txt exists, if not create it
if not os.path.exists(requirements_path):
    with open(requirements_path, 'w') as f:
        pass

# Open the requirements.txt file for writing
with open(requirements_path, "w") as f:
    for module_name in modules:
        # Dynamically import the module and get its version
        module = globals()[module_name]
        module_info = f"{module.__name__}=={module.__version__}"
        f.write(module_info + "\n")  # Save to file

print(f"Module versions written to {requirements_path}")