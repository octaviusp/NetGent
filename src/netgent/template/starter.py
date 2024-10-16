import os
import sys
from pathlib import Path

def netgent_start():
    current_dir = os.getcwd()
    script_path = Path(__file__).parent / "netgent_start.py"
    
    if not script_path.exists():
        print(f"Error: netgent_start.py not found in {script_path}")
        return

    sys.path.append(str(script_path.parent))
    
    from netgent.template.netgent_start import create_project_structure
    
    create_project_structure()
    print(f"Netgent project structure created in {current_dir}")

if __name__ == "__main__":
    netgent_start()

