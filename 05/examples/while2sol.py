def add(a, b):
    return a + b


a, b = 0, 1
# multiple conditions can also be used
while a < 5 or add(a, b) < 15:
    print(a, b, end=", ")
    # same as a = b * 2 and b = a + b
    a, b = b * 2, a + b
# Output: 0 1, 2 1, 2 3, 6 5
