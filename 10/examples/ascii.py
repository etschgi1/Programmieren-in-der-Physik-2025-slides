with open('slides/08/examples/ascii.txt', 'wb') as f:
    f.write(b'\x41\x42\x43') 

with open('slides/08/examples/ascii.txt', 'r', encoding='ascii') as f:
    print(f.read()) # ABC

with open('slides/08/examples/ascii.txt', 'wb') as f:
    f.write(b'\x41\x42\x43\xD6')

with open('slides/08/examples/ascii.txt', 'r', encoding='ISO-8859-1') as f:
    print(f.read()) # ABCÖ
