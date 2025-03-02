import os
path = input("Enter the path: ")
if os.path.exists(path): 
    print("Exists")
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))
else:
    print("Does not exist")