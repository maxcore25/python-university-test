def main(inp):
    a = (inp & 0b00000000000000000000000000000011) << 21
    b = (inp & 0b00000000000000000000000000111100) >> 2
    c = (inp & 0b00000000000000000011111111000000) >> 2
    d = (inp & 0b00000000011111111100000000000000) >> 2
    e = (inp & 0b01111111100000000000000000000000) << 0
    f = (inp & 0b10000000000000000000000000000000) << 0

    return a | b | c | d | e | f


print(hex(main(0xac3099a9)))
print(hex(main(0x9edd5434)))
print(hex(main(0x22c4cb20)))
print(hex(main(0x566cdaad)))
print(hex(main(0xfbf2543c)))
