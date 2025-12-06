names = ['Alice', 'Bob', 'Charlie', 'Diana']
age = [22, 42, 16, 50]
for number, name in enumerate(names):
    print(f"{name} is {age[number]} old", end=", ")
    # Alice is 22 old, Bob is 42 old, ...

for name, age in zip(names, age):
    print(f"{name} is {age} old", end=", ")
    # same output as above
