import os
path = input("Enter the file path: ")
try:
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(len(lines))
except FileNotFoundError:
    print("Error")
except Exception as e:
    print(e)