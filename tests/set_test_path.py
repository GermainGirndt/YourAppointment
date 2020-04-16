import os
import sys

project_root_path_name = "/your_appointment"
sys.path.insert(0, (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) + project_root_path_name )
print(f"\nPath to be tested setted to: {sys.path}\n\n")