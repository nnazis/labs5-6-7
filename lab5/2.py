import re
txt = input("Enter a word: ")
a = r"ab{2,3}"
if re.fullmatch(a, txt):
    print("Mathces")
else:
    print("Does not match")