def main(input):
    A = (input & 0b00000000000000001111111111111111) << 3
    B = (input & 0b00000000000001110000000000000000) >> 16
    C = (input & 0b11111111111110000000000000000000)
    return C | A | B


print(hex(main(0x0004a432)))
print(hex(main(0x8dd30f80)))
print(hex(main(0xe8985dbc)))
print(hex(main(0xb1718cd9)))
print(hex(main(0x3e0b7c8d)))
