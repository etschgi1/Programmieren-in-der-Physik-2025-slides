with open("slides/08/examples/testfile2.txt", "w", encoding="UTF-8") as f:
    f.write("Hello, Österreich!\n")
    
with open("slides/08/examples/testfile2.txt", "r", encoding="ASCII") as f:
    data = f.read()
    print(f"Original data: {data}")