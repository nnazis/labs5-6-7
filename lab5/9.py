import re
def insert_spaces(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
user_input = input("Enter string: ")
output_text = insert_spaces(user_input)
print(output_text)
