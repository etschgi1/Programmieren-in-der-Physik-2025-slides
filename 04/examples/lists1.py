numbers = [1, 2, 3, 4]  # Create a list
print(numbers)
print(numbers[0])  # Output: 1
numbers[0] = 10  # Change the first element
print(numbers)  # Output: [10, 2, 3, 4]
numbers.append(6)  # add 6 to the end 
print(numbers)  # Output: [10, 2, 3, 4, 6]
numbers.remove(3)  # remove 3
print(numbers)  # Output: [10, 2, 4, 6]
print(len(numbers))  # Output: 4
