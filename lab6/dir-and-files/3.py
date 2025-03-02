import os
path = input("Enter a path: ")
if os.path.exists(path):
    print('Exists')
    dir_name = os.path.dirname(path)
    file_name = os.path.basename(path)
    print(dir_name)
    print(file_name)
else:
    print("Does not exist")