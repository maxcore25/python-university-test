def main(x):
    A = x & 0b1
    B = (x >> 1) & 0b1111111111
    C = (x >> 11) & 0b111111111
    D = (x >> 20) & 0b111111
    E = (x >> 26) & 0b1111
    F = (x >> 30) & 0b1
    G = (x >> 31) & 0b1

    fake = 0
    fake |= E
    fake |= D << 4
    fake |= C << 10
    fake |= G << 19
    fake |= F << 20
    fake |= A << 21
    fake |= B << 22
    return fake


print(hex(main(0xc989363c)))
print(hex(main(0x56481e1c)))
print(hex(main(0x64498e35)))
print(hex(main(0xf643e2b8)))
print(hex(main(0x07cb88e4)))
