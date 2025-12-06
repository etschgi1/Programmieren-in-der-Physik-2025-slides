# Using list comprehension
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [x for x in original_list if x % 2 == 0]
print(even)  # Output: [2, 4, 6, 8, 10]
# Using for loop and if statements
even = []
for x in original_list:
    if x % 2 == 0:
        even.append(x)
print(even)  # Output: [2, 4, 6, 8, 10]
