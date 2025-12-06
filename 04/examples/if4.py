x = 42
if x > 0:
    print("x is positive")
elif x == 42:
    print("x is 42")
else:
    print("x is <= 0")


x = 42
if x > 0:
    print("x is positive")
# elif not triggered because x > 0 is True
elif x == 42:
    print("x is 42")
else:
    print("x is <= 0")

x = 42
if x > 0:
    print("x is positive")
# if triggered anyway!
if x == 42:
    print("x is 42")
else:
    print("x is <= 0")