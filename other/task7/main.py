def main(x):
    A = x & 0b1
    B = (x >> 1) & 0b11
    C = (x >> 3) & 0b111111111111111
    D = (x >> 18) & 0b111
    E = (x >> 21) & 0b1
    F = (x >> 22) & 0b111111
    G = (x >> 28) & 0b1111

    fake = 0
    fake |= F
    fake |= C << 6
    fake |= A << 21
    fake |= E << 22
    fake |= G << 23
    fake |= D << 27
    fake |= B << 30
    return fake


print(hex(main(0xc935f95c)))
print(hex(main(0x29c3dd6f)))
print(hex(main(0x413081b6)))
print(hex(main(0x1a9f7918)))
print(hex(main(0x99444247)))
