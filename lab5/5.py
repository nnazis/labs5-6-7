import re
def matches(txt):
    a = r"^a*.*b$"
    if re.fullmatch(a, txt):
        print("Matches")
    else: 
        print("Does not match")
txt = input("Enter a word: ")
matches(txt)