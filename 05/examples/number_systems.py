dec = 42
bin_num = bin(dec)  # 0b101010
oct_num = oct(dec)  # 0o52
hex_num = hex(dec)  # 0x2a
# other way around
new_hex = 0xFF
new_oct = 0o77
dec_new_hex = int(new_hex)  # 255
dec_new_oct = int(new_oct)  # 63
# using 17 as a base
base17 = int("F0", base=17)  # 255
