def greeting(num, name="World"):
    for _ in range(num):  # _ is a dummy
        print("Hello, " + name)


greeting(2)
# Hello, World
# Hello, World
greeting(1, "Python")  # Hello, Python
