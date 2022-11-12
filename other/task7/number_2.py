def main(x):
    A = x & 0b111
    B = (x >> 3) & 0b1111111
    C = (x >> 10) & 0b111111111111
    D = (x >> 22) & 0b1
    E = (x >> 23) & 0b1111
    F = (x >> 27) & 0b11
    G = (x >> 29) & 0b111

    fake = 0
    fake |= B
    fake |= F << 7
    fake |= C << 9
    fake |= G << 21
    fake |= A << 24
    fake |= D << 27
    fake |= E << 28
    return fake


print(hex(main(0xa8093612)))
print(hex(main(0x12fc070c)))
print(hex(main(0xf85ad639)))
print(hex(main(0xba82f86f)))
print(hex(main(0xe0245f95)))
