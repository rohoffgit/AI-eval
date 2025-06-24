# Create conda environment, i.e. conda create -n azureai_py3_12 python=3.12

# Execute this script to set up the environment (see environment.yml).
# It reads the environment.yml file and installs the required packages.
# Ensure you have 'pip' and 'python' installed in your system.
# To execute run in terminal: python 00_setup.py
import os
os.system('pip install pyyaml')
import yaml 

with open("environment.yml") as file_handle:
    environment_data = yaml.safe_load(file_handle)

for dependency in environment_data["dependencies"]:
    if isinstance(dependency, str) and dependency.startswith("python"):
      python_version = os.popen("python --version").read().strip()
      print(f"Current Python version: {python_version}")
      print(f'Expected Python version: {dependency}                                                                                                                                                                                                       ')
    
    if isinstance(dependency, dict):
      for lib in dependency['pip']:
        print(f"\nInstalling {lib}...")
        com =f"pip install --user --upgrade {lib}"
        print(com)
        ret = os.system(com)
        if ret != 0:
            print(f"ERROR: Failed to install {lib}.")
