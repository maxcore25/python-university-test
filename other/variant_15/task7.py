def main(x):
    A = x & 0b1111111111
    B = (x >> 10) & 0b1111111
    C = (x >> 17) & 0b111111111111
    D = (x >> 29) & 0b1
    E = (x >> 30) & 0b11

    fake = 0
    fake |= B
    fake |= C << 7
    fake |= A << 19
    fake |= E << 29
    fake |= D << 31
    return fake


print(hex(main(0x01f0610e)))
print(hex(main(0x9c3adbe6)))
print(hex(main(0x24e59796)))
print(hex(main(0x4fb1a465)))
print(hex(main(0x2d16c218)))
