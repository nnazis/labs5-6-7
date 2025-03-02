import os
path = input("Enter a path: ")
try:
    if os.path.exists(path):
        os.remove(path)
        print("file has been deleted")
    else:
        print("file does not exist")
except Exception as e:
    print(e)