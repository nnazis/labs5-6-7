import math
def multiply(nums):
    return math.prod(nums)
numbers = list(map(int,input("Enter numbers: ").split()))
result = multiply(numbers)
print(result)