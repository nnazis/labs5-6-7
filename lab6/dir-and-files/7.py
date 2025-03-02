first = input("Enter the contest: ")
second = input("Enter the destination file: ")
try:
    with open(first, 'r', encoding='utf-8') as src:
        content = src.read()
    with open(second, 'w', encoding='utf-8') as dest:
        dest.write(content)
    print("copied")
except FileNotFoundError:
    print("file not found")
except Exception as e:
    print(e)

