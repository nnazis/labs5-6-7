import os
path = input("Enter the directory: ")
if os.path.exists(path):
    print("\nDirectories: ")
    print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("\nFiles: ")
    print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("\nAll Directories and Files: ")
    print(os.listdir(path))
else: 
    print("No such directory")