import re
def replace(txt):
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", txt).lower()
user = input("Enter a string: ")
output = replace(user)
print(output)