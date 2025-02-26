def all_true(e):
    return all(e)
values = tuple(map(int, input('Enter numbers: ').split()))
result = all_true(values)
print(result)