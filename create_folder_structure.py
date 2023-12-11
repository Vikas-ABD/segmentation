import os

# Define the directory structure
directory_structure = {
    'app': {
        'templates': {},
        'static': {},
    },
    'model': {},
}

# Create the directories
for directory, subdirectories in directory_structure.items():
    os.makedirs(directory, exist_ok=True)
    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(directory, subdirectory)
        os.makedirs(subdirectory_path, exist_ok=True)