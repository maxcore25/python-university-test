def main(x):
    A = x & 0b1
    B = (x >> 1) & 0b11
    C = (x >> 3) & 0b111111111111
    D = (x >> 15) & 0b1111111
    E = (x >> 22) & 0b111111111
    F = (x >> 31) & 0b1

    fake = 0
    fake |= D
    fake |= C << 7
    fake |= E << 19
    fake |= B << 28
    fake |= F << 30
    fake |= A << 31
    return fake


print(hex(main(0x557f9c9c)))
print(hex(main(0x5d524f94)))
print(hex(main(0x8bd4cca9)))
print(hex(main(0x9029c347)))
print(hex(main(0x25dee11c)))
