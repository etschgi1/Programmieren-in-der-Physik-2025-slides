my_list = [-1, 0, 1, 10, 42, 5]
if 0 in my_list:
    print("0 is in the list")
if all(x > 0 for x in my_list):
    print("all elements are positive")
if any(x > 0 for x in my_list):
    print("at least one element is positive")
