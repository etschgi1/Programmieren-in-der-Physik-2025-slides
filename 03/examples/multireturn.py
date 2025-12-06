def multireturn(a, b):
    sum_ = a + b
    product = a * b
    return sum_, product


my_sum, my_product = multireturn(3, 4)
print(my_sum)  # 7
print(my_product)  # 12
