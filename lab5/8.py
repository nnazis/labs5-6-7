import re
def split_uppercase(s):
    return re.findall(r"[A-Z][^A-Z]*", s)
user = input("Enter a string: ")
output = split_uppercase(user)
print(output)