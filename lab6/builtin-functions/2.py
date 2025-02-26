def count(a):
    upper = sum(1 for char in a if char.isupper())
    lower = sum(1 for char in a if char.islower())
    print(upper)
    print(lower)
txt = input("Enter a string: ")
count(txt)