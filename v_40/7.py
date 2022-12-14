def main(inp):
    a = (inp & 0b00000000000000000000000000000001) << 7
    b = (inp & 0b00000000000000000000000001111110) << 7
    c = (inp & 0b00000000000000000111111110000000) << 17
    d = (inp & 0b00000000000111111000000000000000) >> 15
    e = (inp & 0b00011111111000000000000000000000) >> 5
    f = (inp & 0b01100000000000000000000000000000) >> 15
    g = (inp & 0b10000000000000000000000000000000) >> 25

    return a | b | c | d | e | f | g


print(hex(main(0x44cf4fa6)))
print(hex(main(0x38317cb0)))
print(hex(main(0x0e3f48ee)))
print(hex(main(0x5ca2f9fc)))
print(hex(main(0xb2df7de8)))
