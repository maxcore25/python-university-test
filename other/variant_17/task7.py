

def main(x):
    A = x & 0b111111
    B = (x >> 6) & 0b11111
    C = (x >> 11) & 0b11111
    D = (x >> 16) & 0b11111111111111
    E = (x >> 30) & 0b11

    fake = 0
    fake |= C << 0
    fake |= E << 5
    fake |= B << 7
    fake |= D << 12
    fake |= A << 26
    return fake


print(hex(main(0x9cd3bcfd)))
print(hex(main(0xf58de237)))
print(hex(main(0xfa9891a3)))
print(hex(main(0x6e31dffb)))
print(hex(main(0x62f6be8a)))
