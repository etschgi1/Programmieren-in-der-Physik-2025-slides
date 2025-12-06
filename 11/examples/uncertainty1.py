from uncertainties import ufloat

x = ufloat(2.0, 0.1)  # 2.0 +/- 0.1
y = ufloat(1.0, 0.2)  # 1.0 +/- 0.2
#...
z = x + y
print(z)  # 3.00 +/- 0.223606797749979
print(z.nominal_value)  # 3.0
print(z.std_dev)  # 0.223606797749979
print(z.n)  # 3.0
print(z.s)  # 0.223606797749979