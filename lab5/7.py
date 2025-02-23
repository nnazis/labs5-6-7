import re
def replace(snake_str):
    return re.sub(r"_([a-zA-Z])", lambda match: match.group(1).upper(), snake_str)
user = input("Enter a string: ")
output = replace(user)
print(output)