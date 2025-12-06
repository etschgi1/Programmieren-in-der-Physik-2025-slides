adder = lambda x, y: x + y
print(adder(1, 2)) # 3
adder_default = lambda x, y=1: x + y
print(adder_default(1)) # 2
adder_lambda = lambda x: lambda y: x + y
print(adder_lambda(1)(2)) # 3