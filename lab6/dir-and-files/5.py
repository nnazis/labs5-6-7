path = input("Enter the file path: ")
lst = ["Python", "is", "a", "powerful", "language"]
try:
    with open(path, 'w', encoding='utf-8') as file:
        for item in lst:
            file.write(item + '\n')
    print(path)
except Exception as e:
    print(e)