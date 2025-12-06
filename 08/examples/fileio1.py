with open("slides/08/examples/testfile1.txt", "w") as f:
    f.write("Hello, world!\n")
    f.write("This is a test file.\n")

with open("slides/08/examples/testfile1.txt", "r") as f:
    for line in f:
        print(line, end="")