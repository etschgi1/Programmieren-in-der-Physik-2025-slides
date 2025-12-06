my_list = [x for x in range(1, 5)]
print(my_list)  # [1, 2, 3, 4]
odds = [x for x in my_list if x % 2 != 0]
print(odds)  # [1, 3]
