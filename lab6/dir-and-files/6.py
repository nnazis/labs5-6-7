import string
directory = input("Enter the directory: ")
try:
    for letter in string.ascii_uppercase:
        file_name = f"{directory}/{letter}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"{letter}.txt\n")
    print("created")
except Exception as e:
    print(e)