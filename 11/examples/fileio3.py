with open('slides/08/examples/input.txt', 'a') as f:
    f.write("This is a test file.\n")
    f.writelines(["Boring text 1.\n", "Boring text 2.\n"])
with open('slides/08/examples/input.txt', 'r') as f:
    for line in f.readlines():
        print(line, end="")