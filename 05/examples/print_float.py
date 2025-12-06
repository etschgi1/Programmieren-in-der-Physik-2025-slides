x = 42.42
y = 3.15
print(f"{x:.2f} + {y:.2f} = {(x+y):.2f}")
# a different way to do the same thing
print("{:.2f} + {:.2f} = {:.2f}".format(x, y, x + y))
# another way
print("%0.2f + %0.2f = %0.2f" % (x, y, x + y))
# Output: 42.42 + 3.15 = 45.57
