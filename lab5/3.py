import re
def sequence(txt):
    a = r"\b[a-z]+_[a-z]+\b"
    match = re.findall(a, txt)
    return match
txt = input("Enter a sentence: ")
matches = sequence(txt)
print(matches if matches else "Does not match")