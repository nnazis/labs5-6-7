import re
def replace(txt):
    return re.sub(r"[ ,.]", ":", txt)
text = input(" Enter text: ")
output = replace(text)
print(output)