import os
import sys

project_root_path_name = "/your_appointment"
sys.path.insert(0, (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) + project_root_path_name )
print(f"\nMain test path setted to: {sys.path[0]}\n\n")