name = input("Name: ")
print("Hello, " + name + "!")
age = input("Age: ")
try:
    age = int(age)
except ValueError:
    print(f"{age} is not a valid age.")
    quit()
print("You are " + str(age) + " years old.")