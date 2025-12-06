def hello():
    print("Hello, world!")


def arguments(a, b, c):
    print("Got arguments:", a, b, c)


def return_value():
    return 42


def add(a, b=2):
    return a + b


add_two_arguments = add(30, 12)
add_one_argument = add(40)
