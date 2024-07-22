import os
import subprocess
import shutil

# Define the base directory where the submodules will be installed
base_dir = 'base/submodules'

# Define the submodules with their respective paths and URLs
submodules = {
    "fedramp_automation": {
        "path": "fedramp_automation",
        "url": "https://github.com/GSA/fedramp-automation.git"
    },
    "cvss": {
        "path": "cvss",
        "url": "https://github.com/FIRSTdotorg/cvss-v4-calculator.git"
    },
    "oscal-rest": {
        "path": "oscal-rest",
        "url": "https://github.com/EasyDynamics/oscal-rest"
    }
}

def install_submodule(name, submodule):
    path = os.path.join(base_dir, submodule['path'])
    url = submodule['url']
    
    # Check if the submodule directory exists and remove it if it's not a valid git repository
    if os.path.exists(path):
        print(f"Removing existing directory {path} which is not a valid git repo.")
        shutil.rmtree(path)
    
    # Initialize and update the submodule
    try:
        subprocess.run(['git', 'submodule', 'add', url, path], check=True)
        subprocess.run(['git', 'submodule', 'update', '--init', '--recursive', path], check=True)
        print(f"Submodule {name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install submodule {name}: {e}")

if __name__ == "__main__":
    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Install each submodule
    for name, submodule in submodules.items():
        install_submodule(name, submodule)
