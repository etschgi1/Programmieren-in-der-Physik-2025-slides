import os

with open('data.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')

with open('data.bin', 'rb') as f:
    data = f.read()
    print(f"Original data: {data}")